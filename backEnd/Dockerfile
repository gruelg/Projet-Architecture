FROM python:3.6-slim
EXPOSE 8000
RUN apt update && apt install -y netcat
WORKDIR /src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/ .
ENTRYPOINT ["./entrypoint.sh"]
# commande a executer au lancement du container 
CMD ["python","./main.py"]
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]