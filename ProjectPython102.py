import datetime
import sys
list_names = []
list_date = []
def convertToDate(date):
    brithdate = datetime.datetime.strptime(date,"%d-%m-%Y").date()
    return brithdate

select = int(input('Enter number of persons you want: '))
for i in range(0,select):
    name = input("Enter name: ")
    list_names.append(name)
    date = input("Enter Birthday date DD-MM-YYYY: ")
    try:
        convertToDate(date)
        list_date.append(date)
    except:
        print("Invalid date")
        sys.exit()
        list_date.clear()
        list_names.clear()


list_Bday = list(map(convertToDate,list_date))

currentDate = "1-1-2021"
currentDate = datetime.datetime.strptime(currentDate,"%d-%m-%Y").date()

list_ages = []
for date in list_Bday:
    one_or_zero = ((currentDate.month, currentDate.day) < (date.month, date.day))
    years_diff = currentDate.year - date.year
    age = years_diff - one_or_zero
    list_ages.append(age)

list_days=[]
for day in list_Bday:
    day = datetime.datetime.strftime(day,"%A")
    list_days.append(day)

max = max(list_ages)
index_max = list_ages.index(max)
name_max = list_names[index_max]
min = min(list_ages)
index_min = list_ages.index(min)
name_min = list_names[index_min]


def main():
    for i in range(0,len(list_names)):
        print(f"%s is %d years old and she/he was born on %s"% (list_names[i],list_ages[i],list_days[i]))
    if len(list_names) > 1:

        print('The oldest one is {0}'.format(name_max))
        print('The youngest one is {0}'.format(name_min))
    else:
        print('There is no oldest or youngest person')

    print("Total People:{0}".format(len(list_names)))

if __name__ == '__main__':
    main()