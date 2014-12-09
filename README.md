CamTweeter
==========

Automated webcam snapshots to Twitter (Raspberry Pi)

The CamTweeter script does what is says on the box. When the script runs,a snapshot is pulled from the first detected webcam and the image is published to Twitter with the current timestamp. The original application for the script is to monitor 3D printer progress.

Installing the Pre-requisites
=============================

The CamTweeter script uses the pygame library to capture webcam photos, and the Twython library to interface with a Twiter app account.

In a bash terminal, enter:

	sudo apt-get install python-pip python-pygame cron
	pip install twython


Set up Twitter details
======================

This section of the guide is based off of the Twython 'Getting Started' guide, which can be found at:
https://twython.readthedocs.org/en/latest/usage/starting_out.html#starting-out

1) Create a Twitter Account (if you haven't already)
	https://support.twitter.com/articles/100990-signing-up-with-twitter

2) Add mobile access to your account. This is an important step. The script will not be able to publish anything on your feed without mobile access.
	https://support.twitter.com/articles/110250-adding-your-mobile-number-to-your-account

3) Register an application your account. You'll need to be signed in with your Twitter account.
	https://dev.twitter.com/apps

4) Grab your keys. From your Twitter apps page (https://apps.twitter.com/), click on your newlycreated app to open up its dashboard. Open the 'Keys and Access Tokens' tab. Under 'Application Settings', you'll see your Consumer Key, and Consumer Secret Key. They should just look like long and random strings of text. 

5) Copy both of these strings into the CamTweeter script where it says "Paste x here". Make sure they're surrounded by 'single quotes' 

6) Give your app read and write access by clicking "modify app permissions" in Application Settings where it says 'Access Level'

7) Generate your access token in the Application Settings tab by clicking the "Create my access token" button at the bottom of the tab.

8) After your token has been generated, you'll be able to see your access token and access secret token. Copy these two strings into the CamTweeter script.

9) The Twitter setup should be finished and ready to go. Try running the script	by navigating to the script location in console and typing:

		python CamTweeter.py

If everything works, a webcam snapshot will be published to your Twitter feed.


Set up Cron
===========

Cron is a basic scheduling tool that can be used to set up timed events. A Cron Table is checked every minute to determine which scripts need to be run.

1) In a bash terminal, type:

	crontab -e

This will open up an editing window for the Cron Table, which is the scheduling	script. The script will be blank if Cron has not be used before.

2) At the end of the script (after the # lines), type the following:

	* * * * * /usr/bin/python <location of CamTweeter script>

   This script will run every minute. Other time frames can be spcified by following this guide:
		http://www.thegeekstuff.com/2011/07/cron-every-5-minutes/

3) Hit 'Ctrl+X' to close the Cron Table. Don't forget to save. Cron scripts become active as soon as the table has been saved.


Enable/Disable
==============

To disable the periodic triggering of the CamTweeter script, type the following into a bash terminal:

	crontab -e

This will open the active Cron Table. Place a '#' at the start of the CamTweeter line to disable the call. Similarly, remove the '#' to enable the script again.
