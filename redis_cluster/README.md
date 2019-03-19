honcho start

redis-cli --cluster create 127.0.0.1:7000 127.0.0.1:7001 127.0.0.1:7002 127.0.0.1:7003 127.0.0.1:7004 127.0.0.1:7005 --cluster-replicas 1

python worker.py

https://willwarren.com/2017/10/redis-cluster-cheatsheet/#adding-new-masters-to-an-existing-cluster