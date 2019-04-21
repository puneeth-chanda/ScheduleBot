from pprint import pprint
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient import discovery

scope=['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

credentials= ServiceAccountCredentials.from_json_keyfile_name('timetable-5bfb2ff2757e.json',scope)


service = discovery.build('sheets', 'v4', credentials=credentials)

# The ID of the spreadsheet to retrieve data from.
spreadsheet_id = '19h4E_xF5kbWiz0P7fIIEMfblcphKM4zICaA1mLe_vtM'  


# The A1 notation of the values to retrieve.:ranges
def get_response_username():

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



if __name__ == "__main__":
    