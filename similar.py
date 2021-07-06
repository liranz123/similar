import json, datetime, time, dateutil
#from dateutil import parser
from datetime import datetime

def func(domain, file, allowed):

    final = [] # output array 

    f = open(file)
    data = json.load(f)

    altnames = [] # alt names array
    for i in data[domain]['subjectAltName']:
        altnames.append(i[1])
    sorted(altnames)
    alttotal = len(altnames) # total number of alt names

    final.append(domain)
    final.append(alttotal)
    final.append(altnames)

    print(final)


    starts = data[domain]['notBefore']
    ends = data[domain]['notAfter']

    starts = starts.replace('GMT', '%') # get rid of the gmt string 
    ends = ends.replace('GMT', '%')

    starts = time.mktime(datetime.strptime(starts, "%b %d %H:%M:%S %Y %%").timetuple())
    ends = time.mktime(datetime.strptime(ends, "%b %d %H:%M:%S %Y %%").timetuple())

    diff = ends - starts # number of days the cert is valid
    diff = int(diff/3600/24) # round the float result to int
    final.append(diff)

    if allowed < diff:
        final.append('True')
    else:
        final.append('False')

    print(final)

if __name__ == '__main__':
    func('similarweb.com', 'domains.json', 30)
