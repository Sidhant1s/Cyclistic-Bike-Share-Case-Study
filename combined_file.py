import glob
import pandas as pd

# 1. Find all your processed monthly CSV files in your directory
# (Update the path pattern to match where you saved your cleaned individual files)
all_files = glob.glob(r"D:\Cyclist_Capstone_project_202608-edited\Excel edited\2023 csv\*.csv")

# 2. Read and append each file into a list
df_list = []
for filename in all_files:
  df = pd.read_csv(filename)
  df_list.append(df)

# 3. Concatenate all monthly dataframes into one master dataframe
master_df = pd.concat(df_list, ignore_index=True)

# 4. Ensure timestamps are in proper datetime format across the master set
master_df['started_at'] = pd.to_datetime(master_df['started_at'],format='mixed', errors='coerce')
master_df['ended_at'] = pd.to_datetime(master_df['ended_at'],format='mixed', errors='coerce')


# 5. Export the final combined master dataset for your analysis phase
master_df.to_csv("Cyclistic_Master_Trip_Data.csv", index=False)

print(f"Successfully merged {len(all_files)} files.")
print(f"Total rows in master dataset: {len(master_df)}")