import random 
from equipos.usefullAlgorithms import getDF
def createTeams(n_integrantes):
    df = getDF()
    for i in range(len(df["Nombre"])):
        nr = random.randint(0,len(df["Nombre"]))
        
    return df



