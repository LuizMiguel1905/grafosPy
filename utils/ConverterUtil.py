
from asyncio.windows_events import NULL
from numpy import Infinity
import pandas as pd


class ConverterUtil(object):

    def convertMatrixCollumnToList(self, file, collumn):
        df = pd.DataFrame(file, columns=[collumn]).values
        newList = list()
        for value in df:
            newList.append(value[0])
        return newList

    def convertMatrixToDict(self, matrix):
        adjacency_list = dict()
        keys = (list(matrix.iloc[:, 0]))
        for key in keys:
            connection = self.convertMatrixCollumnToList(matrix, key)
            adjacency_list[key] = connection
        return adjacency_list
