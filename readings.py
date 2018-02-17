#For OctaCore Processor

import numpy as np 
import matplotlib 

matplotlib.use('Agg')

import matplotlib.pyplot as plt 
import time

F = [[]for i in range(8)]
T = [[]for i in range(8)]


for i in range(8) :
	duration = 0.5
	start = time.time()
	while time.time() < start + duration :
		f = np.loadtxt('/sys/devices/system/cpu/cpu'+str(i)+'/cpufreq/scaling_cur_freq')
		t = np.loadtxt('/sys/devices/platform/coretemp.0/hwmon/hwmon1/temp'+str(i+1)+'_input')
		x = (f.astype(int)).tolist()
		y = (t.astype(int)).tolist()
		F[i].append(x/1000)
		T[i].append(y/1000)
		time.sleep(0.001)
	

for i in range(8) :
	plt.plot(F[i],T[i],label = 'Core-'+str(i+1))

plt.xlabel('frequency(1:1000)')
plt.ylabel('temperature(1:1000)')
plt.legend()

plt.savefig('Cores.png')

