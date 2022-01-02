# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 23:19:14 2022

@author: khb16
"""

# 4. 히스토그램
import os
os.getcwd()
os.chdir("C:/Users/khb16/Desktop/code/DA/판다스_데이터분석")

import pandas as pd
import matplotlib.pyplot as plt

# 한글 폰트 오류 해결
from matplotlib import font_manager, rc
font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font',family=font_name)

plt.style.use('classic')
# 자동차 연비 데이터셋
df = pd.read_csv('auto-mpg.csv', header=None)
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model yaer','origin','name']
df['mpg'].plot(kind='hist',bins=10,color='coral',figsize=(10,5))
plt.title('Histogram')
plt.xlabel('mpg')
plt.show()