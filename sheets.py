from pprint import pprint
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient import discovery
import json
import requests
import datetime

scope=['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

credentials= ServiceAccountCredentials.from_json_keyfile_name('timetable-5bfb2ff2757e.json',scope)


service = discovery.build('sheets', 'v4', credentials=credentials)

# The ID of the spreadsheet to retrieve data from.
spreadsheet_id = '1MylMFPDSjs4j2TB-A3UCcF6UD6akrf7L0DRAf4Crs9A'


# The A1 notation of the values to retrieve.:ranges
"""def get_response_username():

    request = service.spreadsheets().values().batchGet(spreadsheetId=spreadsheet_id, ranges='b2:az100000')
    response = request.execute()

    k = response
    return(k)

def no_of_entries():
    k=get_response_username()
    return(len(k['valueRanges'][0]['values']))
    
def all_subscribers():
    k=get_response_username()
    return(k['valueRanges'][0]['values'])

def usernames(i):
    l=no_of_entries()
    a=all_subscribers()
    for i in range(l):
        username = a[i][0]
        return(username)
"""
TOKEN = "647896728:AAELpQDWDBZ1h0c976Hx_XyOzyGHljig6AI"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js


def get_chat_id(updates, i):
    num_updates = len(updates["result"])
    chat_id = updates["result"][i]["message"]["chat"]["id"]
    return (chat_id)


def no_subscribers(updates):
    num_subs = len(updates["result"])
    return (num_subs)


def send_message(tt, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(tt, chat_id)
    get_url(url)

def get_response_classname():

    request = service.spreadsheets().values().batchGet(spreadsheetId=spreadsheet_id, ranges='b2:az100000')
    response = request.execute()

    k = response
    return(k)

if __name__ == '__main__':
    a = []
    b = []
    now = datetime.datetime.now()
    day = now.strftime("%A")