# -*- coding:utf-8 -*-

# 图片和该脚本放在一个文件夹内启动

import os
from PIL import Image

list = os.listdir()

for i in list:
    if i.find('.py') == -1:
        try:
            print('开始处理 ' + i)
            img = Image.open(i).convert('RGBA')
            if img.size[0] == img.size[1]:
                img.resize((512, 512)).save(i[:i.find('.')] + '.png')
            else:
                basemap = Image.new(mode='RGBA', size=(512, 512))
                if img.size[0] > img.size[1]:
                    adjustHigh = 512 * img.size[1] / img.size[0]
                    basemap.paste(img.resize((512, int(adjustHigh))),
                                (0, int((512 - adjustHigh) / 2)),
                                img.resize((512, int(adjustHigh))))
                else:
                    adjustWidth = 512 * img.size[0] / img.size[1]
                    basemap.paste(img.resize((int(adjustWidth), 512)),
                                (int((512 - adjustWidth) / 2), 0),
                                img.resize((int(adjustWidth), 512)))
                basemap.save(i[:i.find('.')] + '.png')
        except:
            print(i + ' 出错')


