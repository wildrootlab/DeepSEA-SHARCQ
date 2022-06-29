from http.client import UnimplementedFileMode
from fastapi import FastAPI, UploadFile
from pydantic import BaseModel
from datetime import datetime
from typing import List
from magnum import Magnum
from .aws_util import AWSUtil


class PredictBody(BaseModel):
    user: str

    
app = FastAPI()



@app.post('/predict/')
async def predict(files: List[UploadFile], body: PredictBody):
    #create file path and awsUtil obj
    time = str(datetime.now())
    folder_path = f'{body.user}_{time}'
    aws_util = AWSUtil(folder_path)
    #upload to s3
    aws_util.s3_upload_files(files)
    #run application
    aws_util.launch_ai_ecs()
    aws_util.run_predict_ecs()
    #download results from ai
    results = aws_util.s3_download_results()
    return {'results': results}

# allows usage on aws lambda
handler = Magnum(app)