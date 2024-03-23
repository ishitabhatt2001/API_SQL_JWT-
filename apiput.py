from services.staff import StaffServices
from services.user import UserServices

#update user
def update_user(self,put_param):
    logid = put_param.get('userid', [''])[0]
    choice= put_param.get('choice', [''])[0]
    value  = put_param.get('value', [''])[0]

    UserServices.updateuser(logid,choice,value,self)
    self.send_response(200)
    self.send_header("Content-type", "text/html")
    self.end_headers()
    html_content = "<html><body><h1>POST Request Received!</h1></body></html>"
    self.wfile.write(html_content.encode("utf-8"))
    
#update staff    
def update_staff(self,put_param):
    logid = put_param.get('userid', [''])[0]
    value= put_param.get('value', [''])[0]
    choice  = put_param.get('choice', [''])[0]
    

    StaffServices.updatestaff(logid,value, choice,self)
    self.send_response(200)
    self.send_header("Content-type", "text/html")
    self.end_headers()
    html_content = "<html><body><h1>POST Request Received!</h1></body></html>"
    self.wfile.write(html_content.encode("utf-8"))