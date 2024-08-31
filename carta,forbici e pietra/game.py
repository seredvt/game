from flask import Flask, render_template, request, url_for, flash, redirect, session, make_response, jsonify,abort
from waitress import serve
from flask_session import Session

import os

import random

import threading
import time

app=Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(64)
#debug
app.config["DEBUG"] = True
#gestioni delle sessioni/coockies
app.config['SESSION_TYPE']='filesystem'
app.config['SESSION_PERMANENT']=True
app.config['PERMANENT_SESSION_LIFETIME']=2678400

list_name=[]




@app.route("/game",methods=("GET","POST"))
def game():

    global list_name

    position=None
    name='NickName'

    position1='display:block;'
    position2='display:none;'

    bottone=None
    both=None
    risult=None


    list_img=['./static/img/carta.png',"./static/img/forbici.png","./static/img/sasso.png"]


    if request.method=="POST":
    
        name=request.form.get('name')

        bottone=request.form.get('selected_image')
       
        if name:
            position='visibility:hidden;'
            list_name.append(name)

        if bottone:
            
            name=list_name[0]
            position1='display:none;'
            position2='display:block;'
            

            both=random.choice(list_img)
            

            if bottone != both:
                if bottone == './static/img/carta.png' and both == "./static/img/forbici.png":
                    risult='GAME OVER'

                elif both == './static/img/carta.png' and bottone == "./static/img/forbici.png":
                     risult='WIN'
                
                elif bottone == './static/img/carta.png' and both == "./static/img/sasso.png":
                     risult='WIN'

                elif both == './static/img/carta.png' and bottone == "./static/img/sasso.png":
                     risult='GAME OVER'

                elif bottone == "./static/img/forbici.png" and both == "./static/img/sasso.png":
                     risult='GAME OVER'

                elif both == "./static/img/forbici.png" and bottone == "./static/img/sasso.png":
                     risult='WIN'

            else:
                risult='PARITY'

    return render_template('game.html',position=position, position1=position1,position2=position2,name=name,bottone=bottone,both=both,risult=risult)

if __name__=="__main__":
    #WSGI server .. localhost:8080
    serve(app,host='0.0.0.0',port=8080,threads=100)