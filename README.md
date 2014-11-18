block-twitter-jerks
===================

Block Twitter jerks, their jerk followers, and jerks they follow. 

### Purpose
Twitter is home to a lot of jerks. 

Twitter's recent timeline tweaks means that tweets from people you would never follow in a million years end up in your timeline. 9 times out of 10 it's some opinionated jerk, and who wants jerks sullying their timeline?

This script gives people with no strong opinions or beliefs a more pleasant Twitter experience. Enjoy!

### How it works
The script iterates through a list of jerks, looks at the jerks they follow, and the jerks that follow them then blocks everyone. By default it uses a list of a few well-known Australian Twitter jerks, but you can customise it however you want.

### Installation

If you don't have tweepy, install the dependency.

`pip install tweepy`

Then run it

`python blockjerks.py`

##### Notes
* Script will not block people you are following or people who are following you.
* Due to Twitter's rate limiting this script will pause for 60 seconds after each batch of jerks is blocked.
* Once the script finishes running, a list of jerks is saved as a CSV file for your records if you ever wish to unblock a jerk.

##### Disclaimer

I take no responsibility for any blowback that stems from your jerk-blocking activities.
