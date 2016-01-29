# Logstash
The contents of this repo should live in /etc/logstash on a server.

Logs are sorted into three groups. The goal is to reduce 'Noise' to 0.
* Signal - Events that resulted from abnormal operations
* Interference - Events that resulted from normal operations
* Noise - Events that our code produces but shouldn't

### File naming - Files are aggregated in alpha order.
* 1* files are for input.
* 2* files are for preprocessing
* 3* files are for filtering Drupal log types (only type per config file).
* 4*-5* files are for filtering other log types (only type per config file).
* 7* files are for cleaning up the fields
* 8* files are for dropping events that we do not need.
* 9* files are for outputs.

## Commands
To clear Elasticseearch (from the logstash server command line):
```
curl -XDELETE localhost:9200/logstash-*
```

To clear the sincedb:
```
rm ~/.sincedb_* # for sincedbs crated form command line
rm /var/lib/logstash/.sincedb_* #for sincedbs created by daemon
```
## Troubleshooting
If you need to test a new config without breaking the running config:
```
/opt/logstash/bin/logstash agent -f /etc/logstash/conf.d --configtest
```
