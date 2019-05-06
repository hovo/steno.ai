import redis
r = redis.Redis(host='localhost', port=6379, db=0)

def cache_metadata(key, val):
    """
    Stores audio metadata in Redis
    Parametrs
    ---------
    key
        string: UUID which uniquely identifies the metadata
    
    val
        string: serialized object containing the audio file metadata
    """
    r.set(key, val)

def get_file_metadata(key):
     """
    Returns the metadata from Redis
    Parametrs
    ---------
    key
        string: UUID which uniquely identifies the metadata
    """
    return r.get(key)