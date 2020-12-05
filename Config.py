import configparser
import os

config = configparser.ConfigParser()


class BasicAuthConfig:
    def __init__(self):
        config.read(os.getcwd() + "/config.ini")
        self.login = config['BASIC_AUTH']['login']
        self.password = config['BASIC_AUTH']['pass']


class FilesSystemConfig:
    def __init__(self):
        config.read(os.getcwd() + "/config.ini")
        self.upload_folder = config['SYSTEM']['upload_folder']
        self.allowed_extensions = config['SYSTEM']['allowed_extensions']


class ProjectRequirements:
    def __init__(self):
        config.read(os.getcwd() + "/config.ini")


class GeneralConfig:
    def __init__(self):
        config.read(os.getcwd() + "/config.ini")
        self.max_bytes_upload_size = int(config['APP_CONFIG']['max_bytes_upload_size'])
        self.secret_key = os.urandom(32)
        self.debug_mode = config['APP_CONFIG']['debug_mode']

