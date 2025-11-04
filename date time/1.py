import datetime
date_input=input()
date_obj=datetime.datetime.strptime(date_input,"%m %d %Y")
day_name=date_obj.strftime("%A")
print(day_name.upper())