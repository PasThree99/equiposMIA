from flask import url_for,request
from pandas import read_excel

df = read_excel("equipos/static/Inscripción Hackathon MIA UAO 22(1-93).xlsx",sheet_name="Hoja2")
def getDF():
    global df
    df = df[["Nombre","Carrera"]]
    return df
    l = []
    for i in df:
        l.append(i[0])
        l.append(i[1])
        print(i[0],i[1])

    return l