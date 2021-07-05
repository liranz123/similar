import json, datetime, time, dateutil
from dateutil import parser
from datetime import datetime, timedelta

f = open('domains.json')
data = json.load(f)
starts = data['similarweb.com']['notBefore']
ends = data['similarweb.com']['notAfter']

starts = starts.replace('GMT', '%') # get rid of the gmt string 
ends = ends.replace('GMT', '%')

starts = time.mktime(datetime.strptime(starts, "%b %d %H:%M:%S %Y %%").timetuple())
ends = time.mktime(datetime.strptime(ends, "%b %d %H:%M:%S %Y %%").timetuple())

diff = ends - starts

print(diff/3600/24) 


