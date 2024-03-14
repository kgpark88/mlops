# MLOps MVP

### MLOps 설치 : Ubuntu
sudo apt update   
sudo add-apt-repository ppa:deadsnakes/ppa    
sudo apt install python3.11 -y   
python3.11 --version   
  
sudo apt install python3-pip   
sudo pip3 install pipenv virtualenv  
  
mkdir mlflow  
cd mlflow  
pipenv --python 3.11  
  
pipenv shell   
pipenv install mlflow awscli boto3 setuptools  

