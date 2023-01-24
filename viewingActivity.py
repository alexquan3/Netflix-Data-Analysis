import pandas as pd

def read_file():
    csv_file = "netflix-report/CONTENT_INTERACTION/ViewingActivity.csv"

    data = pd.read_csv(csv_file)

    df = pd.DataFrame(data)

    df.drop(["Attributes", "Supplemental Video Type","Device Type","Bookmark", "Latest Bookmark", "Country"], axis=1, inplace=True)
    return df

def user(df):
    unique_users = df['Profile Name'].unique()
    return unique_users

def save_values(df,unique_users):
    start_time = []
    duration = []
    title = []

    for index, row in df.iterrows():
        if row["Profile Name"] == unique_users:
            title.append(row["Title"]) 
            start_time.append(row["Start Time"]) 
            duration.append(row["Duration"])

    dict = {'Title': title, 'Start Time': start_time, 'Duration': duration}

    df_user = pd.DataFrame(dict)
    return df_user

def totalDuration(df):
    index = 0
    totalDuration = 0
    for index, row in df.iterrows():
        hhmmss = row["Duration"]
        (h, m, s) = hhmmss.split(':')
        result = int(h) * 3600 + int(m) * 60 + int(s)
        totalDuration += result
        index = index

    durationMin = totalDuration / 60
    durationhour = totalDuration / (3600)
    durationDay = durationhour / 24

    durationList = [int(totalDuration), int(durationMin), int(durationhour), int(durationDay)]
    return durationList
    