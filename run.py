import praw 
import requests
import cv2
import numpy as np
import os
import pickle

#Amount of posts to scrape
quantity = 20

def create_token():
    creds = {}
    creds["client_id"] = input("Client_id: ")
    creds["client_secret"] = input("client_secret: ")
    creds["user_agent"] = input("user_agent: ")
    creds["username"] = input("username: ")
    creds["password"] = input("password: ")
    return creds

def create_folder(image_path):
    CHECK_FOLDER = os.path.isdir(image_path)
    if not CHECK_FOLDER:
        os.makedirs(image_path)

bypass = os.path.join(os.path.dirname(os.path.realpath(__file__)), "bypass/")
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images/")
create_folder(image_path)
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
else:
    creds = create_token()
    pickle_out = open("token.pickle","wb")
    pickle.dump(creds, pickle_out)

reddit = praw.Reddit(client_id=creds['client_id'],
                    client_secret=creds['client_secret'],
                    user_agent=creds['user_agent'],
                    username=creds['username'],
                    password=creds['password'])


list = open("subs.csv", "r")
for item in list:
    sub = item.strip()
    subreddit = reddit.subreddit(sub)
    subimage_path = os.path.join(image_path, f"{sub}")
    create_folder(subimage_path)
    print(f"Scraping from {sub}!")
    for submission in subreddit.new(limit=quantity):
        if "jpg" in submission.url.lower() or "png" in submission.url.lower():
            try:
                resp = requests.get(submission.url.lower(), stream=True).raw
                image = cv2.imdecode(np.asarray(bytearray(resp.read()), dtype="uint8"), cv2.IMREAD_COLOR)
                compare_image = cv2.resize(image,(224,224))
                for (dirpath, dirnames, filenames) in os.walk(bypass):
                    bypass_path = [os.path.join(dirpath, file) for file in filenames]
                ignored = False

                for ignore in bypass_path:
                    diff = cv2.subtract(cv2.imread(ignore), compare_image)
                    b, g, r = cv2.split(diff)
                    res = cv2.countNonZero(b) + cv2.countNonZero(g) + cv2.countNonZero(r)
                    if res == 0:
                        ignored = True

                if not ignored:
                    cv2.imwrite(os.path.join(subimage_path , f"{submission.id}.png"), image)

            except Exception as e:
                print(f"Error!! {submission.url.lower()}")
                print(e)
        

