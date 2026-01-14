import datetime as dt

now = (dt.datetime.now())

#------------------------------------------------ Today----------------------------------------------------------------#
year= now.year
day= now.day
month= now.month
weekday  = now.weekday()


#------------------------------------------------Choosing another day--------------------------------------------------#
date_of_birth = dt(year= 1995,
                   month = 12,
                   day = 15)