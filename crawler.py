from abc import ABC, abstractclassmethod
import requests
from bs4 import BeautifulSoup
import json
from analyze import Analyzer
import os
from mongodb import Mongodb

class Base(ABC):
    @abstractclassmethod
    def start(self):
        pass

    def get_page(self, url):
        # Get utl's source code
        try:
            return requests.get(url).text
        except requests.HTTPError:
            raise requests.HTTPError("Something went wrong!")


class Getlinks(Base):
    """This class is used too find all courses and save them is db/link-db.json"""
    def __init__(self, website):
        self.website = website 

    def find_links_images(self, source):
        # Get all links
        code = BeautifulSoup(source, "html.parser")
        content = code.find("div", attrs={"id": "courses"}) #too select courses part

        # Find and store all links
        links = content.find_all('a')
        course_links = [] #Stored all courses links
        for l in links:
            course_links.append(l.get('href'))

        #Find and store all images
        course_images = []  #Stored all courses images
        for image in links:
            i = image.find_all('img', attrs= {"class": "cover"})
            for im in i:
                course_images.append(im.get('src'))

        return course_links, course_images  #return links and images 

    def start(self):
        source = self.get_page(self.website)
        links, images = self.find_links_images(source)
    
        self.save(links, images)    #call save to store all data in db
    
    def save(self, links, images):
        data = dict()
        num = 0
        while num <= len(links) -1:
            data[links[num]] = images[num]
            num += 1

        os.makedirs("db", exist_ok=True)
        with open("db/link-db.json", "w") as file:
            file.write(json.dumps(data))
            file.close()
            
        print(str(len(links)) + " Link saved in: db/link-db.json")


class Getpages(Base):
    """This class is to crawl all courses pages."""
    def __init__(self, links_db):
        self.links_path = links_db # path to db

    def __load_db__(self):
        if not os.path.exists(self.links_path):    # check if links have been found or not!
            raise FileNotFoundError("Links database not found!\nPlease first run -> python main.py extarxt_courses")
        # get pages from db
        with open(self.links_path, "r") as file:
            pages = json.loads(file.read())
            file.close()
        return pages

    def start(self, save_mode="json-document"):
        pages_url = self.__load_db__()# load data from links-db.json
        for course_link in pages_url.keys():# analyze each page from pages_url
            html_doc = self.get_page(course_link)
            parser = Analyzer()
            data = parser.analyze(html_doc, pages_url[course_link])

            if save_mode == "json-document": # save extacted data
                self.save_document(data["CourseName"], json.dumps(data))
            else:
                self.save_mongo("7learn-courses", data)
                print(data["CourseName"] + " Done.")
        print("All Done.")
   
    def save_document(self, filename, data):
        os.makedirs("db/courses", exist_ok=True)
        filepath = f"db/courses/{filename}.json"
        with open(filepath, "w") as file:
            file.write(data)
        
    def save_mongo(self, collection_name, data):
        self.mongo = Mongodb()  # connect to mongodb
        db = self.mongo.client["7learn-crawler"] # create a database 
        collection = db[collection_name] # create a collection
        collection.insert_one(data) # Add data to database






    

