## Docker
```docker run -v ${PWD}/etc:/opt/splunk/etc -p 9998:9998 -p 8000:8000 \
-e SPLUNK_START_ARGS=--accept-license \
-e SPLUNK_PASSWORD='Splunking!' \
splunk/splunk```

## Splunk
- http://localhost:8000/en-US/app/podcastindex-splunk-app/search?q=%7C%20podcastindexsearch%20keyword%3D%22bad%20blood%22&display.page.search.mode=smart&dispatch.sample_ratio=1&workload_pool=&earliest=-24h%40h&latest=now&sid=1647241537.16
- 
### Debug
- Could not locate the time (_time) field on some results returned from the external search command 'podcastindexsearch'.
- Look at errors http://localhost:8000/en-US/app/podcastindex-splunk-app/search?q=search%20index%3D%22_internal%22%20No%20module%20named%20podcastindex&display.page.search.mode=smart&dispatch.sample_ratio=1&workload_pool=&earliest=-24h%40h&latest=now&sid=1647225560.15
- /Users/ttam/Library/Python/3.8//bin/splunk-appinspect inspect podcastindex-splunk-app.spl
- find /Users/ttam/Library/Python/3.8/ -name splunk-appinspect -print
- /opt/splunk/bin/splunk package app podcastindex-splunk-app
## Changelog

- Mar 13, 2022 - 10:30PM HST - submitted app to Splunkbase https://splunkbase.splunk.com/app/6342/edit/#/hosting
