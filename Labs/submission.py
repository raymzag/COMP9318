## import modules here 
import pandas as pd
import numpy as np


################# Question 1 #################

# helper functions
def project_data(df, d):
    # Return only the d-th column of INPUT
    return df.iloc[:, d]

def select_data(df, d, val):
    # SELECT * FROM INPUT WHERE input.d = val
    col_name = df.columns[d]
    return df[df[col_name] == val]

def remove_first_dim(df):
    # Remove the first dim of the input
    return df.iloc[:, 1:]

def slice_data_dim0(df, v):
    # syntactic sugar to get R_{ALL} in a less verbose way
    df_temp = select_data(df, 0, v)
    return remove_first_dim(df_temp)

def buc_rec_optimized(df):# do not change the heading of the function
    temp_data_raw = buc_helper(df)
    pd_raw_data = []
    for i, j in temp_data_raw:
        aList = list(filter(lambda x: x != '', i.split(',')))
        aList.append(j)
        pd_raw_data.append(aList)
    return pd.DataFrame.from_records(pd_raw_data, columns=df.columns)
    
def buc_helper(input, output_df=[], index=''):
    dims = input.shape[1]
    
    if dims == 1:
        # only the measure dim
        input_sum = sum( project_data(input, 0) )
        output_df.append((index, input_sum))
    else:
        # the general case
        dim0_vals = set(project_data(input, 0).values)
        for dim0_v in dim0_vals:
            if index != '':
                new_index = ',' + str(dim0_v)
            else:
                new_index = str(dim0_v)
            sub_data = slice_data_dim0(input, dim0_v)
            buc_helper(sub_data, output_df, index + new_index)
            
        ## for R_{ALL}
        sub_data = remove_first_dim(input)
        buc_helper(sub_data, output_df, index + ',ALL')
    return output_df

################# Question 2 #################

def v_opt_dp(x, num_bins):# do not change the heading of the function
    pass # **replace** this line with your code