import logging
import re
from app.io import IO
from copy import deepcopy, copy


class LogoUtils:
    def __init__(self, bin_path: str):
        self.__parsed = False
        self.__parsed_splash = {}
        self.__bytes = b""
        self.__iomanager = IO(bin_path, bytes)

    def __get_splash_description(self, splash_bytes: bytes) -> str:
        """get_splash_description(splash) : return the description of the given splash byte array.

        Trunctacte array from 0x98 to 0xd8. (0xA0 to 0xd8 for non-formatted splash_bytes)

        0x98 is where the name of the file start, 0xd8 where it ends.
        64 bytes after 0x98.
        """
        if "SPLASH!!".encode() in splash_bytes:
            return copy(splash_bytes[0xE0:0x110]).decode("UTF-8").rstrip('\x00')
        return copy(splash_bytes[0xd8:0x108]).decode("UTF-8").rstrip('\x00')

    def __get_splash_name(self, splash_bytes: bytes) -> str:
        """get_splash_name(splash) : return the name of the given splash byte array.

        Trunctacte array from 0x98 to 0xd8. (0xA0 to 0xd8 for non-formatted splash_bytes)

        0x98 is where the name of the file start, 0xd8 where it ends.
        64 bytes after 0x98.
        """
        if "SPLASH!!".encode() in splash_bytes:
            return copy(splash_bytes[0xA0:0xE0]).decode("UTF-8").rstrip('\x00')
        return copy(splash_bytes[0x98:0xd8]).decode("UTF-8").rstrip('\x00')

    def __get_splash_content(self, splash_bytes: bytes) -> bytes:
        """get_splash_content(splash) : return the content of the given splash byte array.

        Trunctacte array from 0x200 to END. (0x1f8 for non-formatted splash_bytes)

        0x200 is where the content of the file start.
        """
        if "SPLASH!!".encode() in splash_bytes:
            return copy(splash_bytes[0x200:])
        return copy(splash_bytes[0x1f8:])

    def __get_splash_width(self, splash_bytes: bytes) -> int:
        """get_splash_width(splash) : return the width contained inside the byte array.

        Get the value contained in 0x?? (0x?? for non-formatted splash_bytes)
        """
        if "SPLASH!!".encode() in splash_bytes:
            return int.from_bytes(splash_bytes[0x24:0x28], 'little', signed=True)
        return int.from_bytes(splash_bytes[0x1C:0x20], 'little', signed=True)

    def __get_splash_height(self, splash_bytes: bytes) -> int:
        """get_splash_height(splash) : return the height contained inside the byte array.

        Get the value contained in 0x?? (0x?? for non-formatted splash_bytes)
        """
        if "SPLASH!!".encode() in splash_bytes:
            return int.from_bytes(splash_bytes[0x20:0x24], 'little', signed=True)
        return int.from_bytes(splash_bytes[0x18:0x1C], 'little', signed=True)

    def __parse_splash(self) -> dict:
        for index, splash in enumerate(self.__bytes.split("SPLASH!!".encode())[1:], start=1):
            self.__parsed_splash.update({
                index: {
                    "name": self.__get_splash_name(splash),
                    "description": self.__get_splash_description(splash),
                    "dimentions": {
                        "width": self.__get_splash_width(splash),
                        "height": self.__get_splash_height(splash),
                    },
                    "content": self.__get_splash_content(splash)
                }
            })
        self.__parsed = True

    def __read_splash(self):
        self.__iomanager.read()
        self.__bytes = self.__iomanager.get_copy()

    def get_splashes(self):
        if not self.__parsed:
            self.__read_splash()
            self.__parse_splash()
        return self.__parsed_splash
