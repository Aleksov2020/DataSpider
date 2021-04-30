import re
import time
import urllib.request as urllib2

import requests


def parsing(patch_to_data, patch_to_files, color_processing, normalization):
    url = patch_to_data
    content = str(urllib2.urlopen(url).read())
    imgUrls = re.findall('img .*?src="(.*?)"', content)
    for i in range(len(imgUrls)):
        if imgUrls[i][0] == '/':
            imgUrls[i] = patch_to_data + imgUrls[i]
    k = 0
    for img in imgUrls:
        k += 1
        p = requests.get(img)
        out = open(patch_to_files + '/img' + str(k) + '.jpg', 'wb')
        out.write(p.content)
        out.close()


parsing('https://www.google.com', 'D:/New folder (2)', 1, 1)
