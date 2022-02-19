import pandas as pd

file = pd.read_excel("./matriz_adj_uf_brasil.xlsx")
print(file);
print (pd.DataFrame(file,columns=['0']))