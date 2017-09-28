'''
How old are you in number of days? It's easy to calculate - just subtract your birthday from today. We could make this a real challenge though and count the difference between any dates.

You are given two dates as tuples with three numbers - year, month and day. For example: 19 April 1982 will be (1982, 4, 19). You should find the difference in days between the given dates. For example between today and tomorrow = 1 day. The difference will always be either a positive number or zero, so don't forget about absolute value.

Input: Two dates as tuples of integers.

Output: The difference between the dates in days as an integer.

Example:

days_diff((1982, 4, 19), (1982, 4, 22)) == 3
days_diff((2014, 1, 1), (2014, 8, 27)) == 238
days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    
1
2
3
4
How it is used: Python has batteries included, so in this mission you will need to learn how to use completed modules so that you don't have to invent the bicycle all over again.

Precondition: Dates between 1 january 1 and 31 december 9999. Dates are correct.
'''
'''
def days_diff(date1, date2):
    months_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    dict_day_in_months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    date1_days = date1[2]
    date2_days = date2[2]
    date1_months = date1[1]
    date2_months = date2[1]
    date1_years = date1[0]
    date2_years = date2[0]

    days_in_months = 0
    lower_days_left = 0
    upper_days_left = 0
    total_days = 0

    if date1_months>date2_months or date1_years > date2_years :
        temp = date1_months
        date1_months = date2_months
        date2_months = temp

        temp1 = date1_days
        date1_days = date2_days
        date2_days = temp1

        temp2 = date1_years
        date1_years = date2_years
        date2_years = temp2

    print(date1_years,date1_months,date1_days)
    print(date2_years, date2_months, date2_days)

    range_of_months = months_list[date1_months:date2_months]
   # print(range_of_months)

    for i in range_of_months:
        days_in_months += dict_day_in_months[i]

   # print(days_in_months)
    date1_days_left = dict_day_in_months[date1_months] - date1_days
    date2_days_left = dict_day_in_months[date2_months] - date2_days

    if (date1_years== date2_years):
        if date1_months == date2_months:
            total_days = date2_days - date1_days
            return total_days
        else:
            total_days = date1_days_left + days_in_months - date2_days_left
            return total_days
    else:
        total_days = date1_days_left + days_in_months - date2_days_left + 365* (date2_years-date1_years)
        return total_days





'''

import datetime


def days_diff(date1, date2):
    """
        Find absolute diff in days between dates
    """
    days = (datetime.datetime(*date2) - datetime.datetime(*date1)).days
    if days < 0:
        return -days
    return days

