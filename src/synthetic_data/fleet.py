from sdv.single_table import TVAESynthesizer


def generate_synthetic_data(
    filename: str
) -> pandas.Dataframe:

    metadata = Metadata.detect_from_dataframes(data)
    synthesizer = TVAESynthesizer(metadata)    
    synthesizer = TVAESynthesizer(
        metadata, # required
        enforce_min_max_values=True,
        enforce_rounding=False,
        epochs=500
    )

    synthetic_data = synthesizer.sample(num_rows=100_000)

     