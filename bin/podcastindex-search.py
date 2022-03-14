#!/usr/bin/env python

# given a search execute a search on the PodcastIndex.org API
# return output as JSON output
#
# Use case 1
#   Provide a real-time Splunk search interface into PodcastIndex
# Splunk index
#   podcastindex-podcasts

import os,sys,time

APP_NAME='podcastindex-splunk-app'
splunkhome = os.environ['SPLUNK_HOME']
apphome = os.path.join(splunkhome, 'etc', 'apps', APP_NAME)
sys.path.append(os.path.join(apphome, 'lib'))
sys.path.append(os.path.join(splunkhome, 'etc', 'apps', 'searchcommands_app', 'lib'))
import podcastindex

## TODO these secret should be configurable from the user
config = {
    "api_key": "3BMYBXGEWMG8P46V8NJY",
    "api_secret": "gtsB#x2V77EbyDsm5ysbsJFbsjD6EZDN87hcF3XF"
}


def ignore():
    index = podcastindex.init(config)

    result = index.search("This American Life")
    for r in result["feeds"]:
        r.update({'_time' : int(time.time())})
        print(r)

ignore()


#with open("./sample.txt") as f:
#  print(f.read())