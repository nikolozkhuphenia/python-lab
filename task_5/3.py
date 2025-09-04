#3 დაადგინე, არის თუ არა შეყვანილი წელი ნაკიანი, მომხმარებელს შემოჰყავს მხოლოდ წელი და ვეუბნებით არის თუ არა ნაკიანი
import calendar

myinput = int(input("შეიყვანეთ წელი: "))

if calendar.isleap(myinput):
    print(f"{myinput} წელი არის ნაკიანი.")
else:
    print(f"{myinput} წელი არ არის ნაკიანი.")
