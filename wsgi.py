#!/usr/bin/python
##-------------------------------------------------------------------
## File : wsgi.py
## Author : Denny <https://www.dennyzhang.com/contact>
## Description :
## --
## Created : <2017-06-02>
## Updated: Time-stamp: <2017-11-13 11:00:55>
##-------------------------------------------------------------------
from chatops import application
from chatops import start_app

if __name__ == "__main__":
    start_app(application)
## File : wsgi.py ends
