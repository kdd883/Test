import os
import time
import pandas as pd
import math
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

start_time = time.time()

fac = 0

testdata = [14, 33, 67, 45, 7, 11, 55, 54, 85, 34, 87, 19, 20, 34, 23, 8, 13, 11, 10, 74, 39, 7]
plt.plot(testdata)

print(f'ADF Results: {adfuller(testdata)}')

list = pd.Series(os.listdir("C:/users/kaushald/OneDrive - Sportsbet/Desktop/"))
print(f'Content of user directory --> {list[4], list[5]}')
print(f'Local time is {time.asctime(time.localtime(time.time()))}')

while fac <= 100:
    fac = fac + 1
#    print(f'{fac} Factorial is {math.factorial(fac)}')

#print(f'Square root of this Factorial is {math.sqrt(math.factorial(fac))}, {testdata[0]}')
#print("Square root of this Factorial is %d, %s" % (math.sqrt(math.factorial(fac)), testdata[1]))
#print("Square root of this Factorial is {0}, {1}".format(math.sqrt(math.factorial(fac)), testdata[5]))


end_time = time.time()

print(f'Elapsed time is ' + str(end_time - start_time))