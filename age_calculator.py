# calculate your age
import datetime


def ageCalculator(y, m, d):

    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
# count 365 and 366 days once in 4 years as 0.25
    age = int((today-dob).days/365.25)
    print("Your age is:", age)
# y = year m = month d = day


y = int(input("enter your birth year:"))
m = int(input("enter your birth month (1-12):"))
d = int(input("enter your birth day (1-31):"))
ageCalculator(y, m, d)