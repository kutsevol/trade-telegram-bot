from io import BytesIO

import pandas as pd


def extract_data_from_csv(file_buffer: BytesIO) -> pd.DataFrame:
    """
    It reads a CSV file from a buffer and returns a Pandas DataFrame

    :param file_buffer: The file buffer of the uploaded file
    :type file_buffer: BytesIO
    :return: A pandas dataframe
    """
    return pd.read_csv(file_buffer, sep=";|,", engine="python")
