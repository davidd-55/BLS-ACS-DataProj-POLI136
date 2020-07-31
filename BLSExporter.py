import os

def num_remover(ind):
    if ind[0].isdigit():
        return num_remover(ind[1:])
    else:
        return ind.strip()


def lstScrubber(lst):
    # initialize empty list for cleaned up entries
    scrubbed_lst = []
    
    # scrubs elems and appends
    for elem in lst:
        if lst.index(elem) == 0:
            no_quote = elem.strip('"')
            scrubbed_lst.append(no_quote.strip())
        elif lst.index(elem) == (len(lst)-1):
            no_quote = elem[0:len(elem)-2]
            scrubbed_lst.append(no_quote.strip())
        else:
            scrubbed_lst.append(elem.strip())
    
    return scrubbed_lst


def qtrly_avg(mo1, mo2, mo3):
    mo1_num = float(mo1)
    mo2_num = float(mo2)
    mo3_num = float(mo3)
    return round(((mo1_num + mo2_num + mo3_num)/3), 2)


def extracter(fname_in, dir_out): 
    print("initializing scrubbing on " + fname_in + "...")
    
    #open/prep files
    fname_csv = fname_in[11:20] + "scrbd.csv"
    oldBLS = open(fname_in, 'r')
    newBLS = open(dir_out + fname_csv, 'w')

    # find structure of csv and scrub columns
    structure = oldBLS.readline().split('","')
    strpd_strctr = lstScrubber(structure)

    # data points index for new file using scrubbed header
    area_in = strpd_strctr.index('Area')
    year_in = strpd_strctr.index('Year')
    qtr_in = strpd_strctr.index('Qtr')
    owner_in = strpd_strctr.index('Ownership')
    ind_in = strpd_strctr.index('Industry')
    est_in = strpd_strctr.index('Establishment Count')
    mo1_in = est_in + 1
    mo2_in = est_in + 2
    mo3_in = est_in + 3
    aww_in = strpd_strctr.index('Average Weekly Wage')

    # write new header
    newBLS.write(strpd_strctr[area_in] + ',' + strpd_strctr[year_in] + ',' + strpd_strctr[qtr_in] + ',' + strpd_strctr[owner_in] \
        + ',' + strpd_strctr[ind_in] + ',' + strpd_strctr[est_in] + ',' + "Average employment (3mo.)" + ',' + strpd_strctr[aww_in] + "\n")

    # begin identifying desired lines, scrubbing, and writing to output csv
    for line in oldBLS:

        # strip line and initialize list for cleaned up elements
        sl = line.split('","')
        sl_strpd = lstScrubber(sl)

        # identify lines
        if (sl_strpd[area_in] == 'U.S. TOTAL') or (sl_strpd[area_in] == 'San Bernardino County, California'):
            avg_emp = qtrly_avg(sl_strpd[mo1_in], sl_strpd[mo2_in], sl_strpd[mo3_in])
            area_no_comma = sl_strpd[area_in].replace(',', '')
            industry_no_comma = sl_strpd[ind_in].replace(',', '')

            line = (area_no_comma + "," + sl[year_in] + "," + sl[qtr_in] + "," + sl[owner_in] + "," + \
                num_remover(industry_no_comma) + "," + sl[est_in] + "," + str(avg_emp) + "," + sl[aww_in] + "\n")
            newBLS.write(line)
            
        else:
            continue
    
    # close files
    oldBLS.close()
    newBLS.close()
    print("Scrubbing complete.")

def main():

    count = 0
    directory = "BLSDataCSV"
    osdir = os.fsencode(directory)

    for file in os.listdir(osdir):
        filename = os.fsdecode(file)
        if filename.endswith(".csv"):
            print("scrubbing and exporting " + filename + " to csv...")
            extracter("BLSDataCSV/" + filename, "BLSscrbd/")
            print(filename + " conversion done.")
            count += 1
        else:
            print(filename + " is not an .csv file. Passing over...")
            continue

    print(("*"*5) + " Scrubbing Complete! " + str(count) + " files converted. " + ("*"*5))
    print(("*"*5) + " New files can be found in directory " + "BLSscrbd/ " + ("*"*5))

if __name__ == "__main__":
    main()
