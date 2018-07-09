# This Python file uses the following encoding: utf-8
import os
import sys
import datetime
import time
from datetime import date  
hj = date.today()

def removerRelatoriosAntigos():
    path = "c:/reports"
    dir = os.listdir(path)
    i = 0
    for file in dir:
        if file.endswith(".pdf" or ".xls"  or ".xlsx"):
            dt = datetime.datetime.fromtimestamp(os.path.getmtime(file))
            if dt.toordinal() < hj.toordinal():
                print "Arquivo removido: ",file
                print "Data de criacao: ",dt
                i=i+1
                #os.remove(file)
    print i,"Arquivo(s) removido(s)."   

removerRelatoriosAntigos()   


