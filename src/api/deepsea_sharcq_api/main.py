from http.client import UnimplementedFileMode
from fastapi import FastAPI, UploadFile
from pydantic import BaseModel
from datetime import datetime
from typing import List


from api.deepsea_sharcq_api.aws_util import AWSUtil
class PredictBody(BaseModel):
    user: str

    
app = FastAPI()



@app.post('/predict/')
async def predict(file: List[UploadFile], body: PredictBody):
    aws_util = AWSUtil()
    #upload to s3
    time = str(datetime.now())
    file_path = f'{body.user}_{time}.jpg'
    aws_util.s3_upload_files(file, file_path)
    aws_util.launch_ecs()
    aws_util.run_main_ecs()
    results = aws_util.s3_download_results(file_path)
    return {'results': results}
