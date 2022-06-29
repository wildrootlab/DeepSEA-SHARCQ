from fastapi import UploadFile
from typing import List
import boto3
import os
from joblib import Parallel, delayed

class AWSUtil:
    def __init__(self, folder_path: str):
        self.folder_path = folder_path
        self.s3 = boto3.resource('s3')
        self.bucket_name = os.get_environ('S3_BUCKET')
        self.s3_bucket = self.s3.Bucket(self.bucket_name)

    def s3_upload_files(self, files: List[UploadFile]):
        # action to take in parallel 
        def _upload_file(file):
            with open(file.file) as f:
                key = f'/uploads/{self.folder_path}/{file.filename}'
                # below should implement parallel multipart upload in theory
                self.s3_bucket.upload_fileobj(f,key)
        # runs file uploads in parallel across all cpus - TODO hopefully it doesn't overtax the RAM (10 GB max on lambda instances)
        Parallel(n_jobs=-1)(delayed(_upload_file)(file) for file in files)
            
    def launch_ai_ecs(self):
        raise NotImplementedError
    def run_predict_ecs(self):
        raise NotImplementedError
    def s3_download_results(self):
        raise NotImplementedError