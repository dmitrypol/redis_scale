#!/usr/bin/env python3
import os
import uuid
import time
from random import uniform
from rediscluster import StrictRedisCluster


startup_nodes = [{'host': 'localhost', 'port': '7000'}]
r = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)
pipe = r.pipeline(transaction=False)


def set_start_time():
    if not r.get('start_time'):
        r.set('start_time', time.time())
    

def set_keys():
    while True:
        hash_tag = ''
        unique_user_id = hash_tag + str(uuid.uuid4())
        coordinates = {'lon':uniform(-180,180), 'lat':uniform(-90,90)}
        pipe.hmset(unique_user_id, coordinates)
        pipe.expire(unique_user_id, 60)
        pipe.execute()


if __name__ == '__main__':
    set_start_time()
    set_keys()