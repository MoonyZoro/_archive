import matplotlib.pyplot as plt

import numpy as np

dt = 0.001

n_steps = 10000

x1 = np.zeros((n_steps))

y1 = np.zeros((n_steps))

vx1 = np.zeros((n_steps))

vy1 = np.zeros((n_steps))

x2 = np.zeros((n_steps))

y2 = np.zeros((n_steps))

vx2 = np.zeros((n_steps))

vy2 = np.zeros((n_steps))

x3 = np.zeros((n_steps))

y3 = np.zeros((n_steps))

vx3 = np.zeros((n_steps))

vy3 = np.zeros((n_steps))

m1 = 11.004

m2 = 10

m3 = 9

x1[0] = 3

y1[0]=0

x2[0] = 0

y2[0] = 2

vx1[0] = 0

vx2[0] = 0

x3[0] = 0

y3[0] = -1

vx3[0] = 0

for s in np.arange (1, n_steps):

    r12 = ((x1[s-1]-x2[s-1])**2 + (y1[s-1]-y2[s-1])**2)

    f12 = m1*m2/(r12* np.sqrt(r12))

    r13 = ((x1[s-1]-x3[s-1])**2 + (y1[s-1]-y3[s-1])**2)

    f13 = m1*m3/(r13* np.sqrt(r13))

    r23 = ((x2[s-1]-x3[s-1])**2+(y2[s-1]-y3[s-1])**2)

    f23 =  m2*m3/(r23* np.sqrt(r23))

    ax1 = (f12* (x2[s-1]-x1[s-1]) +f13* (x3[s-1]-x1[s-1])) /m1

    ay1 = (f12* (y2[s-1]-y1[s-1]) + f13* (y3[s-1]-y1[s-1]))/m1

    ax2 = (f12* (x1[s-1]-x2[s-1]) + f23* (x3[s-1]-x2[s-1])) /m2

    ay2 = (f12* (y1[s-1]-y2[s-1]) + f23* (y3[s-1]-y2[s-1])) /m2

    ax3 = (f13* (x1[s-1]-x3[s-1]) +f23* (x2[s-1]-x3[s-1])) / m3

    ay3 = (f13* (y1[s-1]-y3[s-1]) + f23* (y2[s-1]-y3[s-1])) / m3

    vx1[s] = vx1[s-1] + ax1*dt

    vy1[s] = vy1[s-1] + ay1*dt

    vx2[s] = vx2[s-1] + ax2*dt

    vy2[s] = vy2[s-1] + ay2*dt

    vx3[s] = vx3[s-1] + ax3*dt

    vy3[s] = vy3[s-1] + ay3*dt

    x1[s] = x1[s-1] + vx1[s]*dt

    y1[s] = y1[s-1] + vy1[s]*dt

    x2[s] = x2[s-1] + vx2[s]*dt

    y2[s] = y2[s-1] + vy2[s]*dt

    x3[s] = x3[s-1] + vx3[s]*dt

    y3[s] = y3[s-1] + vy3[s]*dt

fig, ax = plt.subplots()

ax.plot(x1, y1)

ax.plot(x2, y2)

ax.plot(x3, y3)

plt.show()