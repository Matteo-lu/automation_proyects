#!/usr/bin/env python3

"""spreadsheet auto-fill

This script allows the user to automate the process to extract especific
information from a quotation to fill an .xlsx file.

This tool accepts comma separated value files (.xlsx).

This script is required to be located in the same directory as the .pdf
files as well as the main .xslx files

This file contains the main function.

"""

import PyPDF2, openpyxl
from pdf_regex_fun import *

# Getting the most recent PDF file from the current directory
recent_pdf_file = recent_pdf()

# opening excel file and setting the worksheet
pipeline_file = openpyxl.load_workbook('Pipeline.xlsx')
work_sheet = pipeline_file['Hoja1']

# Getting the first empty row
empty_cell = work_sheet.max_row + 1

# Opening the PDF file and saving the text content in pdf_text variable
with open(recent_pdf_file, 'rb') as pdf_file:
	file_reader = PyPDF2.PdfFileReader(pdf_file)
	file_page = file_reader.getPage(0)
	pdf_text = file_page.extractText()

# Obtaining the dictionary with the information extracted from pdf
dict_values = pdf_regex(pdf_text)

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

	# Terminal translator
	# Create a respository to upload the project
	# Fix style with PEP8 and documentation
	# Add new functionalities ("")
	# Handle errors
	# Make de proggram portable = "pip install pyinstaller", "got to direcotry -> app", "use pyinstaller --windowed --onefile --icon=./<icon.ico> <app_name>"
	# Simple graphical interface
