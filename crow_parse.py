from configparser import ConfigParser
import os

class CrowFile:
    def __init__(self) -> None:
        file = os.path.join(os.getcwd(), "build.crow")
        parser = ConfigParser()
        parser.read(file)
        self.config = parser