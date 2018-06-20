#Q1


#what is access token?
#An access token is an object that describes the security context of a process or thread

#How generate your access token for any API
#sign in to developer account
#creat a new api
#under that go to keys and access token
#enerate access token



#Q2


#google ip address=172.217.15.68
#facebook ip address=31.13.69.230


#Q3

import tweepy
from keys import Consumer_Key,Consumer_Secret,Access_Token_Secret,Access_Token


oauth=tweepy.OAuthHandler(Consumer_Key, Consumer_Secret)
oauth.set_access_token(Access_Token, Access_Token_Secret)
api=tweepy.API(oauth)
print(api.search("#modi"))

#Q4
'''
API is a part of library which defines how an application communicates with external code
.
API can be written in any language.
Library is written in same language which is a collection of all the functionalities required for the use case.
For example : Numpy is a library of Python, adding support for large, multi-dimensional arrays and matrices, along
with a large collection of high-level mathematical functions to operate on these arrays.
'''
#q5
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('say something!')
    audio = r.listen(source)

try:
    print('google thinks you said:\n' + r.recognize_google(audio))

except:
    pass