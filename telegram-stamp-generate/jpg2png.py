# -*- coding:utf-8 -*-

# 图片和该脚本放在一个文件夹内启动
# 可以处理 .jpg 与 .png 批量转换为 Telegram 贴图格式

import os
from PIL import Image

list = os.listdir()

for i in list:
    suffix = i[i.rfind('.') + 1:]
    if suffix == 'jpg' or suffix == 'png':
        try:
            print('开始处理 ' + i)
            dir = './out'
            saveFileName = dir + '/' + i[:i.find('.')] + '.png'
            if not os.path.exists(dir):
                os.mkdir(dir)
            img = Image.open(i).convert('RGBA')
            if img.size[0] == img.size[1]:
                img.resize((512, 512)).save(saveFileName)
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
                basemap.save(saveFileName)
        except:
            print(i + ' 出错')


