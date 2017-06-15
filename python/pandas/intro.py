'''simple first pandas file'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#plt.style.use('ggplot')

wsmdf = pd.read_csv('mywsm.csv')
culldf = wsmdf[ wsmdf['Pres(kPa)'] < 1500 ]
press = wsmdf['Pres(kPa)']


plt.figure()
culldf['AccelX(g)'].plot()
culldf['AccelY(g)'].plot()
plt.show()
