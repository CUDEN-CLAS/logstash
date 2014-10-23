logstash
========

Logstash config files

The contents of this repo shoudl live in /etc/logstash on a Ubuntu server.

Contents of crontab -e:

    # m h  dom mon dow   command
    * * * * * sh /home/ecorson/crons/gatherer

The gatherer script assumes passwordless ssh to the web servers as the dplagnt user. Logs are scp'ed to /data/logs.

Notes for dev and testing:

 - There are two things to be aware of if you want to clear logstash for testing.
    1. ElasticSearch stores the data.  So you will need to clear ES.
    2. Logstash remembers where it left off in a logfile using hte sincedb. so you need to clear the sincedb or logstash won't reparse older lgofiles after emptying ES.

To clear ES (from the logstash server cmd line):

    curl -XDELETE localhost:9200/logstash-*
    
To clear the sincedb:

    rm ~/.sincedb_*
