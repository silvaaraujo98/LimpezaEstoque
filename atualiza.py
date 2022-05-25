# Código que vai atualizar o arquivo de .xls para .xlsx
import win32com.client as win32
import os
cmd = os.getcwd()
def trans_x(filename):
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    wb = excel.Workbooks.Open(filename)
    wb.SaveAs(filename +"x", FileFormat = 51) 
    wb.Close()                               #FileFormat = 56 is for .xls extension
    os.remove(filename)
    excel.Application.Quit()