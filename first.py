# veriables in python
# a=5
# print(a)
# b="hello"
# print(b)

# import turtle
# pruthvi = turtle.Turtle();
# pruthvi.forward(100)
# pruthvi.right(90)
# pruthvi.forward(100)
# pruthvi.right(90)
# pruthvi.forward(100)
# pruthvi.right(90)
# pruthvi.forward(100)

# Function 

# import turtle
# pruthvi = turtle.Turtle()
# def square():  # Decleare Function
#     pruthvi.forward(100)
#     pruthvi.right(90)
#     pruthvi.forward(100)
#     pruthvi.right(90)
#     pruthvi.forward(100)
#     pruthvi.right(90)
#     pruthvi.forward(100)
# square() # define the function
# pruthvi.forward(200)
# square()

# Caleder in pythons

# import calendar
# import datetime
# import time

# print(calendar.weekheader(3))
# print()
# print(calendar.firstweekday())
# print()
# print(calendar.month(2021,9))

# print(calendar.monthcalendar(2021, 9))

# print(calendar.calendar(2021))

# day_of_the_week = calendar.weekday(2021,9,24);
# print(day_of_the_week)

# is_leep = calendar.isleap(2020)
# print(is_leep)

# how_many_weeks_day = calendar.leapdays(2000, 2020)
# print(how_many_weeks_day)

# If Elase Statments

# elephant_weight = 3000
# ant_weight = 0.1
# import turtle
# pruthvi = turtle.Turtle()
# def square():  # Decleare Function
#     pruthvi.forward(100)
#     pruthvi.right(90)
#     pruthvi.forward(100)
#     pruthvi.right(90)
#     pruthvi.forward(100)
#     pruthvi.right(90)
#     pruthvi.forward(100)

# if elephant_weight < ant_weight:
#     square() # define the function
# else:
#     pruthvi.forward(100)

# While Loops

    # import turtle
    # pruthvi = turtle.Turtle()
    # pr = 'happy'
    # while pr == 'happy':
    #     pruthvi.forward(100)

# For Loops
 
    # for i in range(10):
    #     print(i)

# Primative Data Types

    # integer
    # 1,2,3
    # Floates
    # 1.23
    # Booleans
    # True or False
    # String
    # 'pruthviraj'
    
# Casting

    # a= float(1)
    # print(a)
    # b = str(1)
    # print(b)
    # c= int("35")
    # print(c)

# String In Python

    # s = "hello world"
    # print(s[0])

# List In Python

    # list = [1,2,3,"pruthviaj",True,4.3]
    # print(list)
    # print(list[3]) 

    # List Function

    # names = ['joe','john','james']
    # print(names)

    # names.append('gary')
    # print(names)

    # names.insert(0,'dev')
    # print(names)

    # names.remove('john')
    # print(names)

    # names.reverse()
    # print(names)

    # numbers = [1,5,9,5,6]
    # print(number)

    # number.sort()
    # print(number)

    # for number in numbers:
    #     print(number)
    
# Indexing, Slicing Array

    # digits = [0,1,2,3,4,5,6,9]
    # # name = "first last"
    # # print(name[:2])
    # # print(digits[5:10])
    # # print(digits[0:10:3])
    # # print(digits[5:0:-2])

    # for i in range(len(digits)):
    #     print(digits[0:i])
    # for i in range(len(digits)):
    #     print(digits[i:i+3])
    
# Join and Splitting

    # problems = 'broke, pale, short, nerdy';
    # # print(problems)
    # l = problems.split(", ");
    # # print(l)
    # joined =' and '.join(l)
    # print(joined)

    # csv =','.join(l)
    # print(csv)
    
# Tuples in Python

    # t = (1,2,3)
    # # print(t[0])
    # creadit_card1 = (1235256521,'Joe Rogen','11/20',123);
    # creadit_card2 = (1235256521,'Joe Rogen','11/20',123);

    # create_cards = [creadit_card1,creadit_card2]
    # print(create_cards)
    # person1 = ("Nancy-pants",25,'Pizza')
    # person2 = ("Joe-Shirt",30,'Pasta')
    # people = [person1,person2]
    # (name,age,favfoo) = people
    # print(name)
    # print(age)
    # print(favfoo)

    # for name,age,favfoo in people:
    #     print(name)
    #     print(age)
    #     print(favfoo)
    #     print()

