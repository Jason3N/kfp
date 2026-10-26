from kfp import dsl, compiler, client
from kfp.dsl import Input, Output, Dataset, Model
from synthetic_data.fleet import generate_synthetic_data
import pandas as pd

@dsl.component(base_image="python:3.12", packages_to_install=["pandas"])
def open_file(file: str, output_data: dsl.Output[dsl.Dataset]):
    import pandas as pd
    pd.read_csv(file).to_csv(output_data.path, index=False)

@dsl.component(base_image="python:3.12", packages_to_install=["pandas"])
def train_model(
    epochs: int,
    input_data: dsl.Input[dsl.Dataset],
    output_data: dsl.Output[dsl.Dataset]
  ): 
    import pandas as pd
    from sdv.metadata import Metadata
    from sdv.single_table import TVAESynthesizer
    synthetic_data = generate_synthetic_data(data=data, epochs=epochs).to_csv(output_data.path, index=False)

@dsl.pipeline
def run_synthetic_generation():
    data_task = open_file(file="data/StudentPerformance_csv")
    with dsl.ParallelFor(
        items=[100, 200, 300, 400],
    ) as epochs:
        trained_data = train_model(
            input_data=data_task.outputs["output_data"], 
            epochs=epochs)

if __name__ == '__main__':
    package_path = "synthetic_generation.yaml"
    compiler.Compiler().compile(
        pipeline_func=run_synthetic_generation,
        package_path=package_path
    )

    kfp_client = client.Client(host="http://127.0.0.1:8888")
    run = kfp_client.create_run_from_pipeline_package(
        pipeline_file=package_path,
        run_name="hello-jason",
        experiment_name="synthetic-experiment",
    )

    print(f"Submitted run: {run.run_id}")
