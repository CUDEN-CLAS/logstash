logstash
========

Logstash config files

The contents of this repo shoudl live in /etc/logstash on a Ubuntu server.

Contents of crontab -e:

    # m h  dom mon dow   command
    * * * * * sh /home/ecorson/crons/gatherer

The gatherer script assumes passwordless ssh to the web servers as the dplagnt user. Logs are scp'ed to /data/logs.
