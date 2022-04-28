import time

try:
    data_base
except NameError:
    data_base = dict() #НЕ ЧІПАЙ ВОНО ТЕБЕ УБЄ !!!!!!

try:
    info_base
except NameError:
    info_base = dict() #НЕ ЧІПАЙ ВОНО ТЕБЕ УБЄ !!!!!!    


#REgistration
def no(data_base):
    k = input("Сreate a password \n") 
    l = input("Create a login \n")
    
    data_base[l]=dict()
    data_base[l]["password"]=k

    return data_base


def yes(data_base, info_base):
    login = input("Enter login \n")
    password =str(input("Enter password \n"))
    if login in data_base.keys():
        if password == data_base[login]["password"]:
            
            print("+")
            info_base=info(info_base, login)
            
      
def info(info_base, login):
    name = input("Input your name \n")
    sex = input("Input your sex \n")
    age = str(input("Input your age \n"))
    
    info_base[login] = dict()
    info_base[login]["name"] = name
    info_base[login]["age"] = age
    info_base[login]["sex"] = sex
    return info_base



#Enter
print ("Are you registered ?")
time.sleep(3)

success = 0 
while success == 0:
    l = input("Chose answer Yes/No \n")
    if l == 'Yes':
        b=yes(data_base, info_base)
        success = 1
    elif l == 'No':
        a=no(data_base)
        success = 1
    else:
        print("Not entered correctly, please try again")
        




    

    
