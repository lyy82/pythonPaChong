
proxies_pool = [
    {'http':'60.250.159.191:4598223'},
    {'http':'60.250.159.191:4511983'},
]

import random

proxies = random.choice(proxies_pool)

print(proxies)