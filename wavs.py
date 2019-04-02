#_*_coding:utf-8_*_
# Author:Sung-MinChe

from data import conf
import os

def chk_wavs():
    cwd = os.getcwd()
    print(cwd)
    for wav in conf.wavs:
        print(wav)
        name = wav.get('key')
        if os.path.isfile(name):
            pass
        else:
            with open(name, 'wb') as f:
                f.write(wav.get('val'))

chk_wavs()