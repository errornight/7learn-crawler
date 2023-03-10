#!bin/python3
"""
This script crawls all 7learn.com's courses and extract the following data:
    1- Course name
    2- Course teacher name
    3- Course description
    4- Course longtime
    5- Course price

Run this using following commands:
to find all courses links and images-> python main.py extract_courses 
to extract data from course -> python main.py extract_pages
"""

"""
You can save pages data using .json document or Mongodb.

Save as document -> config.py -> SAVE_MODE = "json-document"
Save in Mongodb -> config.py -> SAVE_MODE = "mongodb"
    Remember to use Mongodb on defult address and port(localhost, 27017)
    you can change that in mongodb.py file.
"""

# Imports
from crawler import *
import sys
import config 

if __name__ == "__main__":
    page = "https://7learn.com/courses"
    try:
        switch = sys.argv[1]
    except IndexError:
        raise Exception("Not definded command!\nUse extract_courses OR extract_pages.")
        

    if switch == "extract_courses":
        crawler = Getlinks(page)
        crawler.start()
    elif switch == "extract_pages":
        crawler = Getpages("db/link-db.json")
        crawler.start(save_mode=config.SAVE_MODE)
    else:
        raise Exception("Not definded command!\nUse extract_courses OR extract_pages.")