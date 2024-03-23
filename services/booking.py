
class BookingServices:         
    #book user room          
    def book(self,logid,roomid,fromdate,todate):
        query=("SELECT roomno, price_per_night FROM room where id={}".format(roomid))
        self.cursor.execute(query)
        id1=self.cursor.fetchone()  
        print (id1[1])
        roomno=id1[0]
        total=id1[1]  
        query2 =("update room set status='{}' where id={}".format("booked",roomid))
        self.cursor.execute(query2)
        query1=("insert into booking (roomno, from_date, to_date, total_price, user_id, room_id) values ('{}','{}','{}',{},{},{})".format(roomno, fromdate, todate, total, logid, roomid))
        self.cursor.execute(query1)
        self.connection.commit()
        self.cursor.close()   
        return ("booked") 
            
    #cancel user booking           
    def cancelbook(roomid,self):
        query=("delete from booking where room_id={};"
            " update room set status='{}' where id={}".format(roomid,"available",roomid))
        self.cursor.execute(query)
        self.connection.commit()
        self.cursor.close() 
        return ("canceled")   
            
    # view customer bookings           
    def viewbookuser(self,logid):
        query =("SELECT roomno, from_date, to_date, total_price FROM booking where user_id={}".format(logid))
        self.cursor.execute(query)
        id = self.cursor.fetchall() 
        my_dict={}
        if id:
            for row in id:
               my_dict["room_no"] =row[0]
               my_dict["from date"] =row[1].strftime("%Y-%m-%d")
               my_dict["to date"] =row[2].strftime("%Y-%m-%d")
               my_dict["total price"] =row[3]
        self.connection.commit()
        self.cursor.close()
        return my_dict