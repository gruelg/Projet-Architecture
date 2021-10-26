from typing import List, Dict
from flask import Flask
import json
from sqlalchemy import create_engine, MetaData, Table, Column, Float, Integer, String, ForeignKey
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.dialects.mysql import DATETIME
import logging
import pymysql
from sqlalchemy.orm import sessionmaker
from datetime import date

app = Flask(__name__)

config = {
    'host': 'db',
    'port': '3306',
    'user': 'newuser',
    'password':'newpassword',
    'database':'Curiculum'
}
db_user = config.get('user')
db_pwd =config.get('password') 
db_host = config.get('host')
db_port = config.get('port')  
db_name = config.get('database')

connexion_str = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'
engine = create_engine(connexion_str, pool_recycle=3600)
connexion = engine.connect()
#metadata
metadata = MetaData(bind=engine)
metadata.reflect(engine)
Base = automap_base(metadata=metadata)
Base.prepare()
##
resume= Base.classes.resume
##session
Session = sessionmaker(bind = engine)
session = Session()

@app.route('/resume')
def fetch_payments() :
    result = session.query(resume).all()
    print(result)
    retour = ""
    for i in range(len(result)):
        retour += json.dumps({ i : { "prenom" : result[i].prenom, "nom" : result[i].nom, "email" : result[i].email, "date_naissance" : result[i].date_naissance , "pays" :  result[i].pays, "ville" : result[i].ville, "code_postal" : result[i]. code_postal }})
    print(retour)
    return retour
"""
    TODO : 
    recuperer les données enovyé du front pour les sav dans la base de données 

"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)