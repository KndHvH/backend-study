import json
import redis

class RedisClient:
    def __init__(self):
        self.client = redis.Redis(
            host="redis",
            port=6379,
            db=0,
            decode_responses=True
        )

    def get_client(self):
        return self.client

class RedisCache:
    def __init__(self):
        self.redis_client = RedisClient().get_client()

    def get(self, key):
        data = self.redis_client.get(key)
        return json.loads(data) if data else None

    def set_cache(self, key: str, value: dict, ttl: int = 60):
        self.redis_client.setex(key, ttl, json.dumps(value))

    def delete(self, key):
        self.redis_client.delete(key)
        
redis_cache = RedisCache()