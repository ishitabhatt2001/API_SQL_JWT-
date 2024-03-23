
class RoomServices:   
    #view rooms type like delux etc...
    def viewroomstype(self):
        query=("select * from roomtype ")
        self.cursor.execute(query)
        type=self.cursor.fetchall()
        self.connection.commit()
        self.cursor.close()
        return type
        
    #view all the rooms available                
    def viewrooms(self,id):
        query=("SELECT r.id, r.status, r.roomno, r.price_per_night, r.capacity, t.name FROM room AS r JOIN roomtype AS t ON r.typeid = t.id where t.id='{}' and r.status='available';".format(id))
        self.cursor.execute(query)
        id=self.cursor.fetchall()
        my_dict = {}
        if id:
            for row in id:
               my_dict["id"] =row[0]
               my_dict["status"] =row[1]
               my_dict["room_no"] =row[2]
               my_dict["price/night"] =row[3]
               my_dict["capacity"] =row[4]
               my_dict["name"] =row[5]
        self.connection.commit()
        self.cursor.close()
        return my_dict