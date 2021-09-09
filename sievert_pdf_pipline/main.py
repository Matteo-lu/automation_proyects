#!/usr/bin/env python3

"""spreadsheet auto-fill

This script allows the user to automate the process to extract especific
information from a quotation to fill an .xlsx file.

This tool accepts comma separated value files (.xlsx).

This script is required to be located in the same directory as the .pdf
files as well as the main .xslx

This file contains the main function.

"""

import PyPDF2, openpyxl
from pdf_regex_fun import *
import sys

# Getting the most recent PDF file from the current directory
recent_pdf_file = recent_pdf()
if not recent_pdf_file:
	print("Sorry, inside this directory there are no PDF files")
	sys.exit(1)

# opening excel file and setting the worksheet
try:
	pipeline_file = openpyxl.load_workbook('Pipeline.xlsx')
	work_sheet = pipeline_file['Hoja1']
except FileNotFoundError:
	print("Sorry the file Pipeline.xlsx doesn't exist inside this folder")
	sys.exit(1)
except:
	print("Unexpected error:", sys.exc_info()[0])
	sys.exit(1)

# Getting the first empty row
empty_cell = work_sheet.max_row + 1

# Opening the PDF file and saving the text content in pdf_text variable
try:
	with open(recent_pdf_file, 'rb') as pdf_file:
		file_reader = PyPDF2.PdfFileReader(pdf_file)
		file_page = file_reader.getPage(0)
		pdf_text = file_page.extractText()
	if not pdf_text:
		print("no data in file " + recent_pdf_file)
except IOError:
	print("Sorry the file {} doesn't exist inside this folder".format(recent_pdf_file))
	sys.exit(1)
except:
	print("Unexpected error:", sys.exc_info()[0])
	sys.exit(1)

# Obtaining the dictionary with the information extracted from pdf
dict_values = pdf_regex(pdf_text)
if not dict_values:
	sys.exit(1)

# Ideinfying if the quotation was already inserted in the .xlsx file
for row in work_sheet.values:
	i = 0
	if (row[0] == dict_values['quot_number']):
		i += 1

if (i == 0):
	#Applying style and value to each cell from A# to Q#
	fill_excel(dict_values, work_sheet, empty_cell)

pipeline_file.save('Pipeline.xlsx')
pipeline_file.close()

	# Fix style with PEP8 and documentation
	# Add new functionalities ("Check all files within the directory and instert them if their are not inide the excel file")
	# Make de proggram portable = "pip install pyinstaller", "got to direcotry -> app", "use pyinstaller --windowed --onefile --icon=./<icon.ico> <app_name>"
	# Generate windows alert for every error
