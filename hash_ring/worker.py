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
        value = {'lon':uniform(-180,180), 'lat':uniform(-90,90)}
        #   
        hash_tag = ''
        unique_id = str(uuid.uuid4())
        key = hash_tag + unique_id
        if hash_tag:
            hr_hint = hash_tag
        else:
            hr_hint = key
        #   
        hr[hr_hint].hmset(key, value)
        hr[hr_hint].expire(key, 60)
