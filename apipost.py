from services.user import *
from services.booking import *

def handle_createuser(self,json_data):
    name=json_data.get('name','')
    email=json_data.get('email','')
    password=json_data.get('password','')
    if not name or not email or not password:
        # Missing required fields
        self.send_error(400, 'Missing required fields')
        return

    UserServices.createuser(self,name,email,password)
    self.send_response(200)
    self.send_header("Content-type", "text/html")
    self.end_headers()
    html_content = "<html><body><h1>POST Request Received!</h1></body></html>"
    self.wfile.write(html_content.encode("utf-8"))
    
def handle_booking(self,json_data):
    logid = json_data.get('userid', '')
    roomid= json_data.get('roomid', '')
    fromdate  = json_data.get('fromdate', '')
    todate = json_data.get('todate', '')

    BookingServices.book(self,logid,roomid,fromdate,todate)
    self.send_response(200)
    self.send_header("Content-type", "text/html")
    self.end_headers()
    html_content = "<html><body><h1>POST Request Received!</h1></body></html>"
    self.wfile.write(html_content.encode("utf-8"))
    
def handle_default(self):
    self.send_response(400)
    self.send_header("Content-type", "text/html")
    self.end_headers()
    html_content = "<html><body><h1>Unknown Command not found.</h1></body></html>"
    self.wfile.write(html_content.encode("utf-8"))
    
