#!/usr/bin/env python
# coding: utf-8

# In[9]:


import smtplib
import getpass
from email.mime.text import MIMEText


# In[12]:


def send_email():
    sender_address='shankarchoudhury47@gmail.com'
    password=getpass.getpass()
    subject='Learn.Inspire.Grow'
    msg='''
    Hello everyone 
    This is a demo message
    Thank you
    '''
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_address,password)
    
    msg=MIMEText(msg)
    msg['Subject']=subject
    msg['From']=sender_address
    msg['To']='shankarchoudhury47@gmail.com'
    #msg.set_param('importance','high value')
    recipients='shankarchoudhury47@gmail.com'
    server.sendmail(sender_address,recipients,msg.as_string()) 


# In[13]:


send_email()


# In[ ]:




