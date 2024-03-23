
class StaffServices:   
    #update information related to staff and hotel
    def updatestaff(logid,value, choice,self):
        query = ("SELECT s.hotel_id FROM user AS u JOIN staff AS s ON u.id = s.id where u.id='{}';".format(logid))  
        self.cursor.execute(query)
        id = self.cursor.fetchall()
        hotel_id=id[0]
        
        if id:
            if choice==1:
                query=("update \"user\" set name='{}' where id={}".format(value,logid))
                self.cursor.execute(query)
                query1=("update staff set name='{}' where id={}".format(value,logid))
                self.cursor.execute(query1)
                return ("Updated")
            elif choice==2:
                query=("update \"user\" set email='{}' where id={}".format(value,logid))
                self.cursor.execute(query)
                query=("update staff set name='{}' where id={}".format(value,logid))
                self.cursor.execute(query1)
                return ("Updated")
            elif choice==3:
                query=("update \"user\" set password='{}' where id={}".format(value,logid))
                self.cursor.execute(query)
                query=("update staff set name='{}' where id={}".format(value,logid))
                self.cursor.execute(query1)
                return ("Updated")
            elif choice == 4:
                query1=("update hotel_id set name='{}' where id={}".format(value,hotel_id))
                self.cursor.execute(query1)
                return ("Updated")
            else:
                return ("something went wrong")
            
        self.connection.commit()
        self.cursor.close()     
            

            
            
            
    #To view all the bookings for a hotel for the staff to see        
    def viewbookstaff(self,logid):
        my_dict = {}

        # Retrieve the hotel_id associated with the staff's login ID
        query_get_hotel_id = "SELECT hotel_id FROM staff WHERE id={}".format(logid)
        self.cursor.execute(query_get_hotel_id)
        hotel_id_result = self.cursor.fetchone()
        hotel_id = hotel_id_result[0]

            # Retrieve all room IDs associated with the hotel_id
        query_get_room_ids = "SELECT id FROM room WHERE hotel_id={}".format(hotel_id)
        self.cursor.execute(query_get_room_ids)
        room_ids = [row[0] for row in self.cursor.fetchall()]
        
        # Check if there are room IDs associated with the hotel
        if room_ids:
            # Retrieve all bookings for the current room_id
            for room_id in room_ids:
                query_get_bookings_for_room = "SELECT roomno, from_date, to_date, total_price FROM booking WHERE room_id = {}".format(room_id)
                self.cursor.execute(query_get_bookings_for_room)
                bookings_for_room = self.cursor.fetchall()
                for row in bookings_for_room:
                    my_dict["room_no"] =row[0]
                    my_dict["from date"] =row[1].strftime("%Y-%m-%d")
                    my_dict["to date"] =row[2].strftime("%Y-%m-%d")
                    my_dict["total price"] =row[3]
                    # Commit changes and close cursor and connection after processing all rooms
                    self.connection.commit()
                    self.cursor.close()
                    return my_dict
        else:
             # No room IDs associated with the hotel
             return "No room IDs associated with the hotel"
