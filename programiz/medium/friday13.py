from datetime import datetime
def is_friday_13(month, year):
    date=13
    day_obj=datetime(year,month,date).strftime('%A')
    if day_obj=='Friday':
        return True
    else:
        return False
print(is_friday_13(8,2010))