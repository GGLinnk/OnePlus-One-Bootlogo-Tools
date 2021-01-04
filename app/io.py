import logging

class IO:
    def __init__(self, filepath, filemode: type = "default"):
        self.readed = False
        self.filepath = filepath
        self.readmode = filemode
        self.__set_mode()

    def __set_mode(self):
        if self.readmode is bytes:
            self.textmode = "rb"
            self.filecopy = b""
        else:
            self.textmode = "r"
            self.filecopy = ""

    def read(self):
        with open(self.filepath, self.textmode) as file:
            self.filecopy = file.read()
        self.readed = True
        
    def get_copy(self):
        if not self.readed:
            logging.warning("Unable to get copy ! You need to read it first !")
        return self.filecopy