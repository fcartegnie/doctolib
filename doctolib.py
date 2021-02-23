from urllib.request import urlopen, Request
from datetime import datetime
import argparse
import sys
from random import randint
import time
import json

receivers = []

def get_next_appointement(url):
    jsonread = urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36', 'Accept': 'application/json'})).read()
    jsonDate = json.loads(jsonread)
    return datetime.strptime(jsonDate['next_slot'], '%Y-%m-%d')

def main():
    # Install the argument parser. Initiate the description with the docstring
    argparser = argparse.ArgumentParser(
        description=sys.modules[__name__].__doc__)
    # this is a option which need one extra argument
    argparser.add_argument('-u',
                           "--url",
                           required=True,
                           help="set the url to check")
    argparser.add_argument('-d',
                           "--date",
                           required=True,
                           help="format : dd-mm-yyyy")

    arguments = argparser.parse_args()
    appointement_wanted = datetime.strptime(arguments.date, '%d-%m-%Y')

    while True:
        next_appointement = get_next_appointement(arguments.url)
        if(appointement_wanted > next_appointement):
            sys.stdout.write("appointement wanted = {}\n".format(appointement_wanted))
            sys.stdout.write("next appointement = {}\n".format(next_appointement))
            sys.exit()
        else:
            sys.stderr.write("{}: {}\n".format(time.strftime("%H:%M:%S"), next_appointement))
            time.sleep(3600 + randint(0, 1500))

if __name__ == "__main__":
    main()
