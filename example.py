from naff import *

# grab test data
dt = np.genfromtxt('testdata.csv')

# run naff
freq,amp = naff(dt)

print freq,amp
