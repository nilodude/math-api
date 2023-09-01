from fastapi import FastAPI
from flama import Flama
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)
flama = Flama()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/flama")
def getFlama(numFrames: int):
    res=flama.readFlama(numFrames)
    return res

@app.get("/numFrames")
def getNumFrames():
    return 30



