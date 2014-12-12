# -*- coding: utf-8 -*-
# download

import requests
import json


def main():
    url = 'https://api.keen.io/3.0/projects/[project id]/queries/extraction?api_key=[read key]&event_collection=[collection name]'
    r = requests.get(url)
    x = to_unicode_or_bust(r.json)

    import csv
    f = open('dict.csv', 'wb')
    for y in x["result"]:
        w = csv.DictWriter(f, y.keys())
        w.writerow(y.encode('utf-8'))
    f.close()


def to_unicode_or_bust(obj, encoding='utf-8'):
    if isinstance(obj, basestring):
        if not isinstance(obj, unicode):
            obj = unicode(obj, encoding)
    return obj


#print x
# now need to parse that into a csv.