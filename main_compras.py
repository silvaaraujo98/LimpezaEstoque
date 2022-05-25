from limpa_linha import limpa_linha
from compras import transforma_base
from atualiza import trans_x
import os
import shutil

path_1 = os.getcwd()+r'\Não Processado'
path_2 = os.getcwd()+r'\Pre Processado'
path_3 = os.getcwd()+r'\Processado'

for i in os.listdir(path_1):
    trans_x(path_1 + r"/" + i)
    shutil.move(path_1 +r"/" + i + "x",path_2 +r"/" + i)


for i in os.listdir(path_2):
    transforma_base(path_2 +r"/" + i)
    shutil.move(path_2 +r"/" + i,path_3 +r"/" + i)

