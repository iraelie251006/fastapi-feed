from fastapi import FastAPI

app = FastAPI()

@app.get("/goal")
def greeting():
    return {
        "name": "Elie",
        "goal": "I'm coming for you all"
    }

@app.get("/")
def greeting():
    return {
        "name": "Elie",
    }
