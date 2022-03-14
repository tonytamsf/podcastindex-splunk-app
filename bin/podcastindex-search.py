#!/usr/bin/env python

# given a search execute a search on the PodcastIndex.org API
# return output as JSON output
#
# Use case 1
#   Provide a real-time Splunk search interface into PodcastIndex
# Splunk index
#   podcastindex-podcasts

# Splunk paths https://dev.splunk.com/enterprise/docs/developapps/createapps/appanatomy/#Considerations-for-Python-code-files
import os,sys,time
APP_NAME='podcastindex-splunk-app'
splunkhome = os.environ['SPLUNK_HOME']
apphome = os.path.join(splunkhome, 'etc', 'apps', APP_NAME)
sys.path.append(os.path.join(apphome, 'lib'))

# This should be loaded after path is updated
from splunklib.searchcommands import dispatch, GeneratingCommand, Configuration, Option

import podcastindex

## TODO these secret should be configurable from the user
config = {
    "api_key": "3BMYBXGEWMG8P46V8NJY",
    "api_secret": "gtsB#x2V77EbyDsm5ysbsJFbsjD6EZDN87hcF3XF"
}

@Configuration()
class PodcastIndexSearch(GeneratingCommand):
    keyword = Option(require=True)

    def generate(self):
        self.logger.info('Search on podcastindex.org {}'.format(self.keyword))
        index = podcastindex.init(config)

        result = index.search(self.keyword)
        for r in result["feeds"]:
            r.update({'_time' : r["lastUpdateTime"]})
            yield r 
    '''
    Convert headers string into dict
    @headers string: Headers as json string
    @return dict
    '''
    def parseHeaders(self, headers):
        # Replace single quotes with double quotes for valid json
        return json.loads(
          headers.replace('\'', '"')
        )


dispatch(PodcastIndexSearch, sys.argv, sys.stdin, sys.stdout, __name__)
#with open("./sample.txt") as f:
#  print(f.read())