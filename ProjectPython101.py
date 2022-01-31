names_number = {'1111111111':'Amal','2222222222':'Mohammed','3333333333':'Khadijah','4444444444':'Abdullah','5555555555':'Rawan','6666666666':'faisal','7777777777':'Layla'}

search = int(input("""Enter number of option
            1) Search by phone number
            2)  Search by name
            3)  Add new phone number and name by write add \r\n"""))

def search_by_name(name):
    val_list = list(names_number.values())
    key_list = list(names_number.keys())
    if name in val_list:
        pos = val_list.index(name)
        print(key_list[pos])
    else:
        print("You don't have this name..")

def search_by_num(num):
    if num in names_number:
        print(names_number[num])
    elif len(num) != 10:
        print("This is invalid number")
    else:
        print("Sorry, the number is not found")

def add_to_dict(key, value):
    names_number[key] = value

def main():
    if search == 1:
        num = input("Enter the phone number: ")
        search_by_num(num)
    elif search == 3:
        key = input("enter phone number ")
        value = input("enter name")
        add_to_dict(key,value)
        print(f'all names you have in your dictionary {names_number.values()}')
    else:
        search_by_name(search)
if __name__ == '__main__':
    main()