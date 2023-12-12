# Detection Phishing Messages Application

### Installing and Running

#### 1. Clone repository
`git clone `

#### 2. ML model
Put your trained model to `ml_models`. \
Add path to your model to `utils.py`. 

#### Open Docker on your machine

#### Open terminal
cd phishing-detection-app

#### Build Docker image
docker build -t phish_detect_app .

#### Run image
docker run -p 8080:8080 phishing_detect_app
