name=input('your name :')
age=input('your age :')
sex=input('your sex :')
work=input('your work :')



person={
    'name':name,
    'age':age ,
    'sex':sex
}

person["work"]=work








#print(person['work'])

# print('name' in person)

# if 'name' in person :
#     print (person)

def program() :
    users=input('keys or values :')

    if 'keys'==users :
       print (list(person.keys()))
    elif 'values'==users :
        print(list(person.values()))
    else :
        print('write correctly and exactly') 

program()         

            
