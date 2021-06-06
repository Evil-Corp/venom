target='70850eb4b48f818748dcd214f17559e2'

from hashlib import md5
import concurrent.futures

for x in range(1749817193):
    y=md5(str(x).encode()).hexdigest()
    print(f"{x} => {y}")
    if y==target:
        print("TARGET FOUND")
        break
a=input()