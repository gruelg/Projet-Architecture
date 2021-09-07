from fastapi import FastAPI

app = FastAPI()

@app.get("/profil")
def read_root():
    return {""}

