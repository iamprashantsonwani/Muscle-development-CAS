#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')
sns.set_context('talk')

from scipy.stats import t
import pyNetLogo


netlogo = pyNetLogo.NetLogoLink(gui=True)

netlogo.load_model('H:/ProjectCAS/Draft/Muscle_Development.nlogo')


netlogo.command('setup')
netlogo.command('set lift?'" "+str('true'))
netlogo.command('set intensity'" "+str(90))

netlogo.command('set hours-of-sleep'" "+str(8))
netlogo.command('set days-between-workouts'" "+str(3))
netlogo.command('set %-slow-twitch-fibers'" "+str(50))

netlogo.command('set inconsistency?'" "+str('true'))
netlogo.command('set inconsistencies-days-sleep'" "+str(20))

netlogo.command('setup')

musclemass = [] 
anabolicstat = []
catabolicstat = []
no_of_ticks = []

for i in range(3000): 
    try: 
        netlogo.command('go') 
        x1 = netlogo.report('muscle-mass') 
        musclemass.append(x1/100)

        y1 = netlogo.report('mean [catabolic-hormone] of patches')
        catabolicstat.append(y1)

        z1 = netlogo.report('mean [anabolic-hormone] of patches')
        anabolicstat.append(z1)

    except:
        x1 = 0
        musclemass.append(x1)
        y1 = 0
        anabolicstat.append(y1)
        z1 = 0
        catabolicstat.append(z1)
        
    no_of_ticks.append(i+1)
plt.plot(no_of_ticks,musclemass) 
plt.ylabel("Muscle mass")
plt.xlabel("No of Ticks") 
plt.title("Muscle development") 
plt.show()

plt.plot(no_of_ticks,catabolicstat) 
plt.ylabel("catabolic harmone")
plt.xlabel("No of Ticks") 
plt.title("catabolic") 
plt.show()

plt.plot(no_of_ticks,anabolicstat) 
plt.ylabel("anabolic harmone")
plt.xlabel("No of Ticks") 
plt.title("anabolic") 
plt.show()

#netlogo.kill_workspace()