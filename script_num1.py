import pandas as pd
#import numpy as np
import sys

#############################################################################
##  command to run the code #################################################
### python script_num1.py FMD-January2020_new.xlsx FMD-January2020_new.csv ##
##############################################################################

df = pd.read_excel(sys.argv[1])

def fix(value):
    #print(value, type(value))
    if type(value) is not str:
        return str(value).zfill(6)
    else:
        return value
df['Fabric#'] = df['Fabric#'].map(fix)

tlrd = '''TLRD BRND 
OO at Mill '''
def fix2(value):
    return int(value)
df[tlrd] = df[tlrd].map(fix2)
df.to_csv(sys.argv[2], index=False,header=True )



