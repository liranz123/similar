import json, datetime, time, dateutil
from dateutil import parser
from datetime import datetime, timedelta

starts = "May 23 21:01:10 2021 GMT"
ends = "May 24 20:01:10 2021 GMT"

starts = starts.replace('GMT', '%') # get rid of the gmt string 
ends = ends.replace('GMT', '%')

starts = time.mktime(datetime.strptime(starts, "%b %d %H:%M:%S %Y %%").timetuple())
ends = time.mktime(datetime.strptime(ends, "%b %d %H:%M:%S %Y %%").timetuple())

diff = ends - starts

print(diff/3600)


