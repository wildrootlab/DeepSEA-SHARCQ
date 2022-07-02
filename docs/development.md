## Dev notes:
- average file size is 40 mb
- example number of files to be processed is TBD
- file type is .tif
## docker usage:
TODO this is not working yet since environment variables need to be handled. and `YOUR_ENV=production/development` needs to be added.
to run ai service, use `docker build . --file=Dockerfile_ai --tag ai_app`
to predict use: `docker run ai_app AI_ACTION=predict PATH={TODO path to files you want to predict for}`
to train: `docker run ai_app AI_ACTION=train PATH={TODO path to files you want to train with}`
to run fast api service in Docker, use `docker build . -t api --file Dockerfile_api` from repo/src/api folder
then, `docker run ai_api`
## DevOps plan: TODO

### general
- set up terraform code for all of this. 
- set up testing  for infrastructure and end to end. 
- set up cicd actions for continuous testing and deployment on push to main. 
- maybe add fault tolerance in ai pipeline
- maybe add in manual labelling tooling to pipeline for continuous improvement. 
- add in authorization and other factors to prevent dos attacks or people spamming the api server. 

### predict
- turn api and ai code into containerized endpoints
- aws api gateway as initial point of contact
- passes event to aws lambda with fast api container uploads files to s3 and calls ai as descirbed below
- calls ecs containers for files - batches files among containers/ parrallelizes on single container/ runs on ec2 -- TODO decide/make options - need more info on use case and memory/cpu usage.
- container uploads partial results to s3 bucket/other storage. 
container uploads final prediction results to s3 bucket.
- return prediction results to end user.
- TODO - figure out way to handle if prediction time takes too long for lambda function ie more than 10 minutes. Maybe have api gateway call a lambda function to spin up ec2 instance/ecs cluster for the actual fastapi running. return data by notifying the user could be a case of emailing with yagmail with the signed link to download files. 

### train
- containerize train code. single machine cpu parrallelization is fine for the algorithms. 
- TODO; need a better idea of what train logic looks like. 