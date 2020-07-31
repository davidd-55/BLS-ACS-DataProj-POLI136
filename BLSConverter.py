import xlrd
import csv
import os

# converts individual .xlsx sheet to csv file
def csv_from_excel(fname):
    # fname slicing will need to be adjusted on use-case basis
    fname_csv = fname[13:22] + ".csv"
    wb = xlrd.open_workbook(fname)
    sh = wb.sheet_by_name('US_St_Cn_MSA')
    csv_file = open(("BLSDataCSV/" + fname_csv), 'w')
    wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    csv_file.close()

# runs the csv_from_excel function on all .xlsx files in specified directory

count = 0
directory = "BLSDataExcel"
osdir = os.fsencode(directory)

for file in os.listdir(osdir):
    filename = os.fsdecode(file)
    if filename.endswith(".xlsx"):
        print("converting " + filename + " to csv...")
        csv_from_excel(directory + "/" + filename)
        print(filename + " conversion done.")
        count += 1
    else:
        print(filename + " is not an .xlsx file. Passing over...")
        continue

print(("*"*5) + " Conversion Complete! " + str(count) + " files converted." + ("*"*5))
