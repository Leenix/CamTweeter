#!/usr/bin.env python
__author__ = 'Leenix'

from pygame import camera, image
from twython import Twython
import logging
import datetime

logging.basicConfig(level=logging.INFO)


def sign_in_to_twitter():
    CONSUMER_KEY = '<Paste Consumer key (API Key) here>'
    CONSUMER_SECRET = '<Paste Consumer Secret (API Secret) here>'
    ACCESS_TOKEN = '<Paste Access Token here>'
    ACCESS_SECRET = '<Paste Access Token Secret here>'

    return Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

if __name__ == '__main__':
    # Initialise camera
    camera.init()
    camlist = camera.list_cameras()
    cam = camera.Camera(camlist[0])
    cam.start()

    # Get an image from the camera
    capture = cam.get_image()
    logging.info("Image captured")
    cam.stop()

    # Upload to Twitter
    now = datetime.datetime.now()
    time_string = now.strftime("%Y-%m-%d %T")
    image.save(capture, "/tmp/image.jpg")
    photo = open("/tmp/image.jpg", "rb")
    twitter = sign_in_to_twitter()
    twitter.update_status_with_media(status=time_string, media=photo)
