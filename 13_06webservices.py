#Twitter API
#web services

import urllib.request, urllib.parse, urllib.error
import twurl
import json

while True:
    print('')
    acct = input('Enter Twitter account:')
    if (len(acct) < 1):
        break

