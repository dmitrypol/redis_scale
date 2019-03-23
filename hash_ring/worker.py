#!/usr/bin/env python3
import uuid
import redis
from random import uniform
from uhashring import HashRing


if __name__ == '__main__':
    nodes = {
        'node1': {
            'instance': redis.Redis(host='hash_ring_redis_1'),
        },
        'node2': {
            'instance': redis.Redis(host='hash_ring_redis_2'),
        },
        'node3': {
            'instance': redis.Redis(host='hash_ring_redis_3'),
        }
    }
    hr = HashRing(nodes)
    while True:
        unique_user_id = str(uuid.uuid4())
        coordinates = {'lon':uniform(-180,180), 'lat':uniform(-90,90)}
        hr[unique_user_id].hmset(unique_user_id, coordinates)
        hr[unique_user_id].expire(unique_user_id, 60)
