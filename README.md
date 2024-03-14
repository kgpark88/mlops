# MLOps

### MLflow 설치
sudo apt update 
sudo add-apt-repository ppa:deadsnakes/ppa 
sudo apt install python3.11 -y 
python3.11 --version 

# sudo apt install python3-pip 
sudo pip3 install pipenv virtualenv

mkdir mlflow
cd mlflow
pipenv --python 3.11

pipenv shell 
pipenv install mlflow awscli boto3 setuptools![image](https://github.com/kgpark88/mlops/assets/17672596/53de2ee1-5de6-466d-a882-d98cc543e985)

