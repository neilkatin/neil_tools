

# spreadsheet tools: common methods to deal with spreadsheet data

import logging
import datetime

log = logging.getLogger(__name__)


ROW_INDEX = '__ROW_INDEX__'
def matrix_to_object_array(matrix):
    """ convert an list of lists (raw spreadsheet data)  to a list of dicts.

        One dict per for in the original matrix.
        First matrix row is assumed to be column headers, and will be the dict keys.
    """

    result = []

    # iterate through the rows
    for index, row in enumerate(matrix):
        if index == 0:
            title_row = row
            columns = title_to_dict(title_row)
        else:
            row_dict = {}
            for name, column_num in columns.items():
                row_dict[name] = row[column_num]

            row_dict[ROW_INDEX] = index
            #log.debug(f"new row_dict: { row_dict }")
            result.append(row_dict)

    return result



def title_to_dict(title_row):
    """ take a title row and return a dict that maps names to column numbers

        throw an error on duplicate values
    """

    result = {}
    for index, value in enumerate(title_row):
        if value in result:
            #log.debug(f"title_row { title_row }")
            raise Exception(f"title_to_dict: duplicate value '{ value }' in passed title row (new index { index }, orig index { result[value] }")

        result[value] = index

    return result


# turn an excel date (days since 1900) into a python datetime
ordinal_1900_01_01 = datetime.datetime(1900, 1, 1).toordinal()
def excel_to_dt(days_since_1900):
    dt = datetime.datetime.fromordinal(ordinal_1900_01_01 + int(days_since_1900) -2)

    return dt

