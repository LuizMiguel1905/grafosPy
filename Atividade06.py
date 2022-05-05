import pandas as pd

from models.grafo import Graph
from utils.PathUtil import PathUtil

from utils.ConverterUtil import ConverterUtil
from utils.ValidadorUtil import ValidadorUtil
from utils.PathUtil import PathUtil

grafo1 = pd.read_excel("docs/grafos/Grafos.xlsx", sheet_name='Grafo 8')
grafo2 = pd.read_excel("docs/grafos/Grafos.xlsx", sheet_name='Grafo 9')

converterUtil = ConverterUtil()
validadorUtil = ValidadorUtil()
pathUtil = PathUtil()

