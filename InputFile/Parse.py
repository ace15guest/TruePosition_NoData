import numpy as np
import pandas as pd


def DataCollectFROMCSV(file):
    """

    :param file:
    :return:
    """
    scale_to_microns = 1000
    # Headers of the file
    header = ['Measurement', 'Misc', 'Ideal', 'tolerance', 'tolerance min', 'Measured']
    # Create Temporary Dataframe to figure out # of rows to skip
    temp_df = pd.read_csv(r'{}'.format(file), names=header, skipinitialspace=True)
    rows_to_skip = temp_df[temp_df['Measurement'] == 'X'].index.values[0] - 1
    document = pd.read_csv(r'{}'.format(file), skiprows=rows_to_skip, names=header, index_col=False)
    # Deal With Missing Data

    # Gathering Values
    DM = np.asarray(document[document['Measurement'].str.contains('Diam')]['Measured'].values)*scale_to_microns
    XI = np.asarray(document[document['Measurement'].str.contains('X')]['Ideal'].values)*scale_to_microns
    YI = np.asarray(document[document['Measurement'].str.contains('Y')]['Ideal'].values)*scale_to_microns
    XM = np.asarray(document[document['Measurement'].str.contains('X')]['Measured'].values)*scale_to_microns
    YM = np.asarray(document[document['Measurement'].str.contains('Y')]['Measured'].values)*scale_to_microns

    return XI, XM, YI, YM, DM




