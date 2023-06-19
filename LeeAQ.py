#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt




dir='/home/kintxo/SAGA_2023/SAGA/SAGA2023/RecuperacionFondeoSAGA/Datos/Aquadop/DatosHorarios/'
number='360401'

# Order of variables below is given in *hdr file
nams=['Month','Day','Year','Hour','Minute','Second','Error Code','Status Code','vel_x','vel_y','vel_z','counts_x','counts_y','counts_z','battery','soundspeed','soundspeed_used','heading','pitch','roll','pressure_db','pressure_m','temperature','analog_1','analog_2','speed','direction']
      
def main():

    df=pd.read_csv(dir+number+'.dat', names=nams,delim_whitespace=True)
    time=pd.to_datetime(df.iloc[:, [2,0,1,3,4,5]])
     # select time section
    it0=1000; it1=25000; inc=1
    plt.figure(figsize=(15,6))

    plt.plot(time[it0:it1:inc],df['vel_x'][it0:it1:inc].values,label='u')
    plt.plot(time[it0:it1:inc],df['vel_y'][it0:it1:inc].values,label='v')
    #plt.plot(time[it0:it1:inc],df['vel_z'][it0:it1:inc].values,label='w')
    plt.legend()

    plt.xticks(rotation=60)
    plt.show()
if __name__ == '__main__':
    main()
