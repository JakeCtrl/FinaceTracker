import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("googlecreds.json", scope)

googleClient = gspread.authorize(creds)
#googleClient.create("Test2")
#sheet2 = googleClient.open("Test2")
#sheet2.share('jakeinctrl@gmail.com', perm_type='user', role='Editor' )

sheet = googleClient.open("Balance Sheet") #.get_worksheet(0)

sheet.

print(sheet)