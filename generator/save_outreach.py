import pandas as pd


def save_outreach(outreach_data, output_file):
    """
    Save generated outreach messages to a CSV file.

    Parameters
    ----------
    outreach_data : list
        List of dictionaries containing outreach messages.

    output_file : Path
        Output CSV file path.
    """

    df = pd.DataFrame(outreach_data)

    df.to_csv(
        output_file,
        index=False
    )

    print(
        f"Saved {len(df)} outreach messages to {output_file}"
    )