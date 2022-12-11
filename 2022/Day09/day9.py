from itertools import accumulate

sign = lambda x: 1 if x > 0 else (-1 if x < 0 else 0)

def follower(headpath):
    tail_pos = [0]
    for hp in headpath:
        distvec = hp-tail_pos[-1]
        if abs(distvec.real) > 1 or abs(distvec.imag) > 1:
            tail_pos.append(tail_pos[-1]+sign(distvec.real)+1j*sign(distvec.imag))
        else:
            tail_pos.append(tail_pos[-1])
    return tail_pos[1:]

# Create head position list
with open('input.txt') as fid:
    data = [x.strip() for x in fid.readlines()]
steps = [x.split() for x in  data]
directions = {'U': 1j, 'D': -1j, 'L': -1,'R':1}

head_pos = [0,] + list(accumulate([directions[x] for x,y in steps for _ in range(int(y))]))

# Part 1
print(len(set(follower(head_pos))))

# Part 2
paths = [head_pos]
new_path = head_pos
for _ in range(9):
    new_path = follower(new_path)
    paths.append(new_path)

print(len(set(new_path)))

import sys
sys.exit()

# visualization
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

xx = []
yy = []
for ii in range(11452):
    xx.append([x[ii].real for x in paths])
    yy.append([x[ii].imag for x in paths])

xx = np.array(xx)
yy = np.array(yy)


fig,ax = plt.subplots(facecolor='lightgray')
dots, = ax.plot(xx[0],yy[0],linewidth=3,label='Rope')
ax.set_xlim(-10,400)
ax.set_ylim(-200,100)
plt.plot([x.real for x in paths[0]], [y.imag for y in paths[0]],alpha=0.2,color='blue',label='Rope head path')
plt.grid()
plt.legend()
#plt.axis('off')
ax.set_title('Advent of Code 2022, Day 9, Part 2')
ax.set_xlabel('$\mathscr{Re}$')
ax.set_ylabel('$\mathcal{Im}$')

def animate(i):
    global xx, yy
    dots.set_xdata(xx[i])
    dots.set_ydata(yy[i])
    return dots

ani = animation.FuncAnimation(fig, animate, frames=range(0000,11452), interval=33)
ani.save('aoc_day9_2.mp4')


