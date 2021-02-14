import csv
cols = 0

f = open("README.md", "a") # a indicates you can write to the file!
f.truncate(0) # delete existing content in file
f.write("# Table Markdown Automator")
f.write("\nTo create a markdown chart: \n* Pull this code \n* Place your CSV file in the root directory of this code \n* Run ```python markdownCreator.py``` \n* Type the name of your CSV file when prompted")
f.write("\n\nThe output will be markdown in the README.md file")

fName = input("Please enter the name of your csv file!");
if (fName == ""):
	print("Using default file input - Bill of Material.csv");
	fName = "Bill of Material.csv"

with open(fName) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    cols = 0
     
    for row in csv_reader:
        if line_count == 0:
            f.write("\n| " + " | ".join(row) + " |")
            cols = len(row)
            f.write("\n| " + " - |" * cols)
            
            line_count += 1
        else:
            f.write("\n| " + " | ".join(row) + " |")
            line_count += 1
    print(f'Processed {line_count} lines.')

f.close()