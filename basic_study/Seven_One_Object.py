# -*- coding:utf-8 -*-
class student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def introduce(self):
        print ("hi ,I'm " + self.name)
        print ("my grade is " + str(self.grade))

    def improve(self, amount):
        self.grade = self.grade + amount


Jim = student('Jim', 86)
Jim.introduce()
Jim.improve(8)
Jim.introduce()
