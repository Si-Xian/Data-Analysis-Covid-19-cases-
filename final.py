#Q1 Get the latest number of confirmed, deaths, recoveded and active cases of COVID19 Country wise.

import pandas as pd
covid_data= pd.read_csv("04-08-2020.csv")
covid_data['Active'] = covid_data['Confirmed'] - covid_data['Deaths'] - covid_data['Recovered'] # using formula to obtain new attribute
result = covid_data.groupby('Country_Region')['Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index() # Groupby + Sum to obtain Countryw wise; Reset index is used to remove the index that is set on the Country_Region column.
print(result) 

 #Q2 Get the cases detail of US province wise.

import pandas as pd
covid_data= pd.read_csv('04-08-2020.csv')
cd_data = covid_data[covid_data['Country_Region']=='US']
cd_data = cd_data[['Province_State', 'Confirmed', 'Deaths', 'Recovered']]
result = cd_data.sort_values(by='Confirmed', ascending=False)
result = result.reset_index(drop=True)
print(result)

#Q3 Get top 10 countries of Confirmed Cases for the COVID19
import pandas as pd
covid_data= pd.read_csv('04-08-2020.csv', usecols = ['Country_Region', 'Last_Update', 'Confirmed'])
result = covid_data.groupby('Country_Region').max().sort_values(by='Confirmed', ascending=False)[:10]
pd.set_option('display.max_column', None)
print("Dataset information: ")
print(result)

#Q4 Visualize the state wise combined number of cases.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
covid_data= pd.read_csv("04-08-2020.csv")
combine_us_data = covid_data[covid_data['Country_Region']=='US'].drop(['FIPS','Admin2','Last_Update','Country_Region','Lat','Long_','Combined_Key','Incidence_Rate','Case-Fatality_Ratio'], axis=1)
combine_us_data = combine_us_data[combine_us_data.sum(axis = 1) > 0]
combine_us_data = combine_us_data.groupby(['Province_State'])['Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index()
combine_us_data = pd.melt(combine_us_data, id_vars='Province_State', value_vars=['Confirmed', 'Deaths', 'Recovered', 'Active'], value_name='Count', var_name='Case')
sns.barplot(data=combine_us_data, x='Province_State', y='Count',hue='Case').set_title('USA State wise combine number of confirmed, deaths, recovered, active COVID-19 cases')
plt.show()

#Q5 Plot a line chart for the data via Country wise where death greather than 200.
import pandas as pd
import matplotlib.pyplot as plt
covid_data= pd.read_csv('04-08-2020.csv', usecols = ['Last_Update', 'Country_Region', 'Confirmed', 'Deaths', 'Recovered'])
covid_data['Active'] = covid_data['Confirmed'] - covid_data['Deaths'] - covid_data['Recovered']
 
cv_data = covid_data.groupby(["Country_Region"])["Deaths", "Confirmed", "Recovered", "Active"].sum().reset_index()
cv_data = cv_data.sort_values(by='Deaths', ascending=False)
cv_data = cv_data[cv_data['Deaths']>200]
plt.figure(figsize=(1, 5))
plt.xticks(rotation = 75)
plt.plot(cv_data['Country_Region'], cv_data['Deaths'],color='red')
plt.plot(cv_data['Country_Region'], cv_data['Confirmed'],color='green')
plt.plot(cv_data['Country_Region'], cv_data['Recovered'], color='blue')
plt.plot(cv_data['Country_Region'], cv_data['Active'], color='black')

plt.title('Total Deaths(>200), Confirmed, Recovered and Active Cases by Country')

plt.show()


'''Q6  Write a Python program to list countries which have no. of percentage death is more than 10% out 
of confirmed case. '''
import pandas as pd
covid_data= pd.read_csv('04-08-2020.csv')
data = covid_data.groupby('Country_Region')['Confirmed', 'Deaths', 'Recovered'].sum().reset_index()
result = data[data['Deaths']/data['Confirmed']>0.1][['Country_Region', 'Confirmed', 'Deaths', 'Recovered']]
print(result)


'''Q7  Write a Python program to list countries which have no of percentage recovered is 80% out of 
confirmed case. '''
import pandas as pd
covid_data= pd.read_csv('04-08-2020.csv')
data = covid_data.groupby('Country_Region')['Confirmed', 'Deaths', 'Recovered'].sum().reset_index()
result = data[data['Recovered']/data['Confirmed']==0.8][['Country_Region', 'Confirmed', 'Deaths', 'Recovered']]
print(result)


#Q8 We need to create a stacked bar chart to Visualize the distribution of cases via the REGION TYPE.
import pandas as pd

import matplotlib.pyplot as plt 

#The 'continent.txt' is in the zip folder (I downloaded from google)
df=pd.read_csv("continent.txt")
df_new=df[['Continent_Name','Country_Name']]
df_new.to_csv('continent_new.txt', header=True, index=None)
covid_data= pd.read_csv("04-08-2020.csv")
c_data = covid_data.groupby(['Country_Region','Last_Update'])['Confirmed'].sum().reset_index()

for x in c_data['Country_Region']:
	if str(x) in str(df_new['Country_Name']):
		c_data['Continent']=df_new['Continent_Name']
group_=c_data.groupby(['Last_Update','Continent'])['Confirmed'].sum().reset_index()
group=group_[group_['Confirmed']>0]
print(group)
# i create a list from the printed dataframe .(As i tried many ways and failed.)
labels=['10/7','13/7','4/8','5/8 2pm','5/8 4pm']

SouthAmerica=[0,0,0,0,4941778]
Asia=[1,0,0,0,2215533]
Europe=[0,13,0,0,4512052]
NorthAmerica=[0,0,2,0,1850084]
Oceania=[0,0,0,332,511632]
Africa=[0,0,0,0,4453641]
Antarctica=[0,0,0,0,55051]
width=0.1
fig, ax=plt.subplots()
ax.bar(labels,Asia,width,label='Asia')
ax.bar(labels,SouthAmerica,width,label='SouthAmerica')
ax.bar(labels,Europe,width,label='Europe')
ax.bar(labels,NorthAmerica,width,label='NorthAmerica')
ax.bar(labels,Oceania,width,label='Oceania')
ax.bar(labels,Africa,width,label='Africa')
ax.bar(labels,Antarctica,width,label='Antarctica')

plt.show()
