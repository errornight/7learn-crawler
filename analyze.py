"""Courses page crawler."""

from bs4 import BeautifulSoup
class Analyzer():
    
    def get_title(self):
            # find CourseName
        title_tag = self.soup.find("span", attrs={"class" : "title"})
        self.data["CourseName"] = title_tag.text

    def get_teacher(self):
            # find CourseTeacherName
        name_tag = self.soup.find("p", attrs={"class": "mb-5"})
        name = ((name_tag.text[8::]).split("\n"))[0]
        name = name.replace(u"\xa0", "")
        self.data["CourseTeacherName"] = name

    def get_description(self):
        # find CourseDescription
        content_des = self.soup.find("div", attrs={"id": "land-sc-text-body"})
        description_tag = content_des.find_all("p")
        description = list()
        if description_tag:
            for i in description_tag:
                description.append(i.text)
        self.data["CourseDescriptin"] = ''.join(description)    

    def get_longtime(self):
        # find course CourseLongtime
        # time_tag = self.soup.find("div", attrs={"class": "tabs"})
        # time_tag = (time_tag.text).split("\n")
        # for i in time_tag:
        #     if "ساعت" in i:
        #         self.data["CourseLongtime"] = i
        selector = ".left > div:nth-child(2) > div:nth-child(1)"
        longtime = self.soup.select_one(selector)
        if longtime:
            self.data["CourseLongtime"] = longtime.text


    def get_price(self):
            # find CoursePrice
        price_tag = self.soup.find("div", attrs={"class": "plan-bold text-success"})
        if price_tag:
            self.data["CoursePrice"] = price_tag.text

    def analyze(self, html_doc, course_image=None):
        self.soup = BeautifulSoup(html_doc, 'html.parser')

        self.data = dict(CourseName= None, CourseTeacherName= None, CourseDescriptin= None, 
                    CourseLongtime= None, CoursePrice= None, CourseImageLink= course_image)
        self.get_title()
        self.get_teacher()
        self.get_description()
        self.get_longtime()
        self.get_price()

        return self.data
    





        