#!/usr/bin/env python

import serial
import time
from urlparse import urlparse
import os
import subprocess
import datetime

TARGET_DOMAIN = 'ferry-sunflower.ga'
LOCAL_SERVER = 'http://localhost:8000/'

# def main():
con=serial.Serial('/dev/ttyUSB0', 115200, timeout=10)
# con=serial.Serial('/dev/serial/by-path/platform-3f980000.usb-usb-0:1.2:1.0-port0', 9600, timeout=10)
# con=serial.Serial('/dev/ttyAMA0', 19200, timeout=10)
print con.portstr
child_pid = None

while 1:
    str=con.readline()
    try:
        if (str):
            str = str.strip()
            str = str.replace("\x02","")
            o = urlparse(str)
            if (len(o.scheme) > 0 and o.netloc == TARGET_DOMAIN):

                # kill chrome
                # os.system("pkill -KILL -f google-chrome")
                os.system("pkill -KILL google-chrome")

                # delete photo file name
                photoname_dir = os.path.abspath('./photo_name/')
                files = os.listdir(photoname_dir)
                for file in files:
                    photoname_file_path = photoname_dir + "/" + file
                    os.remove(photoname_file_path)

                # get info from URL
                fragment = o.fragment.split("/")
                spot_id = fragment[1]
                qr_id = fragment[2].replace("?qrid=","")
                local_url = LOCAL_SERVER + spot_id + ".html"

                try:
                    # open chrome
                    cmd = "sh ./show_chrome.sh " + local_url + " " + spot_id
                    res = subprocess.check_call(cmd.split())

                    # save photo file name
                    image_file_name = "%s_%s_%s.jpg" % (qr_id, spot_id, datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
                    print image_file_name
                    print './photo_name/' + image_file_name
                    f = open('./photo_name/' + image_file_name ,'w')
                    f.write('hoge\n')
                    f.close()

                except subprocess.CalledProcessError as e:
                    print e.returncode
                    print e.cmd
                    print e.output
            else:
                print "invalid url"
    except:
        print "Error"

    con.write(str)

#if __name__ == '__main__':

#    main()``

