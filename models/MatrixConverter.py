
import pandas as pd

class MatrixConverter(object):
    
    def __init__(self,file):
        self.file = file
    
    def convert_collumn_to_list(self, collumn):
        df = pd.DataFrame(self.file,columns=[collumn]).values
        newList = list()
        for value in df:
            newList.append(value[0])
        return newList

    def convert_matrix_to_dict(self,collumn):
        adjacency_list = dict()
        for item in sorted(self.convert_collumn_to_list(collumn)):
            connection = self.convert_collumn_to_list(item)
            print(item  + ': ' + str(connection))
            adjacency_list[item] = connection
        return adjacency_list
    
    def set_file(self,file):
        self.file = file