#TEMPO
import emoji
from time import sleep

for c in range(10, 0, -1):
    print(c)
    if c == 3:
        break
    sleep (0.55)
print ('\33[1;32mBOOOM\33[m')

