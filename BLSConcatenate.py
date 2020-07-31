import os
import glob
import time
import pandas as pd
from csvsort import csvsort

def csv_concatenate(target_directory, outputname): 
    os.chdir(target_directory)
    extension = 'csv'
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

    #combine all files in the list
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])

    #export to csv
    combined_csv.to_csv(outputname, index=False)


def csv_sort(fname):
    csvsort(fname, [1,2,0])


def main():
    # csv_concatenate("BLSscrbd", "BLSScrubbedCCed")
    # time.sleep(3)
    # csv_sort('/Users/daviddattile/OneDrive - Pomona College/Essays&Projects/Politics of Tech/Final Paper/Code&Data/BLSCC.csv')


if __name__ == "__main__":
    main()
