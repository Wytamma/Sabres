import ivar_parse
import os
import pandas as pd

neworder = ['filename', 'REF', 'POS', 'ALT', 'REFPOSALT', 'TOTAL_DP', 'ALT_FREQ', 'REF_AA', 'ALT_AA', 'SNS', 'Protein', 'Mutation', 'Interest', 'Note']
drop_columns = ['Mutation']
def get_resistance_only(file, database, outfile):
    snpprofile_df = pd.DataFrame(ivar_parse.generate_snpprofile(file, database, outfile))
    snpprofile_df['filename'] = os.path.splitext(os.path.basename(file))[0]
    snpprofile_df=snpprofile_df.reindex(columns=neworder)
    resistance_df = snpprofile_df[snpprofile_df['Interest'].str.contains('Resistance')]
    resistance_df.drop(drop_columns, axis = 1, inplace = True)

    if resistance_df.empty == False:
        return resistance_df