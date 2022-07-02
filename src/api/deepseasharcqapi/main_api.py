from fastapi import FastAPI, UploadFile
from pydantic import BaseModel
from datetime import datetime
from typing import List
from magnum import Magnum
from .aws_util import AWSUtil


class PredictBody(BaseModel):
    user: str
    email: str

    
app = FastAPI()



@app.post('/predict/')
async def predict(files: List[UploadFile], body: PredictBody):
    #create folder path and awsUtil obj
    time = str(datetime.now())
    folder_path = f'{body.user}_{time}'
    aws_util = AWSUtil(folder_path)
    #upload to s3 - TODO might need more parallelization or memory management ie in parts for upload - might need some errror handling for uploads greater than ~7 GB (~175 files) (10 gb max on lambda)
    aws_util.s3_upload_files(files)
    #run ai application and close it when done
    aws_util.exec_predict_ecs()

    return {'results': 'we will email you with a signed url to the  predictions at the email you provided. You can download the result files with this.'} # maybe they need to do a get request at this fast api server when they have the url. TODO

# allows usage on aws lambda
handler = Magnum(app)