docker-compose up --build -d --scale redis=3

http://localhost:8001/stats?usedonly&filter=redis.egress_redis.command

docker exec -it envoy_redis_1 redis-cli dbsize