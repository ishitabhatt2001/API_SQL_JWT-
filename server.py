import time
import jwt
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from apiget import getuser,getroom,getbooking,getstaff
from apipost import handle_createuser, handle_booking, handle_default
from apiput import update_user,update_staff
from urllib.parse import urlparse,parse_qs
from helpers.connection import establish_database_connection
from services.booking import *
from services.user import *
from authentication.login import *

# Secret key for signing and verifying tokens (keep this secret!)
SECRET_KEY = "ishitabhatt"
TOKEN_EXPIRATION_TIME = 3600  # in seconds
hostName = "localhost"
port = 8000



class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.connection, self.cursor = establish_database_connection()
        
            # Check Authorization header for JWT token
        def autherization(self):
            auth_header = self.headers.get('Authorization')
            if auth_header:
                try:
                    token = auth_header.split()[1]
                    # Verify JWT token
                    decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
                    print(decoded_token,"JWT token")
                    username = decoded_token['username']
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({'message': f'Hello, {username}! This is a protected resource.'}).encode('utf-8'))
                    return True
                
                except jwt.ExpiredSignatureError:
                    self.send_response(401)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({'error': 'Token expired'}).encode('utf-8'))
                    
                except (jwt.InvalidTokenError, IndexError):
                    self.send_response(401)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({'error': 'Invalid token'}).encode('utf-8'))
            else:
                self.send_response(401)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'No token provided'}).encode('utf-8'))
            
                
            #do check why the hashong is not getting same
        if self.path == '/favicon.ico':
            # Respond with a 200 status code and an empty response for favicon.ico
            self.send_response(200)
            self.end_headers()
            return
        
        # Parse the URL to extract the path and query parameters

        parsed_url = urlparse(self.path)
        path = parsed_url.path
        query_params = parse_qs(parsed_url.query)
        
        # if path.incldues("/protected")
        
        # Check the path and perform corresponding actions based on the conditions
        if path=='/protected/showuser/'and 'id' in query_params:
            if autherization(self):
                getuser.userinfo(self,query_params)
            else :
                print ("no autherization")
            
        elif path=='/protected/viewroomtype':
            if autherization(self):
                getroom.roomtype(self)
            else :
                print ("no autherization")
            
            
        elif path=='/protected/viewrooms/' and 'id' in query_params:
            getroom.viewroom(self,query_params)
            
        elif path=='/protected/viewuserbooking/' and 'id' in query_params:
            getbooking.viewbookuser(self,query_params)
        
        elif path=='/protected/viewstaffbooking/' and 'id' in query_params:
            getstaff.viewbookstaff(self,query_params)
    
        self.cursor.close()
           
           
            
    def do_POST(self):
        self.connection, self.cursor = establish_database_connection()
        
        if self.path == '/login':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            username = data.get('username')
            password = data.get('password')

            if LoginServices.login(self,username, password):

                # Generate JWT token
                issued_at = time.time()
                expiration_time = issued_at + TOKEN_EXPIRATION_TIME
                token_payload = {
                    'username': username,
                    'iat': issued_at,
                    'exp': expiration_time
                }
                token = jwt.encode(token_payload, SECRET_KEY, algorithm='HS256')
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'token': token}).encode('utf-8'))
            else:
                self.send_response(401)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'Unauthorized'}).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            
                
            
        # Parse the URL to extract the path and parameters
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        

        if path=='/protected/post':
            command = self.headers.get('command', '')

            # Read JSON data from the request body
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')

            try:
                json_data = json.loads(post_data)
            except json.JSONDecodeError:
                self.send_error(400, 'Invalid JSON')
                return
        
            if command == 'createuser':
                try:
                    # Handle the first command
                    handle_createuser(self,json_data)
                except Exception as e:
                    self.send_error(500, str(e))
            elif command == 'bookroom':
                # Handle the second command
                handle_booking(self,json_data)
            else:
                # Handle an unknown or default case
                handle_default(self,json_data)
                
                
                
            
    def do_put(self): 
        self.connection, self.cursor = establish_database_connection()
        # Parse the URL to extract the path and parameters +data
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        content_length = int(self.headers['Content-Length'])
        put_data = self.rfile.read(content_length).decode('utf-8')
        command = self.headers.get('command', '')

        try:
            put_param = json.loads(put_data)
        except json.JSONDecodeError:
            self.send_error(400, 'Invalid JSON')
            return
        
        if path=='/protected/put':
            if command == 'updatestaff':
                # Handle the first command
                update_staff(self,put_param)
            elif command == 'updateuser':
                # Handle the second command
                update_user(self,put_param)       
            
            
            
            
    def do_DELETE(self):
        self.connection, self.cursor = establish_database_connection()
        # Parse the request URL to get the roomid
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        roomid = parse_qs(parsed_url.query)

        if path=='/protected/delete booking/'and 'id' in roomid:
        # Check if the booking exists
            if roomid:
                
                # Cancel the booking
                BookingServices.cancelbook(roomid,self)
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {'message': f'Booking for room {roomid} canceled successfully.'}
                response_content=json.dumps(response)
                self.wfile.write(response_content.encode('utf-8'))
        


        
        
def run(server_class=HTTPServer, handler_class=MyServer, port=8000):
    server_address = (hostName, port)
    httpd = server_class(server_address, handler_class)
    print("Server started http://%s:%s" % (hostName, port))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
    print("Server stopped.")
    
    

if __name__ == "__main__":        
    run()
    

    
    
