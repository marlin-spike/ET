#practical no 7

#median
numb = [2, 4, 5, 8, 9]
no = len (numb)
numb. sort()
if no % 2 == 0:
    median1 = numb[no//2]
    median2 = numb[no//2 - 1]
    median = (median1 + median2)/2
else:
    median = numb[no//2]
print("The median of the given numbers (", numb, ") is", str (median))


------------------------------------------------------------------------

#practical no 7

#mean
numb = [2, 3, 5, 7, 8]
no = len(numb)

mean = sum(numb) / no
print("The mean of the given numbers is:", mean)

------------------------------------------------------------------------

#practical no 7
#mode
from collections import Counter

numb = [2, 3, 4, 5, 7, 2]
no = len(numb)
val = Counter(numb)
findMode = dict(val)
findMode = [i for i, V in findMode.items() if V == max(list(val.values()))]
if len(findMode) == no:
    findMode = "The group of number do not have any mode"
else:
    findMode = "The mode of a number is/are: " + ' '.join(map(str, findMode))
print(findMode)


-------------------------------------------------------------------------


#practical no 7

import statistics

mean = statistics.mean([5, 3, 6, 8, 9, 12, 5])

median = statistics.median([5, 3, 6, 8, 9, 12, 5])

mode = statistics.mode([5, 3, 6, 8, 9, 12, 5])

print("mean " )
print(mean)
print("median " )
print(median)
print("mode ")
print(mode)



