#!/bin/bash
set -e

function run()
{
  echo "Running: $@"
  "$@"
}

CONSUMER_SERVERS=( "52.77.231.141" "52.221.227.146" "52.77.227.207" "54.169.1.234" "54.169.52.71" "54.169.169.192" "54.179.145.34" "54.179.154.29" )
for CONSUMER_SERVER in "${CONSUMER_SERVERS[@]}"
do
    	run ssh ubuntu@$CONSUMER_SERVER "pkill -INT -f celery;"
done

CONSUMER_SERVERS=( "52.77.231.141" "52.221.227.146" )
for CONSUMER_SERVER in "${CONSUMER_SERVERS[@]}"
do
    	run ssh ubuntu@$CONSUMER_SERVER "cd /home/ubuntu/balodis;celery worker -A balodis -Q validation --pidfile=validation.pid --detach"
done

CONSUMER_SERVERS=( "52.77.227.207" "54.169.1.234" "54.169.52.71" "54.169.169.192" "54.179.145.34" "54.179.154.29" )
for CONSUMER_SERVER in "${CONSUMER_SERVERS[@]}"
do
    	run ssh ubuntu@$CONSUMER_SERVER "cd /home/ubuntu/balodis;celery worker -A balodis --pidfile=celeryd.pid --detach"
done


CONSUMER_SERVERS=( "52.77.231.141" "52.221.227.146" "52.77.227.207" "54.169.1.234" "54.169.52.71" "54.169.169.192" "54.179.145.34" "54.179.154.29" )
for CONSUMER_SERVER in "${CONSUMER_SERVERS[@]}"
do
    	run ssh ubuntu@$CONSUMER_SERVER "ps aux | grep celery;"
done

