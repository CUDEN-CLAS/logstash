logstash
========

Logstash config files

The contents of this repo shoudl live in /etc/logstash on a Ubuntu server.

Contents of crontab -e:

    # m h  dom mon dow   command
    * * * * * sh /home/ecorson/crons/gatherer

The gatherer script assumes passwordless ssh to the web servers as the dplagnt user. Logs are scp'ed to /data/logs.

Notes for dev and testing:
--------------------------

 - There are two things to be aware of if you want to clear logstash for testing.
    1. ElasticSearch stores the data.  So you will need to clear ES.
    2. Logstash remembers where it left off in a logfile using hte sincedb. so you need to clear the sincedb or logstash won't reparse older lgofiles after emptying ES.

To clear ES (from the logstash server cmd line):

    curl -XDELETE localhost:9200/logstash-*
    
To clear the sincedb:

    rm ~/.sincedb_* # for sincedbs crated form command line
    rm /var/lib/logstash/.sincedb_* #for sincedbs created by daemon

Troubleshooting
---------------

If you need to test a new config on wlogstash without breaking the running config:

    /opt/logstash/bin/logstash agent -f /etc/logstash/conf.d --configtest

If logstash-web service doesn;t stop with sudo service logstash stop:

    change /etc/init/logstash-web.conf
    change the next line:
    start on virtual-filesystems -> start on never
