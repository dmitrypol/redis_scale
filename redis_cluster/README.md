# start Redis and create cluster
./start.sh

redis-cli --cluster create 127.0.0.1:7000 127.0.0.1:7001 127.0.0.1:7002 127.0.0.1:7003 127.0.0.1:7004 127.0.0.1:7005 --cluster-replicas 1

# run local Python 

```
pipenv install --dev
pipenv shell
python web.py
```

# various commands

redis-cli -p 7000 cluster info

redis-cli -p 7000 cluster nodes

redis-cli -p 7000 cluster failover

redis-cli -p 7000 debug segfault

redis-cli --cluster check 127.0.0.1:7000

redis-cli --cluster add-node 127.0.0.1:7006 127.0.0.1:7000

redis-cli --cluster add-node 127.0.0.1:7007 127.0.0.1:7000 --cluster-slave --cluster-master-id node-id

redis-cli --cluster reshard 127.0.0.1:7000

redis-cli --cluster del-node 127.0.0.1:7000 node-id
