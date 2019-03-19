#!/usr/bin/env python3
import os
import uuid
from random import uniform
from rediscluster import StrictRedisCluster

if __name__ == '__main__':
    startup_nodes = [{'host': 'localhost', 'port': '7000'}]
    r = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)
    pipe = r.pipeline(transaction=False)
    while True:
        unique_user_id = str(uuid.uuid4())
        coordinates = {'lon':uniform(-180,180), 'lat':uniform(-90,90)}
        # r.hmset(unique_user_id, coordinates)
        # r.expire(unique_user_id, 60)
        pipe.hmset(unique_user_id, coordinates)
        pipe.expire(unique_user_id, 60)
        pipe.execute()
