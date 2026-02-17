# Election-Data

## Workflows

1. Update config.yaml
2. update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src Config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml

# How to run?
### Steps:

Clone the repository

```bash
https://github.com/Rupesh4113/Election-Data
```
### Step 01 - Create a conda environment after opening the repository
```
Conda create -n cnncls python=3.11 -y
```

```bash
conda activate cnncls
```

# Step 02: install the requirements

```bash
pip install -r requirements.txt
```

```bash
#finally run the following command
python app.py
```
now,
```bash
open up your local host and port
```

### DVC cmd
1. dvc init
2. dvc repo
3. dvc dag


# AWS-CICD-Deployment-with-Github-actions

## 1. Login to AWS console

## 2. Create IAM user for deployment

    #with specific access

    1. EC2 access : It is virtual machine

    2. ECR: Elastic Container registry to save your docker image in aws

    #Description: About the deployment
    1. Build docker image of the source code

    2. Push your docker image to ECR

    3. Launch your EC2

    4. Pull your image from ECR in EC2

    5. Launch your docker image in EC2

    #Policy:

    1. AmazonEC2ContainerRegistryFullAccess

    2. AmazonEC2FullAccess

 ## 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken

## 4. Create EC2 Machine (Ubuntu)

## 5. Open EC2 and install docker in EC2 machine:

    #Optional

    sudo apt-get update -y

    sudo apt-get upgrade

    #required

    curl -fsSL https://get.docker.com -o get-docker.sh

    sudo sh get-docker.sh

    sudo usermod -aG docker ubuntu

    newgrp docker

# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one

# 7. Setup github secrets:

    AWS_ACCES_KEY_ID=

    AWS-SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>> 566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app

# AZURE-CICD-Deployment with Github Actions

## Save Pass:

s3cEZKH5yytiVnJ3h+eI3qhhzf9q1vNwEi6+q+WGdd+ACRCZ7JD6

## run from terminal:

docker build -t electiondataapp.azurecr.io/election:latest .

docker login electiondataapp.azurecr.io

docker push electiondataapp.azurecr.io/election:latest

## Deployment Steps:

1. Build the Docker image of the source code
2. Push the docker image to container registry
3. launch the Web App Server in Azure
4. Pull the Docker image from the container registry to web app server and run