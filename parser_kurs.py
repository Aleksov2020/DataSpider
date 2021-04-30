import re
import urllib.request as urllib2
import requests
import time

def parsing(patch_to_data, patch_to_files, color_processing, normalization, stop_value):
    url = patch_to_data
    content = str(urllib2.urlopen(url).read())
    imgUrls = re.findall('img .*?src="(.*?)"', content)
    for i in range(len(imgUrls)):
        print(imgUrls[i])
        if imgUrls[i][0] == '/':
            imgUrls[i] = patch_to_data + imgUrls[i]
    k = 0
    for img in imgUrls:
        print(img)
        k += 1
        try:
            p = requests.get(img)
        except ConnectionError:
            continue
        except:
            continue
        out = open(patch_to_files + '/img' + str(k) + '.jpg', 'wb')
        out.write(p.content)
        out.close()
        if k % 5 == 0:
            time.sleep(3)
        if k > stop_value:
            break
    return 1
