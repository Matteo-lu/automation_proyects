#!/usr/bin/env python3

"""spreadsheet auto-fill auxiliar functions"""


import re

def pdf_regex(pdf_text):
    """Function to extract information from the pdf text variable
    using regular expressions.

    Args:
        pdf_text: variable containing the text extracted from the pdf file

    Returns:
        The return value. dictionary containing the values to be
        added to the .xlsx file

    """

    dict_values = {}
    # Getting the quotation number
    quotation_number = re.compile(r'No. *\d\d\d\d')
    mo = quotation_number.search(pdf_text)
    if not mo:
        print("The quote number could not be found")
        return(None)
    dict_values['quot_number'] = mo.group()

    # Getting the expedition date
    dates = re.compile(r'(\d\d\W\d\d\W\d\d\d\d)+')
    mo = dates.search(pdf_text)
    if not mo:
        print("The expedition date could not be found")
        return(None)
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
    if not mo:
        print("The client could not be found")
        return(None)
    dict_values['client'] = mo.group()[9:]

    # Value before IVA
    value_list = re.compile(
        r'Subtotal\$(\d+,)?(\d+,)?(\d+,)?(\d+,)?(\d+.)?(\d+)?'
    )
    mo = value_list.search(pdf_text)
    if not mo:
        print("The Value before IVA could not be found")
        return(None)
    dict_values['subtotal'] = mo.group()[9:]

    return(dict_values)
