from services.hashpassword import generate_hash_password


class UserServices:
    
    #TO show info for a specific user
    def showuser(self,logid):
    
        query2 = ("SELECT id,name FROM \"user\" where id={}".format(logid))  
        self.cursor.execute(query2)
        id = self.cursor.fetchone()
        my_dict = {}
        my_dict["id"] =id[0]
        my_dict["name"] =id[1]
        self.connection.commit()
          
        return my_dict
        
        
    #function to create
    def createuser(self,name,email,password):
    #queries
        salt,hash_password=generate_hash_password(password)
        query = "INSERT INTO \"user\" (name, email, salt, hash_password) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(query, (name, email, salt, hash_password))

        self.connection.commit()

        
        
    # Function to update Information
    def updateuser(logid,choice,value,self):
    #updating 
    #1-name 2-email 3-password
        query2 = ("SELECT id FROM \"user\" where id={}".format(logid))  
        self.cursor.execute(query2)
        id = self.cursor.fetchall()
        if id:
            if choice==1:
                query=("update \"user\" set name='{}' where id={}".format(value,logid))
                self.cursor.execute(query)
            elif choice==2:
                query=("update \"user\" set email='{}' where id={}".format(value,logid))
                self.cursor.execute(query)
            elif choice==3:
                query=("update \"user\" set password='{}' where id={}".format(value,logid))
                self.cursor.execute(query)
        self.connection.commit()
        

    #delete customer
    def deleteuser(logid,self):
        query2 = ("SELECT id FROM \"user\" where id={}".format(logid))  
        self.cursor.execute(query2)
        id = self.cursor.fetchone()
        if id:
            query=("delete from \"user\" where id={}".format(logid))
            self.cursor.execute(query) 
            return True
        else:False
                
        self.connection.commit()
          

        

            
            

        
        