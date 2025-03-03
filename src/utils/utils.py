import hashlib

def sha256sum(filename):
    sha256_hasher  = hashlib.sha256()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f:
        while n := f.readinto(mv):
            sha256_hasher.update(mv[:n])
    return sha256_hasher.hexdigest()
