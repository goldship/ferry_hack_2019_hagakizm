#!/usr/bin/env python

import serial
import time
from urlparse import urlparse
import os
import subprocess
import datetime


# def main():
con=serial.Serial('/dev/ttyUSB1', 115200, timeout=10)
# con=serial.Serial('/dev/serial/by-path/platform-3f980000.usb-usb-0:1.2:1.0-port0', 9600, timeout=10)
# con=serial.Serial('/dev/ttyAMA0', 19200, timeout=10)
print con.portstr

while 1:
    str=con.readline()
    try:
        if (str):
            str = str.strip()
            str = str.replace("\x02","")
            if (str == "shot"):

                # get photo file name
                photoname_dir = os.path.abspath('./photo_name/')
                files = os.listdir(photoname_dir)
                photo_file_name = ''
                for file in files:
                    photo_file_name = file
                    break

                if (photo_file_name):
                    
                    # save image
                    os.system("uvccapture -m -v -d/dev/video1 -o./images/%s" % photo_file_name)

                    # send image server
                    res = os.system('sshpass -p "XXXXXXXXXXXX" scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null ./images/%s root@ferry-sunflower.ga:/usr/share/nginx/html/image/' % photo_file_name)

                    # delete photoname file
                    os.remove(photoname_dir + "/" + photo_file_name)

                    #  create photoname file
                    buf = photo_file_name.split("_")
                    image_file_name = "%s_%s_%s.jpg" % (buf[0], buf[1], datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
                    f = open('./photo_name/' + image_file_name ,'w')
                    f.write('hoge\n')
                    f.close()

    except:
        print "Error"

    con.write(str)

#if __name__ == '__main__':

#    main()``

