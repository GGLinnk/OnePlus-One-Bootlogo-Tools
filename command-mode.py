##FILE FOR TEST ONLY, WIP Project !
##NOT COMPATIBLE WITH COLOR OS logo.bin

from app.logo_utils import LogoUtils

utils = LogoUtils()

file = open("logo-cm.bin", "rb")
byte = file.read()

splashes = utils.split_splash(byte)

for element in splashes:
    print("Content : ", splashes[element]["description"])