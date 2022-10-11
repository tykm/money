import csv
from operator import truediv

categories = {}

'''
Parses the general and specific categories
Input: String of category name in format `General Category-Specific`
Output: List in format [General,  Specific]
'''
def category(name):
    categories = []
    tmp_string = ''
    for letter in name:
        if letter == '-':
            categories.append(tmp_string)
            tmp_string = ''
        else:
            tmp_string += letter
    categories.append(tmp_string)
    # todo: error handling if not exactly two categories
    return categories


'''
Amex records certain transactions as blank transactions so this checks for them
Input: array of row of 11 items
Output: bool
'''
def row_is_blank(row):
    blanks = {
        'AUTOPAY PAYMENT - THANK YOU',
        'ONLINE PAYMENT - THANK YOU',
        'MOBILE PAYMENT - THANK YOU'
        }
    desc = row[1]
    if desc in blanks:
        return True
    else:
        return False


with open('amex2022.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    i = 0
    for row in reader:
        if row_is_blank(row):
            continue
        cat = row[10]
        if cat == 'Category':
            continue
        general, specific = category(cat)
        if general not in categories:
            categories[general] = {specific}
        else:
            categories[general].add(specific)

    for item in categories:
        tmp_str = str(item) + ': '
        for spec in categories[item]:
            tmp_str += str(spec)
            tmp_str += ', '
        tmp_str = tmp_str[:-2]
        print(tmp_str)
        