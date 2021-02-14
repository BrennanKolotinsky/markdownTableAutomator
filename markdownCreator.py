import csv
cols = 0

f = open("README.md", "a") # a indicates you can write to the file!
f.truncate(0) # delete existing content in file
f.write("# Table Markdown Automator")
f.write("\n## To create a markdown chart, simply pull this code and place your CSV file in the root directory of this code")
f.write("\n## Then simply run python markdownCreator.py and type the name of your CSV file when prompted. The output will be markdown in the README.md file")

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
            print("| " + " | ".join(row) + " |")
            f.write("\n| " + " | ".join(row) + " |")
            cols = len(row)
            f.write("\n| " + " - |" * cols)
            
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            f.write("\n| " + " | ".join(row) + " |")
            line_count += 1
    print(f'Processed {line_count} lines.')

f.close()