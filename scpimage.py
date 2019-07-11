# #!/usr/bin/env python

# import serial
# import time
# import os
# import glob

# try:
#     # QRID_SPOTID_yyyymmddhhmmss.jpg
#     images_dir = os.path.abspath('./images/')
#     backup_dir = os.path.abspath('./backup/')

#     files = os.listdir(images_dir)
#     ret_files = []
#     for file in files:
#         image_file_path = images_dir + "/" + file
#         backup_file_path = backup_dir + "/" + file

#         res = os.system('sshpass -p "XXXXXXXXXXXx" scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null %s root@ferry-sunflower.ga:/usr/share/nginx/html/image/' % image_file_path)

#         if (res):
#             res = os.system('mv %s %s' % (image_file_path, backup_file_path))

# except:
#     print "Error"
