# def greet (name="Unknown name",time="unknown time") :
#     print (f'Hello good {time},{name}')


# greet() 
# greet("Kyaw Kyaw","morning") 
# greet(time="night",name="my lovely girl")

def greet (name="Unknown name",time="Unknown time") :
    print (f'Hello good {time},{name}.')
   

    question=(input("Do you have girlfriend? yes or no :"))
    if question == "yes" :
       print("I hope,you will be able to marry her.")
    else :
        print("Don't worry,you can find that.")   

greet(input("Your name :"),input("morning or afternoon or night :")) 


   
