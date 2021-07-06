import json, datetime, time, dateutil
from dateutil import parser
from datetime import datetime, timedelta

def func(domain, file, allowed):

    f = open(file)
    data = json.load(f)

    altnames = []
    for i in data[domain]['subjectAltName']:
        altnames.append(i[1])
    print (sorted(altnames))
        


if __name__ == '__main__':
    func('amazon.com', 'domains.json', 30)
