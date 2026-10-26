from sdv.single_table import TVAESynthesizer
import pandas as pd

def generate_synthetic_data(
    data: pd.DataFrame,
    epocs: int
) -> pd.DataFrame:
    metadata = Metadata.detect_from_dataframes(data)
    synthesizer = TVAESynthesizer(metadata)    
    synthesizer = TVAESynthesizer(
        metadata, 
        enforce_min_max_values=True,
        enforce_rounding=False,
        epochs=epochs
    )
    synthetic_data = synthesizer.sample(num_rows=100_000)
    return synthetic_data

     