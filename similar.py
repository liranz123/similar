import json, datetime, time, dateutil
from datetime import datetime # just for checking that you dont need to write the full path of the class

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
        final.append('False')
    else:
        final.append('True')

    print(final)

if __name__ == '__main__':
    func('similarweb.com', 'domains.json', 30)
