# podcastindex-splunk-app
Splunk App to do analysis of Podcastindex.org data and perform real time queries

## SPL command
`| podcastindexsearch keyword=[podcast name]` - search using the Podcastindex.org data

## Building the app package
- `find . -name '*.pyc' -print -exec rm {} \; ; /opt/splunk/bin/splunk package app podcastindex-splunk-app && rm -f /opt/splunk/etc/apps/podcastindex-splunk-app/podcastindex-splunk-app.spl ; cp -f /opt/splunk/share/splunk/app_packages/podcastindex-splunk-app.spl /opt/splunk/etc/apps/podcastindex-splunk-app`
