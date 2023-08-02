import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib
matplotlib.rcParams['font.size'] = 10

# Load the data into a dataframe
df = pd.read_excel('FS Project Pool.xlsx', sheet_name='Operations')
df = df.fillna('')
print(df)
# Extracting data for each state
states = df.iloc[1:9, :]  # Adjust these indices if necessary

# Plotting SSG and GSP trend for each year by state
plt.figure(figsize=(18, 12))
for i, (index, state) in enumerate(states.iterrows()):
    plt.subplot(2, 4, i+1)
    plt.plot(range(2018, 2023), state[1::3], label='SSG')  # SSG data
    plt.plot(range(2018, 2023), state[2::3], label='GSP')  # GSP data
    plt.title(state[0])  # State name
    plt.xlabel('Year')
    plt.ylabel('Sales')
    plt.legend()


plt.tight_layout()
plt.show()
