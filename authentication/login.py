import bcrypt
import base64

class LoginServices:   

    def login(self,email,password):
        # Query to retrieve user id by email
        query1 = ("SELECT salt, hash_password FROM \"user\" WHERE email = %s;")
        self.cursor.execute(query1, (email,))
        result = self.cursor.fetchone()

        if result:
            salt = result[0]
            hashed_password=result[1]
            # Check if salt and hashed_password_from_db are not None
            if salt and hashed_password:
                # Hash the password with the retrieved salt
                hashed_password1 = bcrypt.hashpw(password.encode('utf-8'), bytes(salt))
                # Compare the hashed passwords
                if hashed_password1 ==bytes(hashed_password):
                    
                    # Passwords match
                    self.connection.commit()
                    return True
        else:
            self.connection.commit()
            return False
        

    def logintype(logid,self):
    #checking if login is staff or user           
        query = ("SELECT id FROM staff where id={}".format(logid))  
        self.cursor.execute(query)
        id = self.cursor.fetchone()        
        if id:
            self.connection.commit()
            self.cursor.close() 
            return ("staff")
        else:
            self.connection.commit()
            self.cursor.close() 
            return ("user")