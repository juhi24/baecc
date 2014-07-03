# -*- coding: utf-8 -*-
"""
@author: Jussi Tiira
"""
import time
import glob
import pandas as pd
from collections import defaultdict

def hotplate(date):
    #file_ = open(filename)
    date_str = time.strftime("%Y%m%d",date)
    files = glob.glob("../data/Hotplate/hot_plate_100901_"+date_str+"*")
    
    data=defaultdict(list)

    #descriptin of file
    file_format = {
    1: 'Output format',
    2: 'Fault indicator',
    3: 'Unix timestamp',
    4: 'Voltage, sensor, instantaneous (V)',
    5: 'Voltage, reference, instantaneous (V)',
    6: 'Current, sensor, instantaneous (A)',
    7: 'Current, reference, instantaneous (A)',
    8: 'Resistance, sensor, ratio of previous fields (ohm)',
    9: 'Resistance, reference, ratio of previous fields (ohm)',
    10: 'Power, sensor, 1-minute running average, 1 Hz samples (W)',
    11: 'Power, reference, 1-minute running averag    file_ = open(filename)e, 1 Hz samples (W)',
    12: 'Control effort (PWM), sensor, instantaneous (%)',
    13: 'Control effort (PWM), reference, instantaneous (%)',
    14:'Ambient temperature, 1-minute running ave. 1Hz samples (degC)',
    15: 'Enclosure temperature, 1-minute running ave. 1Hz samples (degC)',
    16: 'Solar IR sensor temperature, 1-minute running ave. 1Hz samples (degC)',
    17: 'Solar radiation, 1-minute ave., 1Hz samples (Wm-2)',
    18: 'Net IR radiation ground to sky, 1-minute running ave., 1 Hz samples (Wm-2)',
    19: 'Barometric pressure, referenced to sea level (mbar)',
    20: 'Temperature of humidity sensor (degC)',
    21: 'Relative humidity (%)',
    22: 'Wind speed, 1- minute running ave, 1 Hz samples (m s)',
    23: 'Collection efficiency, 1-minute running ave, 1Hz samples (W)',
    24: 'Power offset, 1-minute running ave., 1Hz samples (W)',
    25: 'Power offset due to radiation effects, 1Hz samples (W)',
    26: 'Raw precip. rate, 1-minute running ave, 1import os.path Hz samples (mm hr)',
    27: 'Power, sensor, 5-minute running average, 1 minute samples (W)',
    28: 'Power, reference, 5-minute running average, 1 minute samples (W)',
    29: 'delta Power, 5-minute running ave, 1 minute samples (W)',
    30: 'Ambient temperature, 5-minute running ave., 1 minute samples (degC)',
    31: 'Power offset, 5-minute ave., 1 minute samples (W)',
    32: 'Raw precip.rate, 5-minute running ave, 1 min. samples (mm hr)',
    33: 'Current precipitation rate (mm hr)',
    34: 'Total accumulated liquid precipitation (mm)'
     }

    for filename in files:
        file_ = open(filename)
        lines = file_.readlines()
        file_.close
        time_ = []
        for i in lines:
            var = i.split(',')
            if len(var) > 36:
                time_tmp = time.strptime(var[0],'%Y%m%d%H%M%S')
                time_tmp = time.mktime(time_tmp)
                firmware = var[2]
                dev_num = var[1]
                
                data['hotplate_time'].append(time_tmp)
                data['hotplate_firmware'].append(firmware)
                data['hotpalte_devnum'].append(dev_num)
                
                for key,value in file_format.iteritems():
                    data["hotplate_"+value].append(var[key+2])
            
    return pd.DataFrame(data,columns=data.keys())

def jenoptik(date):
    date_str = time.strftime("%Y%m%d",date)
    files = glob.glob("../data/Jenoptik/"+date_str+"*")
    snow = []
    time_ = []
    signal=[]
    temp = []
    for filename in files:
        file_ = open(filename)
        lines = file_.readlines()
        file_.close
        for i in lines:
            var = i.split(',')
            if len(var) > 0:
                time_tmp = time.strptime(var[0],'%Y-%m-%d %H:%M:%S')
                time_tmp = time.mktime(time_tmp)
                time_.append(time_tmp)
                snow.append(float(var[1])-0.034)
                signal.append(float(var[2]))
                temp.append(float(var[3]))
    #print acc
    d = {'jenoptik_time' : time_, 'jenoptik_snow_depth': snow,'jenoptik_signal_strength':signal,'jenoptik_temperature':temp}
    return pd.DataFrame(d)

def pluvio(date):
    """DEPRECATED"""
    date_str = time.strftime("%Y%m%d",date)
    files = glob.glob("../data/Pluvio200/pluvio200_02_"+date_str+"*")
    data=defaultdict(list)


    file_format = {
    2: 'Intensity RT  [mm h]',
    3: 'Accumulated RT NRT [mm]',
    4: 'Accumulated NRT [mm]',
    5: 'Accumulated total NRT [mm]',
    6: 'Bucket RT [mm]',
    7: 'Bucket NRT [mm]',
    8: 'Temperature load cell [degC]',
    9: 'Heating status',
    10: 'Status',
    11: 'Temperature electronics unit',
    12: 'Supply Voltage',
    13: 'Temperature orfice ring rim'
    }

    for filename in files:
        file_ = open(filename)
        lines = file_.readlines()
        file_.close
        time_ = []
        for i in lines:
            var = i.split(';')
            if len(var) > 3:
                time_tmp = time.strptime(var[0],'%Y%m%d%H%M%S')
                time_tmp = time.mktime(time_tmp)
                data['pluvio_time'].append(time_tmp)
                print(len(var))
                for key,value in file_format.iteritems():
                    data['pluvio '+value].append(var[key-1])
            
    #data["pluvio_time"] = time_
    #print len(data['status'])
    return pd.DataFrame(data)