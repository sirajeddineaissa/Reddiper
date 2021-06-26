#!/usr/bin/env python3
import praw
import requests
import cv2
import numpy as np
import os
import pickle

#Reddit credentials
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

def main():
    #Maximum amount of posts to scrape
    max_quantity = 5
    #Path to error images
    bypass = os.path.join(os.path.dirname(
        os.path.realpath(__file__)), "bypass/")
    #Path to ./images
    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images/")
    create_folder(image_path)
    #Load the token with pickle from the generated file token.pickle if it already exists
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    #Else enter your reddit credentials to generate token.pickle
    else:
        creds = create_token()
        pickle_out = open("token.pickle", "wb")
        pickle.dump(creds, pickle_out)
    #Reddit credentials via reddit.com/prefs/apps
    reddit = praw.Reddit(client_id=creds['client_id'],
                         client_secret=creds['client_secret'],
                         user_agent=creds['user_agent'],
                         username=creds['username'],
                         password=creds['password'])

    list = open("subs.csv", "r")
    for item in list:
        sub = item.strip()
        subreddit = reddit.subreddit(sub)
        #Path to the subreddit folder in ./images
        subimage_path = os.path.join(image_path, f"{sub}")
        create_folder(subimage_path)
        print(f"Scraping from {sub}!")
        for submission in subreddit.new(limit=max_quantity):
            #Fetch jpg and png files only
            if "jpg" in submission.url.lower() or "png" in submission.url.lower():
                try:
                    #Submission get request
                    resp = requests.get(submission.url.lower(), stream=True).raw

                    #Read data from the bytearray and convert it into image data
                    image = cv2.imdecode(np.asarray(bytearray(resp.read()), dtype="uint8"), cv2.IMREAD_COLOR)

                    #Make a resized copy of the image to test whether it's invalid or not since the dimensions of the invalid images are 224X224 px. Otherwhise we wouldn't be able to substract the pixel values of both later
                    compare_image = cv2.resize(image, (224, 224))

                    for (dirpath, dirnames, filenames) in os.walk(bypass):
                        #Generate a list for the invalid images' paths
                        bypass_path = [os.path.join(dirpath, file) for file in filenames]
                    ignored = False
                    for ignore in bypass_path:
                        diff = cv2.subtract(cv2.imread(ignore), compare_image)
                        #Seperate the BGR channels
                        b, g, r = cv2.split(diff)
                        #Sum of the number of non-zero pixels in each channel
                        res = cv2.countNonZero(b) + cv2.countNonZero(g) + cv2.countNonZero(r)
                        #If it's equal to 0 then we're sure that our compare_image is invalid
                        if res == 0:
                            ignored = True

                    #Write the non-invalid images into ./images
                    if not ignored:
                        cv2.imwrite(os.path.join(subimage_path,f"{submission.id}.png"), image)

                except Exception as e:
                    print(f"Error!! {submission.url.lower()}")
                    print(e)


if __name__ == "__main__":
    main()
