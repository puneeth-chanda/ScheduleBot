from pprint import pprint
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient import discovery

scope=['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

credentials= ServiceAccountCredentials.from_json_keyfile_name('timetable-5bfb2ff2757e.json',scope)


service = discovery.build('sheets', 'v4', credentials=credentials)

# The ID of the spreadsheet to retrieve data from.
spreadsheet_id = 'id'  

# The A1 notation of the values to retrieve.
def no_responses():


def get_response_username(range_,i):

    request = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_)
    response = request.execute()

    k = response["values"][0][i]
    return(k)
    