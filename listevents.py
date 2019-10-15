#!/usr/bin/python

import sys
import json

vectors = ['events','
browsers = ['edge','firefox','chrome','safari','all']
interactions = ['yes','no','all']
payloads = ['alert(1)', 'alert(random_integer)', 'confirm(random_integer)', 'prompt(random_integer)', 'console.log(random_integer)']

def usage():
        print "Usage: %s BROWSER INTERACTION [POC PAYLOAD]" % sys.argv[0]
        print "-Browser options: %s" % browsers
        print "-Require Interaction?: %s" % interactions
        print "-(Optional) Payload number: "
        print "\t[0]: alert(1)\t\t\t(DEFAULT)"
        for x in range(1,len(payloads)): print "\t[%i]: %s" % (x, payloads[x])
        exit(-1)

def getProtocols():
    f = "protocols.json"
    with open(f) as json_file:
        data = json.load(json_file)
    for tag in data:
        if browser in tag['browsers'] or browser == 'all':
            print tag['code']

def getEvents():
    f = "json/events.json"
    with open(f) as json_file:
        data = json.load(json_file)
    for i in data:
        for j in data[i]:
            tags = data[i]['tags']
            for tag in tags:
                if browser in tag['browsers'] or browser == 'all':
                    if interaction == "yes" and tag['interaction']:
                        print tag['code']
                    elif interaction == "no" and not tag['interaction']:
                        print tag['code']
                    elif interaction == "all":
                        print tag['code']


if __name__ == "__main__":
    vector = 'all'
    browser = 'all'
    interaction = 'no'
    payload = ''
    if sys.argsv[1]: vector = sys.argsv[1]
    if sys.argsv[2]: browser = sys.argsv[2]
    if sys.argsv[3]: interaction = sys.argsv[3]
    if sys.argsv[4]: payload = int(sys.argsv[4])
    if vector not in vectors or browser not in browsers or interaction not in interactions or payload not in range(0,len(payloads)): usage()
    
