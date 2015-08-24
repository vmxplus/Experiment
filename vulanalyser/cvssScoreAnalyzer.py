import numpy as np
from scipy import stats
list=[1,2,3,4,5,6,7,8,9,10]
print np.mean(np.array(list));
print np.min(np.array(list));
print np.max(np.array(list));
narray=np.array(list);

print round(stats.scoreatpercentile(narray,25),1)