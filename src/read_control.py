# -*- coding: utf-8 -*-
from PIL import Image
import readClass

def readStart(path):
    read = readClass.Read()
    data = read.read(path)
    return data
