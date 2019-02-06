from datetime import datetime as dt
tm_now = dt.now()
tm_now.year
tm_now.y
tm_now.month
tm_now.day
tm_now.hour
tm_now.minute
tm_now.second
tm_now.weekday()

delta = dt(2019, 6, 1) - dt(2019, 1, 1, 1, 2, 3)
delta
