from gatherer import *
import numpy as np
import matplotlib.pyplot as plt

"""
plots data on a line graph
input data: [(year, data point), ...]
"""
def line_plot(data, format, data_name, graph_title="", ylabel="", done=False):

    # sets empty lists that will store correlating stock and rain data
    xaxis = []
    yaxis = []

    # appends data to respective list for each input pair
    for pairs in data:
        xaxis.append(pairs[0])
        yaxis.append(pairs[1])

    # plots data
    data_plot = plt.plot(xaxis, yaxis, format, label=data_name)
    plt.setp(data_plot)

    # defines plot labels
    plt.xlabel("Year")

    if ylabel != "":
        plt.ylabel(ylabel)
    
    if graph_title != "":
        plt.title(graph_title)

    # shows plotted data if done argument is True
    if done:
        if data_name != "":
            plt.legend()
        plt.show()


def bar_graph(data, colors, floor, width, graph_title, data_labels, ylabel):

    data1 = data[0]
    data2 = data[1]
    
    data1x = []
    data1y = []
    data2x = []
    data2y = []

    for pairs in data1:
        data1x.append(pairs[0])
        data1y.append(pairs[1]-floor)
    
    for pairs in data2:
        data2x.append(str(pairs[0]))
        data2y.append(pairs[1]-floor)

    N = len(data1x)
    ind = np.arange(N)

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, data1y, width, color=colors[0])
    rects2 = ax.bar(ind + width, data2y, width, color=colors[1])

    ax.set_ylabel(ylabel)
    ax.set_title(graph_title)
    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels(data2x)

    ax.legend((rects1[0], rects2[0]), data_labels)

    plt.show()


def main():

    # SBC BLS Data
    sbc_priv_data = sbc_priv_ind("CCData/BLSCC.csv")
    sbc_ttu_data = sbc_ttu_ind("CCData/BLSCC.csv")

    # SBC private industry employment data w/year
    sbc_priv_emp = []
    # SBC private industry wage data w/year
    sbc_priv_wage = []
    # SBC trade, transport, utilities employment data w/year
    sbc_ttu_emp = []
    # SBC trade, transport, utilities establishment data w/year
    sbc_ttu_est = []
    # SBC trade, transport, utilities wage data w/year
    sbc_ttu_wage =[]

    for elem in sbc_priv_data:
        # if elem[0] >= 2010:
        sbc_priv_emp.append((elem[0], elem[1][1]))
        sbc_priv_wage.append((elem[0], elem[1][2]))
    for elem in sbc_ttu_data:
        # if elem[0] >= 2010:
        sbc_ttu_emp.append((elem[0], elem[1][1]))
        sbc_ttu_est.append((elem[0], elem[1][0]))
        sbc_ttu_wage.append((elem[0], elem[1][2]))

    # National BLS Data
    natl_priv_data = natl_priv_ind("CCData/BLSCC.csv")
    natl_ttu_data = natl_ttu_ind("CCData/BLSCC.csv")
    
    # national private industry wage data w/year
    natl_priv_wage = []
    # national trade, transport, utilities wage data w/year
    natl_ttu_wage = []

    for elem in natl_priv_data:
        # if elem[0] >= 2010:
        natl_priv_wage.append((elem[0], elem[1][2]))
    for elem in natl_ttu_data:
        # if elem[0] >= 2010:
        natl_ttu_wage.append((elem[0], elem[1][2]))

    sbc_acs_data = sbc_acs("CCData/ACSCC.csv")
    ca_acs_data = ca_acs("CCData/ACSCC.csv")
    
    sbc_retail_emp = []
    sbc_warehousing_emp = []
    sbc_ur = []
    ca_retail_emp = []
    ca_warehousing_emp = []
    ca_ur = []

    for elem in sbc_acs_data:
        sbc_retail_emp.append((elem[0], elem[1][1]))
        sbc_warehousing_emp.append((elem[0], elem[1][2]))
        sbc_ur.append((elem[0], elem[1][0]))

    for elem in ca_acs_data:
        ca_retail_emp.append((elem[0], elem[1][1]))
        ca_warehousing_emp.append((elem[0], elem[1][2]))
        ca_ur.append((elem[0], elem[1][0]))

    # Warehousing/Retail Establishments SBC
    line_plot(sbc_ttu_est, 'r-', "", graph_title="Warehousing & Retail Establishments", ylabel="Estab. Count", done=True)

    # Total Private employment SBC
    line_plot(sbc_priv_emp, 'r-', "", graph_title="SB County Private Employment", ylabel="Employed", done=True)

    # ACS CA vs. SBC Unemp. Rate
    bar_graph((sbc_ur, ca_ur), ('r', 'b'), 0, 0.45, "SBC vs. CA Unemployment Rate", \
        ("SBC", "CA"), "Unemployment Rate")
    
    # ACS Retail vs. Warehousing jobs (bar)
    bar_graph((sbc_retail_emp, sbc_warehousing_emp), ('r', 'b'), 0, 0.45, "SBC Retail & Warehousing Employment", \
        ("Retail", "Warehousing"), "# Employed")

    # SBC vs. USA Private Industry Avg. Weekly Wages
    line_plot(sbc_priv_wage, "r-", "SB County", graph_title="SBC vs. USA Private Industry Avg. Weekly Wages", ylabel="Avg. Weekly Wage (3 month)")
    line_plot(natl_priv_wage, "b-", "USA Average", done=True)

    # SBC vs. USA Trade, Transport, and Utilities Avg. Weekly Wages
    line_plot(sbc_ttu_wage, "r-", "SB County", graph_title="SBC vs. USA Trade, Transport, and Utilities Avg. Weekly Wages", ylabel="Avg. Weekly Wage (3 month)")
    line_plot(natl_ttu_wage, "b-", "USA Average", done=True)



if __name__ == "__main__":
    main()