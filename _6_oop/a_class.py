#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

class Animal:
    def __init__(self, name):
        self.name = name
    
    def getName(self):
        print("姓名：%s" % (self.name))

class Person(Animal):
    def __init__(self, name, school):
        self.name = name
        self.school = school
    def getSchool(self):
        print("学校：%s" % (self.school))

p1 =  Person('张三', '小学')
p1.getName()
p1.getSchool()