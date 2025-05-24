import numpy as np
import matplotlib.pyplot as plt

#Plot font and colors
font = {'weight' : 'normal',
        'size'   : 13}

plt.rc('font', **font)
colors=['#1b9e77','#d95f02','#7570b3','#e7298a','#66a61e','#e6ab02']

npt = 1000
z = np.linspace(0, 1, npt)
u = np.zeros(npt)
epsilon = np.zeros(npt)
for i in range(npt):
    if z[i] < 0.33:
        u[i] = 1
        epsilon[i] = 1
    elif z[i] < 0.66:
        u[i] = 2 
        epsilon[i] = 0.5
    else:
        u[i] = 1
        epsilon[i] = 1

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(z, u, color=colors[0],label='$u_z$')
ax2.plot(z, epsilon,'--', color=colors[1],  label='$\\epsilon$')
ax1.set_ylim(0, 3)
ax1.set_xlabel('z')
ax1.set_ylabel('u', color=colors[0])
ax2.set_ylabel('$\\epsilon$', color=colors[1])
# We change the color of the y axis labels
ax1.tick_params('y', colors=colors[0])

# We change the color of the x axis labels
ax2.tick_params('y', colors=colors[1])
plt.savefig('../images/1d_flow.pdf')
plt.show()
