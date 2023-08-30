from fastapi import FastAPI
import cv2
from flama import Flama

app = FastAPI()

flama = Flama()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/flama")
def getFlama(numFrames):
    return flama.readFlama(numFrames)



