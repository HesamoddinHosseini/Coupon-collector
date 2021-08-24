import sys
import random
n = int(sys.argv[2])

count=0
collected_count=0
is_collected_count=[false]*n
while collected_count<n:
    count+=1
    value=random.range(0,n)
    if not is_collected[value]:
        collected_count+=1
        is_collected[value]=true
print(count)