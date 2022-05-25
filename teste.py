from tarfile import PAX_FIELDS
import openpyxl as px
from atualiza import trans_x
from limpa_linha import limpa_linha
from compras import transforma_base
import os

transforma_base(os.getcwd() + r"\Compras3.xlsx")