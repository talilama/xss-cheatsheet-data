#!/usr/bin/python

import sys
import json


browsers = ['edge','firefox','chrome','safari', 'all']
# TODO: add functionality for additional payloads besides alert(1)
poc_payloads = ['alert(1)', 'alert(random_integer)', 'confirm(random_integer)', 'prompt(random_integer)', 'console.log(random_integer)']

def usage():
        print "Usage: %s BROWSER" % sys.argv[0]
        print "-Browser options: %s" % browsers
        '''print "-(Optional) Payload number: "
        print "\t[0]: alert(1)\t\t\t(DEFAULT)"
        for x in range(1,len(poc_payloads)): print "\t[%i]: %s" % (x, poc_payloads[x])'''
        exit(-1)



if __name__ == "__main__":
    if len(sys.argv) != 2: usage()
    browser = sys.argv[1]
    if browser not in browsers: usage()

    f = "json/protocols.json"
    with open(f) as json_file:
        data = json.load(json_file)
    for tag in data:
        if browser in tag['browsers'] or browser == 'all':
            print tag['code']
