#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyttsx3
import PyPDF2


# In[3]:


book = open('agm.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()

#"""VOICE"""
voices = speaker.getProperty('voices')
#speaker.setProperty('voice', voices[0].id) #male
speaker.setProperty('voice', voices[1].id) #female

# """VOLUME"""
volume = speaker.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
speaker.setProperty('volume',0.5)    # setting up volume level  between 0 and 1
# print(volume)                          #printing current volume level

# """ RATE"""
rate = speaker.getProperty('rate')   # getting details of current speaking rate
speaker.setProperty('rate', 125)     # setting up new voice rate
# print(rate)                        #printing current voice rate

for num in range(0, 1):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()


# In[3]:


# """Saving Voice to a file"""
speaker.save_to_file(text, 'test.mp3')
speaker.runAndWait()

