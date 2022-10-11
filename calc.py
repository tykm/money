import csv

categories = set()

with open('amex2022.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    i = 0
    for row in reader:
        cat = row[10]
        if cat not in categories:
            categories.add(cat)




        # breaks loop after testing first row
        #if i == 1:
        #    break
        #i += 1
    categories.remove('Category')
    print(len(categories))
    for item in categories:
        print(item)