import os

def show_contacts(file_name):
    os.system('CLS')
    with open(file_name, 'r') as file:
        data =  file.readlines()
        
        for contact in data:
            print(contact, end='')
            
    input('\npress any key')

def add_contacts(file_name):
    os.system('CLS')
    with open(file_name, 'a') as file:
        res = ''
        res += input('Input a  name of contact ')+' '
        res += input('Input a surname of contact ')+' '
        res += input('Input a phone number of contact ')+' '
        
        file.write('\n'+res)
    input('\npress any key')

def search_contact(file_name):
    os.system('CLS')
    target = input('\nInput a name of contact for searching')
    
    with open(file_name, 'r') as file:
        contacts =  file.readlines()
        
        
        for contact in contacts:
            if target in contact:
                print(contact)
                break
        else: print('there is no contacts in this name.')
    input('\n press any key')
   
def drawing():
    print('1 - show contacts')
    print('2 - add contacts')
    print('3 - seach contacts ')
    print('4 - delete contact')
    print('5 - change contact')
    print('6 - exit')  
 
def main(file_name):
    while True:
        os.system('CLS')
        drawing()
        user_chois = int(input('Input number from 1 to 5\n'))
        if user_chois ==  1:
            show_contacts(file_name)
        elif user_chois == 2:
            add_contacts(file_name)
        elif user_chois == 3:
            search_contact(file_name)
        elif user_chois == 4:
            delete(file_name) 
        elif user_chois == 5:
            change(file_name)  
        elif user_chois == 6:
            print('Have a nice day!')
            return


def delete(file_name):
    del_contact = input('Input word for deleted ')
    with open(file_name, "r") as f:
        
        data = f.readlines()
        
    with open(file_name, "w") as f:
      
        for line in data :
            if del_contact not in line:
                f.write(line)
                
def change(file_name):
    change_contact = input('Input word for changed ')
    with open(file_name, "r") as f:
        data = f.readlines()
        
    with open(file_name, "w") as f:
        for line in data :
            if change_contact not in line:
                f.write(line)
            else: 
                
                print(line+'\n')
                res = ''
                res += input('Input a  name of contact ')+' '
                res += input('Input a surname of contact ')+' '
                res += input('Input a phone number of contact ')+' \n'
                f.write(res)

main('test.txt')
        
        


