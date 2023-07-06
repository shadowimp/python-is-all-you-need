```python
import hashlib

hash_obj = hashlib.md5()

hash_obj.update("string".encode('utf-8'))

res_hash=hash_obj.hexdigest()

```

