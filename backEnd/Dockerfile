FROM python:3.8

WORKDIR /src

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/ .

# commande a executer au lancement du container 
#CMD [ "uvicorn", "main:app" ] 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]