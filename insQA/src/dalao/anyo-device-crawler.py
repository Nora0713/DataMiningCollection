# 来自阿姚的code
# !/usr/bin/python
import datetime
import json
import os
import os.path
import sqlite3
import threading
import time
# from concurrent.futures import ThreadPoolExecutor

# import numpy as np
# import pandas as pd
import requests
import io
import sys
import urllib


class Crawler:

    def __init__(self):
        self.device_list = "/home/jjyao/anyo/devices/anyo.station.list.shanghai.nonempty"
        self.data_dir = "/home/jjyao/anyo/devices/"
        self.url_station_get = "http://app.anyocharging.com:8981/api/v2/station/station/get"
        self.url_station_search = "http://app.anyocharging.com:8981/api/v2/station/station/search"
        self.url_device_search = "http://app.anyocharging.com:8981/api/v2/station/device/search"
        self.headers_anyo = {
            'r': '1509712840967',
            'Accept-Language': 'zh-CN;q=0.8',
            'Accept-Encoding': 'gzip',
            'VERSIONID': '3.3.1',
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
            'User-Agent': 'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; GT-I9508 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
            'Connection': 'keep-alive',
        }
        self.auth_anyo = requests.auth.HTTPBasicAuth('ANDROID.anyoee.com', 'f914750620613e503b3af11360cca65a')

    def get_device(self, station_id, offset=0, limit=10):
        # wt = io.open('./ay.rt','w',encoding='utf8')
        device_info = " "
        try:

            # ------search---
            # params = {
            # 'station_id':'10788',
            # 'offset':'0',
            # 'limit':'10',
            # }
            # -------search ----
            # params={
            #   "status" : "usable",
            #   "latitude" : 31.228462621707109,
            #   "longitude" : 121.40886026121109,
            #   "charge_type" : "both"
            # }
            # ------get ---
            # params={
            #     'id':'10788'
            # }
            # params = urllib.pathname2url(json.dumps(params))
            # print params
            # params = "data="+ params
            # print params  
            params = "station_id=%s&offset=%s&limit=%s" % (station_id, offset, limit)
            self.headers_anyo['Content-Length'] = str(len(params))

            response = requests.post(self.url_device_search, headers=self.headers_anyo, data=params,
                                     auth=self.auth_anyo)
            # print ("status: %s" % response.status_code)
            device_info = response.text

        except Exception as ex:
            print(ex)
        finally:
            # wt.close()
            return device_info

    def collect_devices(self):
        station_dict = {}
        with open(self.device_list) as rd:
            for line in rd:
                (station_id, device_count) = line.rstrip().split('\t')
                station_dict[station_id] = int(device_count)
        # print "station count:", len(station_dict)
        curr = datetime.datetime.now()
        out_path = "%sanyo.device.%s-%s-%s-%s" % (
            self.data_dir, curr.year, curr.month, curr.day, curr.hour)
        output = open(out_path, 'w')
        for (station_id, device_count) in station_dict.items():
            now = datetime.datetime.now()
            # print "%s : %s : %s" % (now,station_id, device_count)
            if device_count <= 10:
                time.sleep(2)
                device_info = self.get_device(station_id)
                output.write("%s\t%s\t%s\n" % (station_id, now, device_info))
                continue
            for step in range(0, device_count / 10):
                # print "step:",step
                time.sleep(2)
                device_info = self.get_device(station_id, step * 10, 10)
                output.write("%s\t%s\t%s\n" % (station_id, now, device_info))
            if device_count % 10 != 0:
                device_info = self.get_device(station_id, device_count / 10 * 10, 10)
                output.write("%s\t%s\t%s\n" % (station_id, now, device_info))
        output.close()

    def collect_station_descrp(self, in_path, out_path):
        output = open(out_path, 'w')
        with open(in_path) as rd:
            for line in rd:
                (opId, stationId, stationType, addr, lat, lont) = line.split('\t')
                print("fetch station...%s" % stationId)
                time.sleep(2)
                descrp = self.get_station(stationId)
                print(descrp)
                output.write(descrp)
                output.write('\n')
        output.close()

    def enumerate_station_descrp(self, out_path):
        output = open(out_path, 'w')
        for stationId in range(10000, 9000, -1):
            print("fetch station...%s" % stationId)
            time.sleep(2)
            descrp = self.get_station(stationId)
            if descrp is None:
                output.write("%s\t\n")
                continue
            output.write(descrp)
            output.write('\n')
        output.close()


if __name__ == "__main__":
    cr = Crawler()
    # cr.collect_station_descrp(sys.argv[1],sys.argv[2])
    # print (cr.get_device(10730,0,10))
    cr.collect_devices()
    # print cr.get_device(10511,30,10)
