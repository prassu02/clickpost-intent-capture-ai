import pandas as pd


def load_companies(path):
    """
    Load company list from CSV.
    """
    return pd.read_csv(path)


def save_dataframe(df, path):
    """
    Save DataFrame to CSV.
    """
    df.to_csv(path, index=False)


def print_header(title):
    """
    Print formatted section header.
    """
    print("=" * 60)
    print(title)
    print("=" * 60)


def save_signals(signals, output_path):
    """
    Save collected signals to CSV.
    """
    df = pd.DataFrame(signals)
    df.to_csv(output_path, index=False)

    print(f"Saved {len(df)} signals to {output_path}")