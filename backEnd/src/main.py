from fastapi import FastAPI
from sqlalchemy import *
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
import json

config = {
    'host': '127.0.0.1',
    'port': '3306',
    'user': 'api',
    'password':'my-secret-pw',
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
metadata = MetaData()
metadata.reflect(engine)
Base = automap_base(metadata=metadata)
Base.prepare()
##
resume= Base.classes.resume
##session
Session = sessionmaker(bind = engine)
session = Session()

app = FastAPI()

@app.get("/resume")
def read_root():
    result = session.query(resume).all()
    print(result)
    retour = ""
    for i in range(len(result)):
        retour += json.dumps({ i : { "prenom" : result[i].prenom, "nom" : result[i].nom, "email" : result[i].email, "date_naissance" : result[i].date_naissance , "pays" :  result[i].pays, "ville" : result[i].ville, "code_postal" : result[i]. code_postal }})
    print(retour)
    return retour

@app.get("/experience")
def read_root():
    result = session.query(resume).all()
    print(result)
    retour = ""
   
    return retour