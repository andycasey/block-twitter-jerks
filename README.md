block-twitter-jerks
===================

Block Twitter jerks, their jerk followers, and jerks they follow. 

### Purpose
Twitter is home to a lot of jerks. 

Twitter's recent timeline tweaks means that tweets from people you would never follow in a million years end up in your timeline. 9 times out of 10 it's some jerk who seeks to impose their world view on the rest of us, or is generally just a massive jerk to other people. 

And who wants jerks sullying their timeline?

### How it works
The script iterates through a list of user-defined jerks. It then looks at the jerks who they follow, and the jerks that follow them. It then looks to see if you are following/followed by any of these jerks. If not, then it those jerks are blocked.

#### Notes
* Due to Twitter's rate limiting this script will pause for 60 seconds after each batch of jerks is blocked.
* Once the script finishes running, a list of jerks is saved as a CSV file for your records if you ever wish to unblock a jerk.

### Installation

If you don't have tweepy, install the dependency.

`pip install tweepy`

Then run it

`python blockjerks.py`

#### Disclaimer

I take no responsibility for any blowback that stems from your jerk-blocking activities.
