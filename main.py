import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from viewingActivity import read_file, user, save_values, totalDuration


def main():
    df = read_file()
    users = user(df)
    users_len = len(users)
    flag = 1
    print(f"Netflix data Analysis\n\nThere are {users_len} users on this account {users}")
    
    while flag != 0:
        for i in range(users_len):
            print(f"Press {i+1} for {users[i]}")
        print("Press 0 to exit")

        user_choice = input("Enter value: ")   
        if user_choice == "0":
            flag = 0


        user_data = save_values(df,users[int(user_choice)-1])
        durationList = totalDuration(user_data)

        if flag != 0:
            infoFlag = 1
            while infoFlag != 0:      
                print("\nSelect one of the following:")
                print("1. Total time spent watching")
                print("2. Time spent watching per month")
                print("3. Most watched shows")
                print("0. to exit")
                value = input("Enter a value: ")

                if value == "0": 
                    infoFlag = 0
                elif value == "1": 
                    durationSelect(durationList)
                elif value == "2":
                    monthSelected(user_data)
                elif value == "3":
                    titles(user_data)


def titles(df):
    df2 = df[['Title','Duration']].copy()

    duration = []
    titles = []

    for index, row in df2.iterrows():
        hhmmss = row["Duration"]
        (h, m, s) = hhmmss.split(':')
        result = round((int(h) * 3600 + int(m) * 60 + int(s))/60)
        title = row['Title']

        duration.append(result)
        titles.append(title.split(':')[0])

    dict = {'Duration': duration, 'Title': titles}
    df_title = pd.DataFrame(dict)
    sumTitle = df_title.groupby(['Title'],as_index=False, sort=True)["Duration"].sum()

    topTitle = sumTitle.nlargest(10, 'Duration')

    topTitle.plot.bar(x='Title', y='Duration',title="Mins Watched per Show Top 10")
    plt.show(block=True)

def monthSelected(df):
    df['Start Time'] = df['Start Time'].str.split(' ').str[0]

    year_month = []
    duration = []

    for index, row in df.iterrows():
        year_month.append(getYearMonth(row["Start Time"]))
        duration.append(row["Duration"])

    dict = {"Date": year_month, "Duration": duration}
    df_month = pd.DataFrame(dict)

    year_month = list(dict.fromkeys(year_month))
    new_dict = {}
    for i in range(len(year_month)):
        new_dict[year_month[i]] = 0
        for index, row in df_month.iterrows():
            if year_month[i] == row["Date"]:
                hhmmss = row["Duration"]
                (h, m, s) = hhmmss.split(':')
                result = int(h) * 3600 + int(m) * 60 + int(s)
                new_dict[year_month[i]] += result

    dateMonth = []
    timeWatch = []

    for x, y in new_dict.items():
        dateMonth.append(x)
        timeWatch.append(y)

    df_plot = pd.DataFrame({"Month": dateMonth,"Time": timeWatch})
    
    df_plot.plot.bar(x='Month', y='Time',title="Seconds Watch per Month")
    plt.show(block=True)


def durationSelect(durationList):
    print(f"{durationList[0]} seconds\nApprox {durationList[1]} mins\nApprox {durationList[2]} hours\nApprox {durationList[3]} days")

def getYearMonth(s):
      return s.split("-")[0] + "-" + s.split("-")[1]


if __name__ == "__main__":
    main()

