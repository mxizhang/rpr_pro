from apiclient import discovery
import gspread
from googleapiclient.errors import HttpError
from oauth2client.service_account import ServiceAccountCredentials

KEY = 'flipnj-4f3fbac03d23.json'

def main():
	scope = ['https://spreadsheets.google.com/feeds']
	creds = ServiceAccountCredentials.from_json_keyfile_name(KEY, scope)
	client = gspread.authorize(creds)

	# Find a workbook by name and open the first sheet
	# Make sure you use the right name here.
	sheet = client.open("HUNTERDON SHERIFF SALE LIST")
	worksheet = sheet.worksheet('all')

	cell_list = worksheet.range('A6:Q6')

	for cell in cell_list:
	    print cell.value
	# Extract and print all of the values
	#list_of_hashes = worksheet.get_all_records()
	#print(list_of_hashes)

if __name__ == '__main__':
    main()