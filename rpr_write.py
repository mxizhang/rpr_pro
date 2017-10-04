# -*- coding: utf-8 -*-
# -*- author: mxiz -*-
import time
from gspread import *
import csv
from zillow_function import findzillow
import httplib2
import random
import os
import subprocess
from apiclient import discovery
from googleapiclient.errors import HttpError
from oauth2client.service_account import ServiceAccountCredentials

ADD = 'https://docs.google.com/spreadsheets/d/1BAOmr9Hx08pDnEpA2lSGoinZYX19qxjI54SVzNQ3h50/edit#gid=0'

def get_gspread(SS_ADDRESS, sheetname):
	scope_gs = ['https://spreadsheets.google.com/feeds']
	credentials_gs = ServiceAccountCredentials.from_json_keyfile_name(KEY, scope_gs)
	gc = authorize(credentials_gs)
	sh = gc.open_by_url(SS_ADDRESS)
	worksheet = sh.worksheet(sheetname)
	return worksheet

def get_google_service():
	scope_gl = 'https://www.googleapis.com/auth/spreadsheets'
	credentials_gl = ServiceAccountCredentials.from_json_keyfile_name(KEY, scope_gl)
	http = credentials_gl.authorize(httplib2.Http())
	discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?version=v4')
	service = discovery.build('sheets', 'v4', http=http, discoveryServiceUrl=discoveryUrl)
	return service

def find_sheetId(spreadsheetID, sheetname):
	service = get_google_service()
	result = service.spreadsheets().get(spreadsheetId=spreadsheetID).execute()
	for item in result['sheets']:
		if item['properties']['title'] == sheetname:
			return item['properties']['sheetId']
	return None

def find_sheetname(spreadsheetID, sheetId):
	service = get_google_service()
	result = service.spreadsheets().get(spreadsheetId=spreadsheetID).execute()
	for item in result['sheets']:
		if item['properties']['sheetId'] == sheetId:
			return item['properties']['title']
	return None