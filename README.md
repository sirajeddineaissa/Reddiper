
# Reddiper

Reddiper is an app that scrapes content from reddit (for the moment, only images).

## User Credentials Setup

1- Go to [App Preferences](https://www.reddit.com/prefs/apps)

2- Setup a script-type app

3- Collect the Client ID, Client Secret, User Agent, Username and Password

4- Create a ``.env`` file in the root directory with the following structure :

```
$CLIENT_ID = <Your client ID>
$CLIENT_SECRET = <Your client secret>
$USER_AGENT = <it could be anything>
$USERNAME =  <Your Reddit useranme>
$PASSWORD = <Your Reddit password>
```
**Note : If you have entered wrong credentials and run the script, make sure you delete the generated ``token.pickle`` file after you fix your ``.env`` data.**


## Installation

### Linux

```bash
pip3 install virtualenv
git clone https://github.com/Dismalness/Reddiper.git
cd Reddiper
virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
```

### Windows

```bash
pip3 install virtualenv
git clone https://github.com/Dismalness/Reddiper.git
cd Reddiper
virtualenv env
env/Scripts/activate
pip3 install -r requirements.txt
```

## Usage

1- Run the script with 
```python
python3 UI.py
```
to launch to the following window :
<p align="center">
  <img src="https://i.imgur.com/L1h4Uqr.png">
</p>

2- Insert the name of the subreddits you want to scrape (some subreddits may present errors due to invalid names or error comparing images with the OpenCV library).

3- Insert the maximum number of images to scrape from that subreddit

4- Insert the submissions' category (controversial, hot, new, top, gilded, rising)

3- Click on "Scrape Now"

## Tools

* Python
* OpenCV
* PRAW (The Python Reddit API Wrapper)
* PySimpleGUI



## Troubleshooting

If you're having trouble managing your packages in a python virtual environement with VS Code. Make sure you've set the right python interpreter :

1- ```CTRL+SHIFT+P```

2- Python: Select Python Interpreter

3- Select the one with the following path : ```./{name of your virtualenv}/bin/python```

## License
[MIT](https://choosealicense.com/licenses/mit/)