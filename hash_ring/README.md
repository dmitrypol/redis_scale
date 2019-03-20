docker-compose up --build -d --scale redis=3

docker exec -it hash_ring_redis_1 redis-cli dbsize