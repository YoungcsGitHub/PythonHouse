import time

a = []
t0 = time.clock()
for i in range(1, 20000):
    a.append(i)
print(time.clock() - t0, 'Seconds process time')

t1 = time.clock()
b = [i for i in range(1, 20000)]
print(time.clock() - t1, 'Seconds process time')