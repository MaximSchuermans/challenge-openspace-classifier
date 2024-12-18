from typing import List
from pandas import read_excel


def read_xls(filename: str) -> List[str]:
    """
    Reads the excel file into a pandas dataframe and returns a list of names.

    :param filename: A str containing the name of the file to be read
    """
    names = []
    excel = read_excel(filename)
    for row in excel.itertuples():
        names.append(row[1])  # Append the name to the names list
    return names
