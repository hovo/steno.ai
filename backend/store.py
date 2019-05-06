import redis
r = redis.Redis(host='localhost', port=6379, db=0)

def cache_metadata(key, val):
    r.set(key, val)

