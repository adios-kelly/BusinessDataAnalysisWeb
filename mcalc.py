from flask import Flask, render_template
from flask import request
import numpy as np


def m_simple_calc():
    data_min_value_tmp = -1.234
    
    if request.method == 'POST':  
        datatxt = request.form.get('datatxt') 
        data_list = []
        for x in datatxt.split(','):
            x = x.strip()
            x = float(x)
            data_list.append(x)
        print('data_list_input={0}'.format(data_list))
        data_min_value_tmp = min(data_list)
    return render_template('simple_calc.html', 
                            data_min_value=data_min_value_tmp)



def mstd(arr):
    return np.std(arr)

def m_std_calc():
    data_std_value_tmp = -1.234

    if request.method == 'POST':
        datatxt = request.form.get('datatxt')
        data_list = []
        for x in datatxt.split(','):
            x = x.strip()
            x = float(x)
            data_list.append(x)
        print('data_list_input={0}'.format(data_list))
        data_std_value_tmp = mstd(data_list)
    return render_template('std_calc.html',
                            data_std_value=data_std_value_tmp)
