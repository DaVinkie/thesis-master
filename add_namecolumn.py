import os
import sys
import numpy as np
import pandas as pd

def main():
    ''' 
    Inserts a column called Name into recorded output as is required by 
    Unreal Engine to handle data tables. Values are simply a indexed list that
    Unreal Engine can loop over. '''
    
    # Check input argument
    if len(sys.argv) != 2:
        print("Please provide a single path to an input file.")
        sys.exit()
    else:
        in_file = sys.argv[1]
        in_path = os.path.normpath(in_file)

    # Column insertion
    df = pd.read_csv(in_path, sep=',')
    df_size = len(df)
    name_col = np.arange(0, df_size)
    
    df.insert(0, 'Name', name_col)

    # Output file
    out_name = in_file[:-4] + '_named.csv'
    out_path = os.path.normpath(out_name)
    
    df.to_csv(out_path, index=False)

if __name__ == "__main__":
    main()