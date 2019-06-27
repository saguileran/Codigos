#import matplotlib
#matplotlib.use('Agg')
#import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

#fig.savefig("test.png")
plt.show()

###Subplot
#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.plot([1,2,3])
#fig.savefig('test.png')

'''
#####Easiest exmaple#####
# Compute the x and y coordinates for points on a sine curve
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)
#plt.title("sine wave form")

# Plot the points using matplotlib
plt.plot(x, y)
plt.show()
'''
