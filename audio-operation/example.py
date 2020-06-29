# -*- coding: utf-8 -*

from pydub import AudioSegment


path = './music.wav'

sound = AudioSegment.from_file(path, format="wav")

#获取音频音量大小
loudness = sound.rms
print(loudness)

#调整音量大小
sound = sound.apply_gain(+20) # 提高

newPath = './music_new.wav'

sound.export(newPath, format = 'wav')

