#!/usr/bin/env python3
import os
import uuid
import redis
from random import uniform


if __name__ == '__main__':
    r = redis.Redis(host=os.environ['REDIS_HOST'], port=os.environ['REDIS_PORT'])
    pipe = r.pipeline(transaction=False)
    while True:
        hash_tag = '{}'
        unique_user_id = hash_tag + str(uuid.uuid4())
        coordinates = {'lon':uniform(-180,180), 'lat':uniform(-90,90)}
        pipe.hmset(unique_user_id, coordinates)
        pipe.expire(unique_user_id, 60)
        pipe.execute()
