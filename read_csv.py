import csv

# Opening csv file

with open("FL_insurance_sample.csv", "rU") as data:
    p = csv.reader(data)

    # list and sting to append data

    with_type = []
    a = ""
    
    # ASKING COUNTY NAME
    
    county = raw_input("Enter a county name: ")

    for row in p:
        
        """ printing only CLAY COUNTY """
        
        if row[2] == county.upper():
            
            # Assign each one with specific value
            
            """a = "policyID: " + row[0] + ",\nstatecode: " + row[1] + ",\ncounty: " + row[2] + ",\neq_site_limit: " + row[3] + ",\nhu_site_limit: " + row[4] + ",\nfl_site_limit: " + row[5] + \
                 ",\nfr_site_limit: " + row[6] + ",\ntiv_2011: " + row[7] + ",\ntiv_2012: " + row[8] + ",\neq_site_deductible: " + row[9] + ",\nhu_site_deductible: " + row[10] + ",\
fl_site_deductible: " + row[11] + ",\nfr_site_deductible: " + row[12] + ",\npoint_latitude: " + row[13] + \
                 ",\npoint_longitude: " + row[14] + ",\nline: " + row[15] + ",\nconstruction: " + row[16] + ",\npoint_granularity: " + row[17] """

            a = "policyID: " + row[0] + ",statecode: " + row[1] + ",county: " + row[2] + ",eq_site_limit: " + row[3] + ",hu_site_limit: " + row[4] + ",fl_site_limit: " + row[5] + \
                 ",fr_site_limit: " + row[6] + ",tiv_2011: " + row[7] + ",tiv_2012: " + row[8] + ",eq_site_deductible: " + row[9] + ",hu_site_deductible: " + row[10] + ",\
fl_site_deductible: " + row[11] + ",fr_site_deductible: " + row[12] + ",point_latitude: " + row[13] + \
                 ",point_longitude: " + row[14] + ",line: " + row[15] + ",construction: " + row[16] + ",point_granularity: " + row[17]
                        
            # Appending values to list
                        
            with_type.append(a)
            
# creating a dictionary
            
length = range(0,len(with_type))
dict_data = dict(zip(length,with_type))
            
print dict_data[1]

