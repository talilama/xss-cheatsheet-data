#!/usr/bin/python

import sys
import json

#TODO add option for encoding of payloads
#TODO add tag and event filters for events

vectors = ['events', 'protocols', 'all']
browsers = ['edge','firefox','chrome','safari','all']
interactions = ['yes','no','all']
payloads = ['alert(1)', 'alert(random_integer)', 'confirm(random_integer)', 'prompt(random_integer)', 'console.log(random_integer)']


def usage():
        print "Usage: %s VECTOR BROWSER USER_ACTION? [POC_PAYLOAD]" % sys.argv[0]
        print "Example: %s events chrome no 1\n"
        print "-VECTOR options \t(Default: all)\t \t%s" % vectors
        print "-BROWSER options \t(Default: all)\t \t%s" % browsers
        print "-USER_ACTION? options \t(Default: no)\t \t%s" % interactions
        print "-POC_PAYLOAD options \t(Default [0]: alert(1))\t "
        for x in range(0,len(payloads)): print "\t[%i]: %s" % (x, payloads[x])
        exit(-1)

def getProtocols():
    f = "json/protocols.json"
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
                if browser in tag['browsers']:
                    if interaction == "all" or (interaction == "yes" and tag['interaction']) or (interaction == "no" and not tag['interaction']):
                        print chooseCode(tag['code'])
                elif browser == 'all' and len(tag['browsers']) == 4:
                    print chooseCode(tag['code'])

def chooseCode(code):
    if int(p) == '0': return code
    payload = payloads[int(p)]
    return code


if __name__ == "__main__":
    vector = 'all'
    browser = 'all'
    interaction = 'no'
    p = '0'
    if len(sys.argv) > 1 : vector = sys.argv[1]
    if len(sys.argv) > 2 : browser = sys.argv[2]
    if len(sys.argv) > 3 : interaction = sys.argv[3]
    if len(sys.argv) > 4 : p = int(sys.argv[4])
    if vector not in vectors or browser not in browsers or interaction not in interactions: usage()
    if int(p) not in range(0,len(payloads)): usage()
    if vector == 'all':
        getEvents()
        getProtocols()
    elif vector == 'events': 
        getEvents()
    elif vector == 'protocols': 
        getProtocols()
