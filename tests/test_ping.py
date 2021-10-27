import urllib.request as urllib2
from sqlalchemy import create_engine

def test_backend():
    """
        Test sur le fonctionnement du frontend
    """
    assert 200 == urllib2.urlopen('http://localhost:8000/resume').getcode()

def test_frontend():
    """
        Test sur le fonctionnement du frontend
    """
    assert 200 == urllib2.urlopen('http://localhost:5000/resume').getcode()

def test_bdd(): 
    """
        Test sur le fonctionnement de la bdd
    """
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
    assert engine

def test_echec(): 
    assert 200 == urllib2.urlopen('http://localhost:8000/echec').getcode()




    

