from user import user
class usermanager:
   __user=[]
   @classmethod
   def adduser(cls,userobj):
      if isinstance(userobj,user):
         cls.__user.append(userobj)
         print("Register Successfully!!!!")
      else:
           print("invalide user")  
   @classmethod
   def finduser(cls,mailid,pwd):
      for u in cls.__user:
         if u.mailid==mailid and u.password==pwd:
            return u
      return None 
       