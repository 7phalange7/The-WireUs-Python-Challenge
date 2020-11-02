# challenge 45

import re

x = "abcd"
y = [match for size in range(1,len(x)+1) for match in re.findall('(?=(.{%d}))' % size, x)]

print(y)
