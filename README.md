
# Reddiper

Reddiper is an app that scrapes content from reddit ( for the moment, only images).

## Installation

### Linux

```bash
pip3 install virtualenv
git clone https://github.com/Dismalness/Reddiper.git
cd Reddiper
virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
python3 UI.py
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
  <img src="https://i.imgur.com/aFNRX5y.png">
</p>

2- Enter the name of the subreddits you want to scrape (some subreddits may present errors due to invalid names or error comparing images with the OpenCV library).
3- Click on "Scrape Now"

## Tools

-Python
-OpenCV
-PRAW (The Python Reddit API Wrapper)

## License
[MIT](https://choosealicense.com/licenses/mit/)