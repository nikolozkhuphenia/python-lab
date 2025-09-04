#2 იპოვე მომდევნო კვირის პირველი სამშაბათი, საწყისი თარიღი არის დღევანდელი დღე (ხელით არ გაწეროთ თარიღი)

from datetime import date, timedelta

today = date.today()
this_week_monday = today - timedelta(days=today.weekday()) 
next_week_monday = this_week_monday + timedelta(days=7)
first_tuesday_next_week = next_week_monday + timedelta(days=1)
print(timedelta(days=today.weekday()))
print(next_week_monday)
print(first_tuesday_next_week.isoformat())
