#!/bin/bash
rm -f 700*/nodes.conf 700*/dump.rdb 700*/appendonly.aof 700*/redis.log
pkill -f redis-server
