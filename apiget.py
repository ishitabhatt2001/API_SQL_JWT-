
import json
from services.staff import *
from services.user import *
from services.room import *
from services.booking import *

# Pascal Case
class getuser:
    def userinfo(self,query_params): 
        user_id = query_params['id'][0]

        # Assuming you have a function to fetch data based on user_id
        data = UserServices.showuser(self,user_id)

        # Send response headers
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        # Send the response content (assuming data is a dictionary)
        response_content = json.dumps(data)
        self.wfile.write(response_content.encode())
        
class getroom:        
    def roomtype (self):
        # Assuming you have a function to fetch data based on user_id
        data = RoomServices.viewroomstype(self)

        # Send response headers
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        # Send the response content (assuming data is a dictionary)
        response_content = json.dumps(data)
        self.wfile.write(response_content.encode())    
        
    def viewroom(self,query_params):
        type_id = query_params['id'][0]

        # Assuming you have a function to fetch data based on user_id
        data = RoomServices.viewrooms(self,type_id)

        # Send response headers
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

            # Send the response content (assuming data is a dictionary)
        response_content = json.dumps(data)
        self.wfile.write(response_content.encode())
    
class getbooking:
    def viewbookuser(self,query_params): 
        user_id = query_params['id'][0]

        # Assuming you have a function to fetch data based on user_id
        data = BookingServices.viewbookuser(self,user_id)

        # Send response headers
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        response_content = json.dumps(data)
        self.wfile.write(response_content.encode())  
        
class getstaff:
    def viewbookstaff(self,query_params): 
        staff_id = query_params['id'][0]

        # Assuming you have a function to fetch data based on user_id
        data = StaffServices.viewbookstaff(self,staff_id)

        # Send response headers
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        response_content = json.dumps(data)
        self.wfile.write(response_content.encode())  