from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient import discovery
import json
import requests
import datetime
from telegram.ext import Updater, CommandHandler
class Telegram:
    def __init__(self, token):
        self.username = ''
        self.token = ''

    def SendMessage(message):
        

