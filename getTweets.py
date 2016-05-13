
# coding: utf-8

# In[6]:

import MySQLdb as mdb


# In[7]:

import sys


# In[8]:

con = mdb.connect('128.206.116.195', 'tg4_ro', '?3stEt7!3hUbRa-R', 'tw4_db');


# In[9]:

cur = con.cursor()


# In[10]:

cur.execute("SELECT VERSION()")


# In[11]:

ver = cur.fetchone()


# In[12]:

print ("Database version : %s " % ver)


# In[17]:

cur.execute("Select month(created_at) as theMonth, day(created_at) as theDay, year(created_at) as theYear, count(*) as counter from tweet where job_id=2616 group by theYear, theMonth, theDay")


# In[18]:

ver = cur.fetchall()


# In[22]:

with open('intermediate_data.txt', 'w') as f:
    for row in ver:
        for x in row:
            f.write(str(x) + ",")
        f.write("\n")


# In[23]:

cur.execute("Select Count(*) from tweet")


# In[24]:

x = cur.fetchall()


# In[25]:

print(x)


# In[ ]:



