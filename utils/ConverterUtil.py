
import pandas as pd


class ConverterUtil(object):

    def convert_matrix_collumn_to_list(self, file, collumn):
        df = pd.DataFrame(file, columns=[collumn]).values
        newList = list()
        for value in df:
            newList.append(value[0])
        return newList

    def convert_matrix_to_dict(self, file):
        adjacency_list = dict()
        keys = (list(file.iloc[:, 0]))
        for key in keys:
            connection = self.convert_matrix_collumn_to_list(file, key)

            adjacency_list[key] = connection
        return adjacency_list
