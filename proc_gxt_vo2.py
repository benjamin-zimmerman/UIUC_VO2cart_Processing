import pandas as pd
import numpy as np


def minbyminVO2(xl_file):
    """
    Outputs the minute-by-minute VO2 for a participant from the raw GXT data.

    Parameters
    ----------
    xl_file : Excel file defined by the user
        Check in \\bi-cnl-nas3.beckman.illinois.edu\data\pea\epl_data\GXT_Excels

    Returns
    -------
    DataFrame
        DataFrame containing the minute-by-minute VO2 for the participant.
    """
    # Read in the Excel file
    df = pd.read_excel(xl_file, skiprows = 28, usecols = [0,2])
    
    # Find the index of the first row that has all NaNs, which corresponds to the first blank row in an Excel file
    first_row_with_all_NaN = df[df.isnull().all(axis=1) == True].index.tolist()[0]

    # Select rows from first row to first row with all NaNs
    df_clean = df.loc[0:first_row_with_all_NaN-1]

    return df_clean


def downsample_minbyminVO2(df, interval):
    """
    Downsamples the minute-by-minute VO2 data to a specified interval. The
    interval should be set to "2" for UIUC GXT output sampled at 2Hz.


    Parameters
    ----------
    df : DataFrame
        DataFrame containing the minute-by-minute VO2 for the participant.
    interval : int
        Interval to downsample the data to.

    Returns
    -------
    DataFrame
        DataFrame containing the downsampled minute-by-minute VO2 for the participant.
    """
    # Downsample the data to the specified interval
    df_downsampled = df.groupby(lambda x: x // interval).max()

    return df_downsampled