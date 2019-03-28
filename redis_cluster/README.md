honcho start

redis-cli --cluster create 127.0.0.1:7000 127.0.0.1:7001 127.0.0.1:7002 127.0.0.1:7003 127.0.0.1:7004 127.0.0.1:7005 --cluster-replicas 1

./web.py

http://localhost:5000/

./worker.py

redis-cli -p 7000 cluster info

rm -f 700*/nodes.conf 700*/dump.rdb 700*/appendonly.aof

pkill -f redis-server