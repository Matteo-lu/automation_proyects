#!/usr/bin/env python3

"""spreadsheet auto-fill auxiliar functions

This script allows the user to automate the process to extract especific
information from a quotation to fill an .xlsx file.

This script is required to be located in the same directory as the .pdf
files as well as the main .xslx file

This file can also be imported as a module and contains the following
functions:

    * pdf_regex - returns dictionary containing the values to be
		added to the .xlsx file
    * fill_excel - apply style and insert values to each cell
	* recent_pdf - get the most recent PDF file from the current directory

"""

def pdf_regex(pdf_text):
	"""Function to extract information from the pdf text variable
	using regular expressions.

    Args:
        pdf_text: variable containing the text extracted from the pdf file

    Returns:
        The return value. dictionary containing the values to be
		added to the .xlsx file

    """

	import re

	dict_values = {}
	# Getting the quotation number
	quotation_number = re.compile(r'No. *\d\d\d\d')
	mo = quotation_number.search(pdf_text)
	dict_values['quot_number'] = mo.group()

	# Getting the expedition date
	dates = re.compile(r'(\d\d\W\d\d\W\d\d\d\d)+')
	mo = dates.search(pdf_text)
	dates_string = mo.group()
	dates_list = []
	dates_list.append(dates_string[:10])
	dates_list.append(dates_string[10:])
	dict_values['expedition_date'] = dates_list[0]

	# Responsable
	dict_values['responsable'] = 'Lina García'

	# Getting cliente
	client_list = re.compile(r'\d{9}\D+')
	mo = client_list.search(pdf_text)
	dict_values['client'] = mo.group()[9:]

	# Value before IVA
	value_list = re.compile(r'Subtotal\$(\d+,)?(\d+,)?(\d+,)?(\d+,)?(\d+.)?(\d+)?')
	mo = value_list.search(pdf_text)
	dict_values['subtotal'] = mo.group()[9:]

	return(dict_values)

def fill_excel(dict_values, work_sheet, empty_cell):
	"""Function to apply style and insert values to each cell from A# to Q#

    Args:
        dict_values: dictionary containing the values to be
		added to the .xlsx file
		work_sheet: .xlsx worksheet object
		empty_cell: first empty cell identify in the .xlsx file

    Returns:
        The return value. None
    """

	from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font
	from datetime import datetime

	# Setting variables fill and align with the expecting cells format
	fll = PatternFill(start_color="a4c2f4", fill_type = "solid")
	align = Alignment(horizontal='center', vertical='center', wrapText=True)

	letter = 'ABCDEFGHIJKLMNOPQ'
	for cell in letter:
		if cell == 'A':
			work_sheet[cell + str(empty_cell)] = dict_values['quot_number']
		if cell == 'C':
			date_format = datetime.strptime(dict_values['expedition_date'], '%d/%m/%Y')
			work_sheet[cell + str(empty_cell)] = date_format.date()
		if cell == 'F':
			work_sheet[cell + str(empty_cell)] = dict_values['responsable']
		if cell == 'H':
			work_sheet[cell + str(empty_cell)] = dict_values['client']
		if cell == 'J':
			work_sheet[cell + str(empty_cell)] = dict_values['subtotal']

		style_cell = work_sheet[cell + str(empty_cell)]
		style_cell.fill = fll
		style_cell.alignment = align

def recent_pdf():
	"""Function to get the most recent PDF file from the current directory

    Args:
		None

    Returns:
        The return value. Most recent file name within the current directory
    """

	import glob, os

	file_path = '*.pdf'
	list_files = sorted(glob.iglob(file_path), key=os.path.getctime, reverse=True)
	print(list_files)

	return (list_files[0])
