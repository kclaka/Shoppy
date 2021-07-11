# Shopping List Web App

### WebApp URL : https://poetic-chariot-319022.uc.r.appspot.com

### About Project:
<div>
<p>I picked the Shopping App project over the Game project
because I saw it as an opportunity to explore building a serverless
project.</p>
<p>After I received the project details I spent some time to think
about the design and what technologies to use. I picked Flask
because I had a fair knowledge of python and I have done some little
projects with Flask previously. I also didn't want to deal with Javascript :laughing: </p>

<p>I opted for a serverless architecture so I could some experience building
a cloud app. I am glad I did because I learned (and failed :sob:) so much!</p>
</div>

Resources Used:<br>
<a href="https://cloud.google.com/appengine/docs/standard/python3/building-app">Building a Python 3 App on App Engine</a><br>
<a href="https://flask.palletsprojects.com/en/1.0.x/quickstart/#">Flask Quick Start</a><br>
<a href="https://cloud.google.com/datastore/docs/concepts/entities">Entities, Properties, and Keys</a>
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

### Teck Stack :hammer:
- FrontEnd
    - HTML/CSS
    - Bootstrap
    

- BackEnd
    - Flask
    - Google Cloud App Engine
    - FireStore
    - Google Cloud Data Store


### Web App Features :point_down:

- [x] User is able to add an item to the shopping list
- [x] User is able to view their whole shopping list
- [x] User is able to delete an individual item from the shopping list
- [x] User is able to delete their entire shopping list, with a single button click (without going and deleting each individual item one by one) 
- [x] Each is able to login with their Google account and their shopping list must persist between their logins
- [x] And so much more ... :blush: 


### Upcoming Features :hourglass_flowing_sand:
- [ ] Cache results in an encrypted cache results in an encrypted session store
- [ ] Improve design for better user experience
- [ ] Add more authentication methods
- [ ] Enable user to add shopping list without login but will have to login to save
- [ ] Automatic price look up for items in shopping list
- [ ] One Click button to purchase all items in shopping list from user favorite store
