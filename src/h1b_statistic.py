# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 13:04:44 2018

@author: Shilong
"""

import csv
from collections import Counter



def counting(filename, visa_info, count_item, visa_status = "CERTIFIED"):
    
    with open(filename, encoding = "utf8", newline = '') as csvfile:
        reader = csv.DictReader(csvfile, delimiter = ";")
        filtered = filter(lambda x: x[visa_info] == visa_status, reader)
        counts = Counter(row[count_item] for row in filtered)
        
    return counts, sum(counts.values())



def sort_values(counts, total_values, output_number = 10):
    
    counts_sorted = sorted(counts.items(), key = lambda x: (-x[1], x[0]))
    counts_with_percent = [list(tup) + [str(round(tup[1] / total_values * 100, 1)) + '%'] for tup in counts_sorted]
    
    return counts_with_percent[:output_number]



def write_file(output_filename, counts_statistic, header):
    
    title = ";".join(header) + '\n'
    with open(output_filename, "w") as writefile:
        writefile.write(title)
        for i in range(len(counts_statistic)):
            value = ";".join([str(x) for x in counts_statistic[i]]) + '\n'
            writefile.write(value)


            
def main():
    
    filename = "h1b_input.csv"
    visa_info = "CASE_STATUS" 
    job_title = "SOC_NAME"
    
    counts, total_values = counting(filename, visa_info, count_item = job_title)
    
    counts_statistic = sort_values(counts, total_values)
    
    header_occup = ['TOP_OCCUPATIONS', 'NUMBER_CERTIFIED_APPLICATIONS', 'PERCENTAGE']
    header_states = ['TOP_STATES', ' NUMBER_CERTIFIED_APPLICATIONS', 'PERCENTAGE']
    
    write_file("top_10_occupations.txt", counts_statistic, header_occup)
    write_file("top_10_states.txt", counts_statistic, header_states)
    
    
     

if __name__ == "__main__":
    main()