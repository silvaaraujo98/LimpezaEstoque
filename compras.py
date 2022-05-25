# Importando as bibliotecas
from openpyxl import load_workbook


def transforma_base(path_completo):
    #Carregando as bases
    wb_compras = load_workbook("Compras2.xlsx")
    wb_base = load_workbook("Base.xlsx")

    #Setando as planilhas
    ws_compras = wb_compras['Sheet1']
    ws_base = wb_base['Plan1']

    #Reconhecendo a linha máxima do arquivo de compras
    linha_maxima = ws_compras.max_row
    i=5
    while i<= linha_maxima:
        Lista = []
        produto = ws_compras.cell(i,9).value
        codigo = ws_compras.cell(i,3).value
        if None not in [codigo,produto]:
            j=1
            fornecedor = ws_compras.cell(i+j,7).value
            while fornecedor != None:
                Lista = [produto,fornecedor]
                j+=1
                fornecedor = ws_compras.cell(i+j,7).value
        i+=1



