import datetime
import re
import pandas as pd
import random


# FUNCTION TO CLEAN DATA AND CALCULATION OF DAYS

def number_days(date1, date2):
    date1clean = (re.findall(r'\d+', date1))  # returns only numbers
    date2clean = (re.findall(r'\d+', date2))  # returns only numbers
    final_date = datetime.datetime.strptime(date2clean[0], "%Y%m%d") \
                 - datetime.datetime.strptime(date1clean[0], "%Y%m%d")  # converts the numbers to a date format

    return final_date


# FUNCTION TO CREATE RAMDOM DATES

def random_dates(rdate1, rdate2):
    start_date = datetime.datetime.strptime(rdate1, "%Y%m%d")  # converts the numbers to a date format
    end_date = datetime.datetime.strptime(rdate2, "%Y%m%d")  # converts the numbers to a date format

    counter = 0
    return_list = []

    while counter < 100:  # number of rows for the new random dataset
        days_between_dates = (end_date - start_date).days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = datetime_to_int(start_date + datetime.timedelta(days=random_number_of_days))
        return_list.append(random_date)
        counter += 1

    return return_list


# FUNCTION TO CONVERT DATETIME TYPE TO INT

def datetime_to_int(dt):
    return str(dt.strftime("%Y%m%d"))


# MAIN SCRIPT

# FIRST DATAFRAME

dates_dic = {"i_date": ["20001020", "20190101", "20120101", "20130101", "20140101", "20110101", "20150101",
                        "20010101", "19990101", "19980203"],
             "final_date": ["20051020", "20200101", "20130101", "20140101", "20150101", "20130101", "20160101",
                            "20050101", "20010101", "19990203"]}

date_df = pd.DataFrame.from_dict(dates_dic)  # convert dictionary to a data.frame

days_dif = []

for index, row in date_df.iterrows():  # iterate trough rows of "date_df"
    result = number_days(row['i_date'], row['final_date'])  # calculate the days difference via function "number_days"
    days_dif.append(result)  # append the days difference to a list

date_df["Days_dif"] = days_dif  # insert a new column

# SECOND DATAFRAME, RANDOM DATE VALUES

i_date_list = random_dates("19900101", "19990101")
final_date_list = random_dates("19990102", "20200101")

random_dic = {"i_date": i_date_list, "final_date": final_date_list}  # create dictionary with random dates
random_df = pd.DataFrame.from_dict(random_dic)  # convert dictionary to a data.frame

days_dif2 = []

for index, row in random_df.iterrows():  # iterate trough rows of "date_df"
    result2 = number_days(row['i_date'], row['final_date'])  # calculate the days difference via function "number_days"
    days_dif2.append(result2)  # append the days difference to a list

random_df["Days_dif"] = days_dif2  # insert a new column

# JOIN THE TWO DATAFRAMES

# print(date_df)
# print(random_df)

frames = [date_df, random_df]

final_df = pd.concat(frames)


# add a new column with the difference in years through days_dif column



final_df["Years_dif"] = [str(final_df["Days_dif"]/365)[0]]

print(final_df)
