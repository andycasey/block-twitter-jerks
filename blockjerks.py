#!/usr/bin/env python
# blockjerks.py
# Block twitter jerks, their followers, and jerks they follow for a more pleasant Twitter experience
# Author : David Johnson <@struct>
 
import tweepy
import time
import csv

# Key settings
consumer_key 		= ""
consumer_secret 	= ""
access_token 		= ""
access_token_secret	= ""
filename			= "jerks.csv"

# OAuth Handler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# API object
api = tweepy.API(auth)

# My user profile
me = api.me()

# Jerks
jerks = []
jerks.append('clementine_ford')
jerks.append('benpobjie')
jerks.append('chriskkenny')
jerks.append('mirandadevine')
jerks.append('SharriMarkson')
jerks.append('CatherineDeveny')
jerks.append('CorrellioRedux')
jerks.append('Asher_Wolf')
jerks.append('chalky021154')

# Followers/Following. Probably jerks.
followers = []
following = []
blocked = []

def get_followers():
	followers_cursor = tweepy.Cursor(api.followers_ids, id=me.id)
	for id in followers_cursor.items():
		if id not in followers and id not in following:
			followers.append(id)

def get_following():
	friends_cursor = tweepy.Cursor(api.friends_ids, id=me.id)
	for id in friends_cursor.items():
		if id not in followers and id not in following:
			following.append(id)

def block_jerks(page):
	for subjerk in page:
		if subjerk.id in following:
			print "Skipped: You're following " + subjerk.screen_name
		elif subjerk.id in followers:
			print "Skipped: " + subjerk.screen_name + " follows you"
		elif subjerk.id in blocked:
			print "Skipped: " + subjerk.screen_name + " already blocked"
		else:
			print "Blocking jerk: " + subjerk.screen_name
			# Add to the blobke list
			blocked.append([subjerk.screen_name])
			# Create block
			api.create_block(subjerk.id)

	print "Sleeping for one minute..."
	time.sleep(60)

# Get my followers/friends
get_following()
get_followers()

print "================================================================================"
print "Hello " + me.screen_name
print "You have " + str(len(followers)) + " followers"
print "You are following " + str(len(following)) + " people"
print "NOTE: There is a 60-second pause between blocking batches to avoid rate limiting"

# Jerk loop
for jerk in jerks:
	# Block jerk
	blocked.append([jerk])
	api.create_block(jerk)

	# Block jerk's followers
	print "================================================================================"
	print "BLOCKING " + jerk + "'s JERK FOLLOWERS"
	print "================================================================================"
	
	for page in tweepy.Cursor(api.followers, jerk).pages():
		block_jerks(page)

	# Block jerks this jerk follows
	print "BLOCKING JERKS " + jerk + " FOLLOWS"
	print "================================================================================"
	for page in tweepy.Cursor(api.following, jerk).pages():
		block_jerks(page)

# Dump jerks into a file
f = open(filename, 'wb')
w = csv.writer(f)
w.writerows(blocked)
f.close()
