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

### Web App Features :point_down:

- [x] User is able to add an item to the shopping list
- [x] User is able to view their whole shopping list
- [x] User is able to delete an individual item from the shopping list
- [x] User is able to delete their entire shopping list, with a single button click (without going and deleting each individual item one by one) 
- [x] Each is able to login with their Google account and their shopping list must persist between their logins
- [x] And so much more ... :blush: 


### Upcoming Features :hourglass_flowing_sand:
- [ ] Improve design for better user experience
- [ ] Add more authentication methods
- [ ] Enable user to add shopping list without login but will have to login to save
- [ ] Automatic price look up for items in shopping list
- [ ] One Click button to purchase all items in shopping list from user favorite store
