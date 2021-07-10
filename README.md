# Shopping List Web App

### WebApp URL : https://poetic-chariot-319022.uc.r.appspot.com/

### Design :

![image](https://storage.googleapis.com/gweb-cloudblog-publish/images/firebase-aunthentication0s8a.max-700x700.PNG)
<br><b>Image Credits - <a href= "https://cloud.google.com/blog/products/gcp/how-to-authenticate-users-on-google-app-engine-using-firebase">Google Cloud</a></b>


### Install Locally
- Clone this repo to your local machine
```
git clone https://github.com/Project-Assignments/Project-F.git
```

- Set up a new python virtual environment
    - cd into new folder
```
python3 -m venv env
source env/bin/activate
```

- cd into project folder, install required packages and run the application

```
pip install  -r requirements.txt
python main.py
```

### Deploy to Cloud
- cd into root project folder
```
gcloud app deploy
```

Visit your new project url:
```
gcloud app browse
```