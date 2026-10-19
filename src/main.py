from kfp import dsl, compiler, client
import pandas as pd


@dsl.component
def open_file(
    file: str
) -> str:
    data = pd.to_csv

@dsl.component
def run_synthetic_generation(

)
    with dsl.ParallelFor(items=item_list, parallelism=10) as item:
        
)

@dsl.pipeline
def hello_pipeline(recipient: str) -> str:
    hello_task = say_hello(name=recipient)
    return hello_task.output


if __name__ == '__main__':
    package_path = "hello_pipeline.yaml"
    compiler.Compiler().compile(
        pipeline_func=hello_pipeline,
        package_path=package_path
    )

    kfp_client = client.Client(host="http://127.0.0.1:8888")
    run = kfp_client.create_run_from_pipeline_package(
        pipeline_file=package_path,
        arguments={"recipient": "Jason"},
        run_name="hello-jason",
        experiment_name="hello-experiment",
    )

    print(f"Submitted run: {run.run_id}")
