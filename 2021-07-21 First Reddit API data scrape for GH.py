#!/usr/bin/env python
# coding: utf-8

# In[1]:


import praw #import praw python reddit api wrapper
import pandas as pd # import pandas as pd
import datetime as dt # import date-time function

reddit = praw.Reddit(client_id='client ID', 	client_secret='super secret squirrel phrase', 	user_agent='script name', 	username='yer username', 	password='yer password to the super secret club')
#above: reddit API stuff
# tutorial link https://www.storybench.org/how-to-scrape-reddit-with-python/

print(reddit.user.me())
## above tests API access


# In[2]:


a_sub = reddit.subreddit('news')

top_subreddit = a_sub.top()

#for submission in a_sub.top(limit=1):
#	print(submission.title, submission.id)
	
topics_dict = { "title": [], 	"score": [], 	"id": [], 	"url": [], 	"comms_num": [], 	"created": [], 	"body": []}

for submission in top_subreddit:
	topics_dict["title"].append(submission.title)
	topics_dict["score"].append(submission.score)
	topics_dict["id"].append(submission.id)
	topics_dict["url"].append(submission.url)
	topics_dict["comms_num"].append(submission.num_comments)
	topics_dict["created"].append(submission.created)
	topics_dict["body"].append(submission.selftext)
	
# above creates dict for several post fields, then loops thru 


# In[3]:


topics_data = pd.DataFrame(topics_dict)
# puts scraped data into a Pandas DataFrame


# In[4]:


# convert UNIX timestamps to ...
def get_date(created):
    return dt.datetime.fromtimestamp(created)

_timestamp = topics_data["created"].apply(get_date)

topics_data = topics_data.assign(timestamp = _timestamp)
    


# In[5]:


topics_data
# displays data frame; ought to be with appended timestamp


# In[6]:


import time
the_date = time.strftime("%d-%m-%Y")
csv_name = the_date + ' data scrape.csv'
topics_data.to_csv(csv_name, index=False)


# In[ ]:




