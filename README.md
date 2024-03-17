

# MLOps MVP

## 팀즈 링크
https://teams.microsoft.com/l/meetup-join/19%3ameeting_YjU3OWU2YzktNjI0Yi00M2U5LTkyM2EtMDQzYWYwMzI4ZTc0%40thread.v2/0?context=%7b%22Tid%22%3a%22e6c9ec09-8430-4a99-bf15-242bc089b409%22%2c%22Oid%22%3a%2238ca6ef9-682c-43cb-9772-17977dacdda6%22%7d

 
## MLOps 설치 : Ubuntu
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

