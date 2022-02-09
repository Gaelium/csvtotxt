import csv

filename = "mycsv.csv" #replace with path to your csv file.
title = "Column Key" #Name of the column that you want to be used for each text file name.
with open(filename, encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        file_name ='{0}.txt'.format(row[title]) 
        with open(file_name, 'w', encoding="utf8") as f:
            for key in row:
                f.write("\n\n" + key + "\n")
                f.write(row[key])
            

#To run, open a terminal, cd to the folder this file is in, and type "py csvhandler.py" for powershell or "python csvhandler.py" for bash
