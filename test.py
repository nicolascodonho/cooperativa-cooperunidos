import uuid
import random

print(uuid.uuid1().int)

print(len(str(9223372036854775807)))
print(len(str(38570671288765240564701377375925720633)))

random_id = random.getrandbits(64)

print(random_id)