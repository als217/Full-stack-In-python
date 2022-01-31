"""
    Version 2.0
    Abdullah    | 31 Jan 2022
"""

import datetime
import sys

list_names = []
list_date = []
def convertToDate(date):
    brithdate = datetime.datetime.strptime(date,"%d-%m-%Y").date()
    return brithdate

# input number of persons
select = int(input('Enter number of persons you want: '))
# for give names and dates
for i in range(0,select):
    name = input("Enter name: ")
    list_names.append(name)
    date = input("Enter Birthday date DD-MM-YYYY: ")
    list_date.append(date)

try:    #if the user Enter filed date the program stop.
    list_date = list(map(convertToDate,list_date))
except:
    print("Invalid date")
    list_names.clear()
    list_date.clear()
    sys.exit()

currentDate = datetime.datetime.now().date()

def ages(list_date):
    list_ages = []
    for date in list_date:
        one_or_zero = ((currentDate.month, currentDate.day) < (date.month, date.day))
        years_diff = currentDate.year - date.year
        age = years_diff - one_or_zero
        list_ages.append(age)
    return list_ages


def printDay(list_date):
    list_days = []
    for day in list_date:
        day = datetime.datetime.strftime(day,"%A")
        list_days.append(day)
    return list_days

def maxage(list_ages):
    age = max(list_ages)
    index_max = list_ages.index(age)
    name_max = list_names[index_max]
    return name_max
def Min(list_ages):
    age = min(list_ages)
    index_min = list_ages.index(age)
    name_min = list_names[index_min]
    return name_min


def main():
    list_ages = ages(list_date)
    list_days = printDay(list_date)

    for i in range(len(list_names)):
        print(f"%s is %d years old and she/he was born on %s"% (list_names[i],list_ages[i],list_days[i]))

    if len(list_names) > 1:
        name_max = maxage(list_ages)
        name_min = Min(list_ages)
        print('The oldest one is {0}'.format(name_max))
        print('The youngest one is {0}'.format(name_min))
    else:
        print('There is no oldest or youngest person')

    print("Total People:{0}".format(len(list_names)))

if __name__ == '__main__':
    main()
