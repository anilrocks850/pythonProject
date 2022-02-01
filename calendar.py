date,month,year = (1,1,2001)
weekday_dict = {0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
def year_odd_days (year):
    year=year-1
    year = year % 400
    odd_days = (year//100)*5
    year = year%100
    leap_years = year//4
    odd_days += (year-leap_years) + leap_years*2
    return odd_days%7
print(year_odd_days (year))
month_odd_days = {0:0,1:3,2:3,3:6,4:1,5:4,6:6,7:2,8:5,9:0,10:3,11:5}
if year%4 == 0:
    month_odd_days = {0: 0, 1: 3, 2: 4, 3: 0, 4: 2, 5: 5, 6: 0, 7: 3, 8: 6, 9: 1, 10: 4, 11: 6}
month = month-1
date_odd_days = date%7
odd_days = (year_odd_days (year) + month_odd_days[month] +date_odd_days)%7
print(weekday_dict[odd_days])

