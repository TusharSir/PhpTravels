import configparser

config = configparser.RawConfigParser()

#config.read("D:\\Credence Python Projects by Tushar Sir\\PhpTravels\\Configuration\\config.ini")
config.read(".\\Configuration\\config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseUrl')
        return url

    @staticmethod
    def getUsername():
        username= config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

import collections