from http.client import UnimplementedFileMode
from fastapi import FastAPI
from pydantic import BaseModel

class PredictBody:
    user: str
    
app = FastAPI()



@app.post('/predict/')
async def predict():
    raise NotImplementedError
