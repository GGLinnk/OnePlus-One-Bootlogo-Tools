#!/bin/env python3

##FILE IS FOR TESTING ONLY, WIP Project !
##NOT COMPATIBLE WITH COLOR OS logo.bin

from app.logo_utils import LogoUtils

utils = LogoUtils("logo-oos.bin")
splashes = utils.get_splashes()
for splash in splashes:
    print("Name : %s" % splashes[splash]["name"])
    print("Desc : %s" % splashes[splash]["description"])
    print("Dime : %s" % splashes[splash]["dimentions"])
    print("Cont : %s" % splashes[splash]["content"])

#splashes = utils.split_splash(byte)

#for element in splashes:
#    print("Content : ", splashes[element]["description"])