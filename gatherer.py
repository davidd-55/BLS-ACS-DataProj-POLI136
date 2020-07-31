def yr_qtr(yr, qtr):
    if qtr == 1:
        yr = yr
    elif qtr == 2:
        yr += .25
    elif qtr == 3:
        yr += .5
    else:
        yr += .75
    return yr


"""
collects data about SBC private industry totals
return: [(year, [Establishment Count, Average employment (3mo.), Average Weekly Wage]) ... ]
"""
def sbc_priv_ind(fname):
    
    data = open(fname, 'r')
    data.readline()
    targ_area = "San Bernardino County California"
    targ_ind = "Total all industries"

    sbc_data = []

    for line in data:
        data_lst = line.split(',')
        if data_lst[0] == targ_area and data_lst[3] == "Private" and data_lst[4] == targ_ind:
            
            yr = int(data_lst[1])
            qtr = int(data_lst[2])
            
            year = yr_qtr(yr, qtr)

            sbc_data.append((year, [float(data_lst[5]), float(data_lst[6]), float(data_lst[7])]))
    
    data.close()
    return sbc_data


"""
collects data about National private industry totals
return: [(year, [Establishment Count, Average employment (3mo.), Average Weekly Wage]) ... ] county averages in tuple
"""
def natl_priv_ind(fname):
    
    data = open(fname, 'r')
    data.readline()
    targ_area = "U.S. TOTAL"
    targ_ind = "Total all industries"

    natl_data = []

    for line in data:
        data_lst = line.split(',')
        if data_lst[0] == targ_area and data_lst[3] == "Private" and data_lst[4] == targ_ind:
            
            yr = int(data_lst[1])
            qtr = int(data_lst[2])
            
            year = yr_qtr(yr, qtr)

            natl_data.append((year, [round(float(data_lst[5])/3124, 2), round(float(data_lst[6])/3124, 2), float(data_lst[7])]))
    
    data.close()
    return natl_data


"""
collects data about SBC private industry totals
return: [(year, [Establishment Count, Average employment (3mo.), Average Weekly Wage]) ... ]
"""
def sbc_ttu_ind(fname):
    
    data = open(fname, 'r')
    data.readline()
    targ_area = "San Bernardino County California"
    targ_ind = "Trade transportation and utilities"

    sbc_data = []

    for line in data:
        data_lst = line.split(',')
        if data_lst[0] == targ_area and data_lst[3] == "Private" and data_lst[4] == targ_ind:
            
            yr = int(data_lst[1])
            qtr = int(data_lst[2])
            
            year = yr_qtr(yr, qtr)

            sbc_data.append((year, [float(data_lst[5]), float(data_lst[6]), float(data_lst[7])]))
    
    data.close()
    return sbc_data


"""
collects data about National trade, transport, utilities totals
return: [(year, [Establishment Count, Average employment (3mo.), Average Weekly Wage]) ... ] county averages in tuple
"""
def natl_ttu_ind(fname):
    
    data = open(fname, 'r')
    data.readline()
    targ_area = "U.S. TOTAL"
    targ_ind = "Trade transportation and utilities"

    natl_data = []

    for line in data:
        data_lst = line.split(',')
        if data_lst[0] == targ_area and data_lst[3] == "Private" and data_lst[4] == targ_ind:
            
            yr = int(data_lst[1])
            qtr = int(data_lst[2])
            
            year = yr_qtr(yr, qtr)

            natl_data.append((year, [round(float(data_lst[5])/3124, 2), round(float(data_lst[6])/3124, 2), float(data_lst[7])]))
    
    data.close()
    return natl_data

"""
collects yearly ACS data for SBC
return: [(year, unemp. rate, retail employed, warehousing employed)]
"""
def sbc_acs(fname):
    data = open(fname, 'r')
    data.readline()
    targ_area = "San Bernardino"

    sbc_data = []

    for line in data:
        data_lst = line.split(',')
        if data_lst[1] == targ_area:
            retail_employed = float(data_lst[4])
            warehousing_employed = float(data_lst[5])
            sbc_data.append((int(data_lst[0]), [float(data_lst[2]), retail_employed, warehousing_employed]))

    data.close()
    return sbc_data


"""
collects yearly ACS data for California county averages
return: [(year, [unemp. rate, avg. retail employed, avg. warehousing employed])]
"""
def ca_acs(fname):
    data = open(fname, 'r')
    data.readline()
    targ_area = "California"

    ca_data = []

    for line in data:
        data_lst = line.split(',')
        if data_lst[1] == targ_area:
            retail_employed_avg = round(float(data_lst[4]))
            warehousing_employed_avg = round(float(data_lst[5]))
            ca_data.append((int(data_lst[0]), [float(data_lst[2]), retail_employed_avg, warehousing_employed_avg]))

    data.close()
    return ca_data

    
#sbc_data = sbc_priv_ind("CCData/BLSCC.csv")
#natl_data = natl_priv_ind("CCData/BLSCC.csv")
#sbc_acs_data = sbc_acs("CCData/ACSCC.csv")
#ca_acs_data = ca_acs("CCData/ACSCC.csv")
  