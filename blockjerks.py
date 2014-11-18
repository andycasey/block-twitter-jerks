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

# OAuth Handler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# API object
api = tweepy.API(auth)

# My user profile
me = api.me()

# Jerks
jerks = []
jerks.append('CorrellioRedux')
jerks.append('BernardGaynor')
jerks.append('aclobby')
jerks.append('chalky021154')
jerks.append('clementine_ford')
jerks.append('chriskkenny')
jerks.append('mirandadevine')
jerks.append('SharriMarkson')
jerks.append('CatherineDeveny')
jerks.append('Asher_Wolf')
jerks.append('Vanbadham')
jerks.append('RitaPanahi')
jerks.append('StevensAsh')
jerks.append('struct') # <3

# Followers/Following. Probably jerks.
followers = []
following = []
blocked = []
filename = "jerks.csv"

# Saved values
alpha_jerk_iteration = 0
beta_jerk_page = 0
beta_jerk_iteration_type = 0

def get_shelf():
	# Jerk shelf
	shelf = shelve.open('jerk-shelf')
	try:
		global blocked
		global alpha_jerk_iteration
		global beta_jerk_iteration_type
		global beta_jerk_page

		blocked = shelf['blocked']
		alpha_jerk_iteration = shelf['alpha_jerk_iteration']
		beta_jerk_page = shelf['beta_jerk_page']
		beta_jerk_iteration_type = shelf['beta_jerk_iteration_type']

		for s in blocked:
			print s
	except KeyError:
		print "ERROR: Could not open shelf file"
	shelf.close()

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

def update_shelf(key, value):
	shelf = shelve.open('jerk-shelf')
	shelf[key] = value;
	shelf.sync();
	shelf.close();

def block_jerk(screen_name):
	if [screen_name] not in blocked:
		# Add to the blocked list
		blocked.append([screen_name])
		# Create block
		api.create_block(screen_name)
		# Update shelf
		update_shelf('blocked', blocked)
	else:
		print "Skipped: @" + screen_name + " already blocked"


def block_jerks(page):
	for betajerk in page:
		if betajerk.id in following:
			print "Skipped: You're following @" + betajerk.screen_name
		elif betajerk.id in followers:
			print "Skipped: @" + betajerk.screen_name + " follows you"
		elif [betajerk.screen_name] in blocked:
			print "Skipped: @" + betajerk.screen_name + " already blocked"
		else:
			print "Blocking jerk: @" + betajerk.screen_name
			block_jerk(str(betajerk.screen_name))

		# Dump file
		dump_file()

def dump_file():
	# Dump jerks into a file
	f = open(filename, 'wb')
	w = csv.writer(f)
	w.writerows(blocked)
	f.close()

def iterate():
	print "================================================================================"
	print "HELLO " + me.screen_name
	print "You have " + str(len(followers)) + " followers"
	print "You are following " + str(len(following)) + " people"
	print "================================================================================"
	print "SHELF INFO"
	print "	Alpha Jerk Iteration: " + str(alpha_jerk_iteration)
	print "	Beta Jerk Page: " + str(beta_jerk_page)
	print "	Beta Jerk Iteration Type: " + str(beta_jerk_iteration_type)

	# Jerk loop
	x = 0
	y = 0
	for jerk in jerks:
		# Block jerk
		if x >= alpha_jerk_iteration:
			print "================================================================================"
			print "BLOCKING @" + jerk
			print "================================================================================"
			block_jerk(jerk)
			update_shelf('alpha_jerk_iteration', x)

			# Block jerk's followers
			print "================================================================================"
			print "BLOCKING @" + jerk + "'s jerk followers"
			print "================================================================================"
			
			for page in tweepy.Cursor(api.followers, jerk, count=200).pages():
				if y >= beta_jerk_page and (beta_jerk_iteration_type == 0 or beta_jerk_iteration_type == 1):
					update_shelf('beta_jerk_iteration_type', 1)
					update_shelf('beta_jerk_page', y)
					block_jerks(page)
				else:
					print "Skipping page " + str(y)
				y += 1

				print "Sleeping for 60 seconds..."
				time.sleep(60)
			
			y = 0
			# Block jerks this jerk follows
			print "================================================================================"
			print "BLOCKING jerks @" + jerk + " follows"
			print "================================================================================"
			for page in tweepy.Cursor(api.following, jerk, count=200).pages():
				if y >= beta_jerk_page and (beta_jerk_iteration_type == 0 or beta_jerk_iteration_type == 2):
					update_shelf('beta_jerk_iteration_type', 2)
					update_shelf('beta_jerk_page', y)
					block_jerks(page)
				else:
					print "Skipping page " + str(y)
				y += 1

				print "Sleeping for 60 seconds..."
				time.sleep(60)
		else:
			print "Skipping jerk " + jerk
	
		x += 1

# Get my followers/friends
get_following()
get_followers()
get_shelf()
iterate()
