from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def allData():
    return {"name":"dev"}

@app.post("/")
def addUser(name:str):
    return name
