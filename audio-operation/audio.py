# -*- coding: utf-8 -*

from pydub import AudioSegment
import os
import sys


def main():
    try:
        files = os.listdir(sys.argv[1])
    except:
        print('缺少文件夹参数')
        return 

    for file in files:

        if sys.argv[1][-1] == '/' or sys.argv[1][-1] == '\\':
            sys.argv[1] = sys.argv[1][:-1]

        sound = AudioSegment.from_file(sys.argv[1] + '/' + file, format="wav")

        #调整音量大小
        sound = sound.apply_gain(+15) # 提高

        folder = './out/'
        if not os.path.exists(folder):
            os.mkdir(folder)
        newFile = folder + file

        sound.export(newFile, format = 'wav')



if __name__ == "__main__":
    main()