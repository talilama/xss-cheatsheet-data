#!/usr/bin/python

import sys
import json


browsers = ['edge','firefox','chrome','safari','all']
interactions = ['yes','no','all']
# TODO: add functionality for additional payloads besides alert(1)
poc_payloads = ['alert(1)', 'alert(random_integer)', 'confirm(random_integer)', 'prompt(random_integer)', 'console.log(random_integer)']

def usage():
        print "Usage: %s BROWSER INTERACTION [POC PAYLOAD]" % sys.argv[0]
        print "-Browser options: %s" % browsers
        print "-Require Interaction?: %s" % interactions
        print "-(Optional) Payload number: "
        print "\t[0]: alert(1)\t\t\t(DEFAULT)"
        for x in range(1,len(poc_payloads)): print "\t[%i]: %s" % (x, poc_payloads[x]) 
        exit(-1)


if __name__ == "__main__":
    if len(sys.argv) != 3: usage()
    browser = sys.argv[1]
    interaction = sys.argv[2]
    if browser not in browsers or interaction not in interactions: usage()
    
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
            
