from user import user
from usermanager import usermanager

class Loginsystem:
    def login(self):
        mailid=input("enter mailid:")
        password=input("password:")
        u=usermanager.finduser(mailid,password)    
        if u :
            print("login successfully!! Welcome")
        else:
            print("invalide mailid and password!!!! try again!!!")

    def register(self):
        name=input("name:")
        mobile=int(input("Mobile no:"))
        mailid=input("emailid :")
        password=input("password :")
        u=user(name,mobile,mailid,password)   
        usermanager.adduser(u)                 
        
    def guestlogin(self):
        pass

    def validoption(self,choice):
        if choice ==1:
            self.login()
        elif choice ==2:
            self.register()
        elif choice  ==3:
            self.guestlogin()
        elif choice ==4:
            print("thankyou")
            exit()   
        else:
            print("invalid option...")  

class Foodapp:
    loginoption={1:"login", 2:"register", 3:"guest", 4:"exit"}
    @staticmethod
    def Init():
        print("Welcome to online food app!!!!!")
        loginsystem=Loginsystem()
        while True:
            for option in Foodapp.loginoption:
                print(f"{option}.{Foodapp.loginoption [option]}",end=" ")
            print()
            try:
               choice=int(input("enter your option:"))
               loginsystem.validoption(choice)
               
            except ValueError:
                print("please enter your correct choice")   
Foodapp.Init()  
       
   
     
      

        