# Sets in Python 

    # l = [1,2,3,3,5,5,7,8,9,'abc','abc']
    # print(l)
    # no_duplicate = set(l)
    # print(no_duplicate)
    # s= {'blueberry','resberry'}
    # s.add('strawberry')
    # s.add('blueberry')
    # s.add(4)
    # print(s)
    # no_duplicate_list = list(no_duplicate);
    # print(no_duplicate_list)
    
    # library_1 = {'Harry Potter','Hunger Games','Lord of the Rings'}
    # library_2 = {'Harry Potter','Romeo and Julieo'}
    # all_boxes_towns= library_1.union(library_2)

    # same_boxes_towns= library_1.intersection(library_2)

    # diff = library_1.difference(library_2)

    # print(all_boxes_towns)
    # print(same_boxes_towns)
    # print(diff)
    
# Dictionaries

    # groceries = {'bananas':5,'oranges':3}

    # print(groceries['bananas'])

    # print(groceries.get('bananas'))
    
    # contacts = {
    #     'Joe':{'phone':1234567,'email':'example@gmail.com'},
    #     'Jane':{'phone':1234567,'email':'example@gmail.com'}
    # }

    # print(contacts['Joe'])

    # from collections import OrderedDict 

    # sentence = "I Like name Asron beacuase the name Aaron is the best"

    # words_counts = {
    #     'I':1,
    #     'like':1,
    #     'the':3
    # }
    # print(words_counts)
    # words_counts['Aaron'] = 2
    # print(words_counts)

    # # dict.items()
    # print(list(words_counts.items()))
    # # dict.keys()
    # print(list(words_counts.keys()))
    # # dict.values()
    # print(list(words_counts.values()))

    # Delete Iteam From Dictionaries
    # words_counts.pop('I')
    # print(list(words_counts.items()))

    # print(words_counts.popitem())
    # print(words_counts)

    # dict.clear()
    # words_counts.clear()

    # Sorted using python package
    # print(sorted(list(words_counts.items())))
    
# Mutlibality
    
    # inmutable( tuples,ints,floats,strings,booleans )
    # mutable ( lists,dictionary,orderedDict )

    # t = (1,2,3,[1,2,3])
    # print(t)
    # t[3][0]=6;
    # print (t)
        
# List Comprehension

    # names = ['Jennifer','Susan','Jane','Sophie']

    # l=[]
    # for person in names:
    #     l.append(person)
    # print(l)

    # print([person for person in names])

    # l = []
    # for person in names:
    #     l.append(person + ' dumped me ')
    # print(l)

    # print([person + ' dumped me ' for person in names])

    # movies = {"Interstellar":9,"Dark Knight":8,"50 Shades":3,"50 Shades Darker":2}
    # l=[]

    # for movie in movies:
    #     if movies[movie] >6 :
    #         l.append(movie)
    # print(l)

    # print([movie for movie in movies if movies[movie] > 6])
    
#  Regex

    # Email Finder
    
    # import re

    # text = "A random string. MyName123@website.com. some more randome text. your_Name5-8-8@company.com"
    # # pattern = re.compile("[a-zA-Z0-9]+")
    # pattern = re.compile("[a-zA-Z0-9\.\-\_]+@[a-zA-Z0-9]+\.[a-zA-Z]+")
    # # result = pattern.search(text)
    # result = pattern.findall(text) # Find All Email Id
    # print(result)
    
    # DateTime Module

    # import datetime
    # import pytz

    # today = datetime.date.today()
    # print(today)
    # birthday = datetime.date(2000, 5 , 30)
    # print(birthday)

    # days_since_birth = (today - birthday).days
    # print(days_since_birth)

    # tdelta = datetime.timedelta(days=10)
    # print(today + tdelta)
    # print(today - tdelta)

    # print(today.month)
    # print(today.day)
    # print(today.weekday())

    # print(datetime.time(7, 2 , 20, 15))

    # datetime.date ( Y, M, D)
    # datetime.time (h,m,s,ms)
    # datetime.datetime( y, m, d ,h, m, s, ms)

    # Add 10 hours to current day
    # hour_delta = datetime.timedelta(hours=10)
    # print(datetime.datetime.now()+hour_delta)
    # print(datetime.datetime.now())

    # print(datetime.datetime.now(tz=pytz.UTC))
    # datetime_pacific =datetime.datetime.now(tz=pytz.UTC).astimezone(pytz.timezone('US/Pacific'))
    # print(datetime_pacific)

    # for tz in pytz.all_timezones:
    #     print(tz)
        
    # string formating with dates
    # 2019-03-09 => march 3, 2019

    # print(datetime_pacific.strftime('%B %d %Y'))
    # dateTime_Thing = datetime.datetime.strptime('March 09, 2019', '%B %d, %Y')
    # print(repr(dateTime_Thing))

# Web Scraping

# ( beautiful soap And requests)


