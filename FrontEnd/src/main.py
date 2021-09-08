from flask import Flask, render_template, redirect, url_for
import os
from flask import request
import json
import requests
app = Flask(__name__)

@app.route('/')
def index():
   """
    renvoie le template de base quand le route correspond a /
   """
   return render_template('base.html')

@app.route('/resume')
def resume():
    """
        renvoie le template de base quand le route correspond a /resume
    """
    resume =  requests.get('http://127.0.0.1:8000/resume')
    for row in resume : 
        print(row)
    return render_template('resume.html')

@app.route('/contact')
def contact():
    """
        renvoie le template de base quand le route correspond a /contact
    """
    return render_template('contact.html')

@app.route('/contact', methods=['POST'])
def text_box():
    """
        renvoie le template de base quand le route correspond a /contact
        avec des données d'une requete POST et les stock dans un fichier json
    """
    response = {}
    response['nom'] = request.form['nom']
    response['prenom'] = request.form['prenom']
    response['mail'] = request.form['mail']
    response['message'] = request.form['message']
    with open('messages.json', 'w') as f:
        json.dump(response, f, indent=4, ensure_ascii=False, sort_keys=False)
    return render_template('base.html')

@app.route('/projet')
def projet():
    """
        renvoie le template projet quand le route correspond a /projet
        et affiche tous les projets d'apres les données enregistrer dans le fichier json
    """
    return render_template('projet.html', projets=projet)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)