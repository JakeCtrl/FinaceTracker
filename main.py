import pprint
from config import CONSUMER_KEY, REDIRECT_URI, JSON_PATH
from Jake import TD_ACCOUNT
from td.client import TDClient
from twili import ACCOUNT_SID, AUTH_TOKEN, MY_NUMBER
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, redirect

# TD Ameritrade =========================================================================================
td_client= TDClient(client_id= CONSUMER_KEY, redirect_uri= REDIRECT_URI, credentials_path= JSON_PATH)

td_client.login()

quotes_responce = td_client.get_quotes(instruments=['BCRX'])

orders_and_positions = td_client.get_accounts(account= TD_ACCOUNT, fields= ['positions', 'orders'])

totalAccountBalance = orders_and_positions.get('securitiesAccount').get('currentBalances').get('equity')

currentPositions = orders_and_positions.get('securitiesAccount').get('positions')
#print(type(currentPositions))
#print(currentPositions[]['instrument']['symbol'])
currentTickers = []
currentOptions =[]

for i in range(len(currentPositions)):

    temp = currentPositions[i]['instrument']['symbol']

    if len(temp) < 6 and temp != "MMDA1":
        currentTickers.append(temp)

    if len(temp) > 6 and temp != 'MMDA1':
        currentOptions.append(temp)


print(currentTickers)
print(currentOptions)

# TD End ================================================================================================

# Twillo ================================================================================================
account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN

client = Client(account_sid, auth_token)

#client.messages.create(body = "32", from_ = MY_NUMBER, to= '+19806998508' )
messages = client.messages.list(limit=20, from_= '+19806998508')

#Twillo End ==============================================================================================

# Google Sheets ==========================================================================================

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("googlecreds.json", scope)

googleClient = gspread.authorize(creds)

sheet = googleClient.open("Balance Sheet").get_worksheet(0)

print(sheet)

# ========================================================================================================

# MAIN FUNCTIONALITY =====================================================================================

app = Flask(__name__)

@app.route("/sms", methods= ['GET', 'POST'])
def sms_reply():
    resp = MessagingResponse()
    resp.message("The test worked")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

# Weekly Update

# Monthly Update

# Spend Category Tracker


# Net worth update

# Income made

# Money Spent

# Free cash flow

# Spending changes alert

# Setting Monthly Budget

# Investment Performance

# Credit Card optimization

# Keeping track of time

#DB password 0lk0HmuOsMmrC6S1

# ========================================================================================================

