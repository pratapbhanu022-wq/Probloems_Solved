# to find whether a year is leap year or not
def is_leap(year):
    return year%4==0 and (year%400==0 or year%100!=0)
year = int(input('enter year :'))
print(is_leap(year))