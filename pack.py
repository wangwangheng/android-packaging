__author__ = 'jie'

import zipfile
import shutil
import sys
import os
# channels = ['xiaomi', 'baidu', 'm360', 'm91']



apk_path = sys.argv[1]
out_path = sys.argv[2]
if not os.path.exists(out_path):
    os.mkdir(out_path)

name = os.path.basename(apk_path)
apk_name = name[:len(name) - 4] + "_{}.apk"


file = open('channels.txt')
for channel in file:
    channel_apk_name = (out_path + '/' + apk_name).format(channel.strip())
    shutil.copy2(apk_path, channel_apk_name)
    zipped = zipfile.ZipFile(channel_apk_name, 'a', zipfile.ZIP_DEFLATED)
    empty_channel_file = "META-INF/gmchannel_{}".format(channel)
    zipped.writestr(empty_channel_file, '')
    zipped.close()


