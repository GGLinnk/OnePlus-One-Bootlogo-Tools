from copy import deepcopy, copy

class LogoUtils :
    def get_splash_description(self, splash_bytes: bytes) -> str:
        """get_splash_description(splash) : return the description of the given splash byte array.

        Trunctacte array from 0x98 to 0xd8. (0xA0 to 0xd8 for non-formatted splash_bytes)

        0x98 is where the name of the file start, 0xd8 where it ends.
        64 bytes after 0x98.
        """
        result = None
        if "SPLASH!!".encode() in splash_bytes:
            result = copy(splash_bytes[0xE0:0x110])
        else :
            result = copy(splash_bytes[0xd8:0x108])
        return result.decode("UTF-8").rstrip('\x00')

    def get_splash_name(self, splash_bytes: bytes) -> str:
        """get_splash_name(splash) : return the name of the given splash byte array.

        Trunctacte array from 0x98 to 0xd8. (0xA0 to 0xd8 for non-formatted splash_bytes)

        0x98 is where the name of the file start, 0xd8 where it ends.
        64 bytes after 0x98.
        """
        result = None
        if "SPLASH!!".encode() in splash_bytes:
            result = copy(splash_bytes[0xA0:0xE0])
        else :
            result = copy(splash_bytes[0x98:0xd8])
        return result.decode("UTF-8").rstrip('\x00')

    def get_splash_content(self, splash_bytes: bytes) -> bytes:
        """get_splash_content(splash) : return the content of the given splash byte array.

        Trunctacte array from 0x200 to END. (0x1f8 for non-formatted splash_bytes)

        0x200 is where the content of the file start.
        """
        result = None
        if "SPLASH!!".encode() in splash_bytes:
            return copy(splash_bytes[0x200:])
        return copy(splash_bytes[0x1f8:])

    def split_splash(self, logo_bin: bytes) -> dict:
        splash_dict = {}
        splashes = logo_bin.split("SPLASH!!".encode())[1:]
        for index, splash in enumerate(splashes, start=1):
            splash_dict.update({index: {"name": self.get_splash_name(splash), "content": self.get_splash_content(splash), "description": self.get_splash_description(splash)}})
        return splash_dict

