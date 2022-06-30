import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv("https://raw.githubusercontent.com/globaldothealth/monkeypox/main/timeseries-confirmed.csv")
#covid_df = pd.read_csv("./covid-data/worldwide-aggregate.csv")



if __name__ == '__main__':	
	#print(pd.to_datetime(df.Date_entry[len(df.Date_entry)-1])-pd.to_datetime(df.Date_entry[0]))	
	plt.plot([i+1 for i, d in enumerate(df.Date)], df.Cumulative_cases)
	#plt.plot([i+1 for i, d in enumerate(covid_df.Date) if i < 25], covid_df.Confirmed[0:25])
	plt.title('2022 Global Monkeypox Outbreak ')
	plt.xlabel('Days')
	plt.ylabel('Number of cases')
	plt.grid()
	plt.show()
	