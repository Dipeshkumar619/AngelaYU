# import pandas as pd
# df=pd.read_csv('weather_data.csv')
# print(df.head())
# with open('weather_data.csv') as csv:
#     data=csv.readlines()
#     print(data)
# import csv
#
# with open('weather_data.csv') as file:
#     data=csv.reader(file)
#     temperature=[]
#     for row in data:
#         print(row)
#         if row[1] !="temp":
#             temperature.append(row[1])
#     print(temperature)
# import pandas
# import pandas as pd
# data=pd.read_csv('weather_data.csv')
# print(data)
# print(type(data))
#
# data_dict=data.to_dict()
# print(data_dict)
#
# temp_list=data["temp"].to_list()
# avg=sum(temp_list)/len(temp_list)
# print(avg)
# print(data["temp"].max())
# print(data[data.day=="Monday"])
# print(data[data.temp==data.temp.max()])
# monday_temp=data.temp[data.day=="Monday"]
# fahrenheit=(monday_temp*9)/5
# print(fahrenheit)

# Create data frame from scrach
# data_dict={
#     "students": ["Amy","James","Angela"],
#     "scores": [76,56,65]
# }
#
# new_data=pandas.DataFrame(data_dict)
# new_data.to_csv("new_data.csv")
import pandas
import pandas as pd
data=pd.read_csv('squirrel_data.csv')
colors=data["Primary Fur Color"]
grey_squirrels_count=len(data[data["Primary Fur Color"]=="Gray"])
print(grey_squirrels_count)
black_squirrels_count=len(data[data["Primary Fur Color"]=="Black"])
print(black_squirrels_count)
red_squirrels_count=len(data[data["Primary Fur Color"]=="Cinnamon"])
print(red_squirrels_count)

data_dict={
    "Fur_colors": ["Gray","Cinnamon","Black"],
    "Count": [grey_squirrels_count,red_squirrels_count,black_squirrels_count]
}

pandas.DataFrame(data_dict).to_csv("squirrelcolors.csv")
