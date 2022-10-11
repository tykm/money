import csv


with open('amex2022.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)

    i = 0
    for row in reader:
        ct = 0
        for item in row:
            ct += 1
            #print(item)
        #print('\n')
        if ct != 11:
            print(row)
        # breaks loop after testing first row
        #if i == 1:
        #    break
        #i += 1