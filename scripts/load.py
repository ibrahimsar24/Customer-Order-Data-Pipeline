import pandas as pd

def load_to_parquet(df, output_path):
    """Write DataFrame to Parquet file."""
    df.to_parquet(output_path, index=False)

def load_to_csv(df, output_path):
    """Write DataFrame to Parquet file."""
    df.to_csv(output_path, index=False)