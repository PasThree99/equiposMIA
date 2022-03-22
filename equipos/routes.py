#from flask_wtf import form
from wtforms import form
from equipos import app
from flask import render_template,url_for,redirect
import random

from equipos.usefullAlgorithms import getDF




@app.route("/")
@app.route("/home")
def home_page():
    df = getDF()
    participantes = len(df["Carrera"])
    personas_por_equipo = 8
    numEquipos = int(participantes/personas_por_equipo)
    carreras = df["Carrera"].unique()

    dfs = []

    for i in carreras:
        dft = df[df["Carrera"] == i]
        dfs.append(dft)
        
    for i in range(len(dfs)):
        dfs[i] = dfs[i].reset_index()

    dfa = 0
    equipos =[[] for i in range(numEquipos)]


    print(participantes,len(df["Carrera"]))

    for i in range(participantes):
        
        rnd = random.randint(0,len(dfs[dfa])-1)
        equipos[i % numEquipos].append(dfs[dfa].iloc[rnd])
        
        nm = dfs[dfa].iloc[rnd]["Nombre"]
        bm = dfs[dfa]["Nombre"] != nm 

        dfs[dfa] = dfs[dfa][bm]

        if(len(dfs[dfa]["Nombre"])==0):
            dfa+=1
        # print(nm)
        # print(dfs[dfa]["Nombre"])
        # print(bm)

    


    return render_template('home.html',items = equipos)

