# Commands

To download **rabbitmqadmin**, run

```bash
curl http://msg:15672/cli/rabbitmqadmin | tee rabbitmqadmin
chmod u+x rabbitmqadmin
```

To use **rabbitmqadmin** and delete problematic queens,

```bash
./rabbitmqadmin --user admin \
                --password ${password} \
                --host msg01 \
                --vhost /openstack \
                delete queue name=
```

## Delete Queues

```bash
#!/bin/bash
set -u

while getopts ":hH:p:u:P:r" opt; do
  case $opt in
    h )
      echo "h"
      exit 0
      ;;
    r )
      DRYRUN=1
      ;;
    H )
      HOST=${OPTARG}
      ;;
    p )
      PORT=${OPTARG}
      ;;
    u )
      USER=${OPTARG}
      ;;
    P )
      PASSWORD=${OPTARG}
      ;;
   esac
done

DRYRUN=${DRYRUN:-0}
HOST=${HOST:-10.151.174.83}
PORT=${PORT:-15672}
USER=${USER:-rabbitmq}
PASSWORD=${PASSWORD:-password}

CMD="./rabbitmqadmin --host ${HOST} --port ${PORT} --user ${USER} --password ${PASSWORD}"

vhosts=`${CMD} list vhosts -f tsv | awk 'NR>1 { print $1 }'`

for vhost in ${vhosts}; do
  echo "deleting vhost: $vhost"
  for i in `${CMD} --vhost ${vhost} -f tsv list queues name | awk 'NR>1 {print $1}'`; do

    if [ ${DRYRUN} -gt 0 ]; then
      ${CMD} --vhost ${vhost} delete queue name=$i
    else
      echo $i
    fi
  done
done
```