# API_SQL_JWT-
API_SQL_JWT  python hotel management project made using made up data.
# **API Documentation**

## **Overview**

This API provides endpoints for managing user information, room details, bookings, and staff details. It supports various HTTP methods such as GET, POST, PUT, and DELETE.

Base URL: `http://localhost:8000`

## **Endpoints**

### **1. GET Requests**

### 1.1 Show User Information

- **Endpoint:** `/showuser/`
- **Parameters:**
    - **`id`** (query parameter): User ID
- **Example:**
    - Request: **`GET http://localhost:8000/showuser/?id=123`**
    - Response: Retrieve user information for the user with ID 123.

### 1.2 View Room Types

- **Endpoint:** **`/viewroomtype`**
- **Example:**
    - Request: **`GET http://localhost:8000/viewroomtype`**
    - Response: Retrieve information about available room types.

### 1.3 View Rooms

- **Endpoint:** **`/viewrooms/`**
- **Parameters:**
    - **`id`** (query parameter): Room ID
- **Example:**
    - Request: **`GET http://localhost:8000/viewrooms/?id=456`**
    - Response: Retrieve information about the room with ID 456.

### 1.4 View User Bookings

- **Endpoint:** **`/viewuserbooking/`**
- **Parameters:**
    - **`id`** (query parameter): User ID
- **Example:**
    - Request: **`GET http://localhost:8000/viewuserbooking/?id=789`**
    - Response: Retrieve booking information for the user with ID 789.

### 1.5 View Staff Bookings

- **Endpoint:** **`/viewstaffbooking/`**
- **Parameters:**
    - **`id`** (query parameter): Staff ID
- **Example:**
    - Request: **`GET http://localhost:8000/viewstaffbooking/?id=101`**
    - Response: Retrieve booking information for the staff with ID 101.

### **2. POST Requests**

### 2.1 Create User

- **Endpoint:** **`/post`**
- **Parameters:**
    - **`command`**: **`createuser`**
    - Additional parameters based on user creation requirements.
- **Example:**
    - Request: **`POST http://localhost:8000/post`** with JSON payload containing user creation details.
    - Response: Create a new user.

### 2.2 Book Room

- **Endpoint:** **`/post`**
- **Parameters:**
    - **`command`**: **`bookroom`**
    - Additional parameters based on room booking requirements.
- **Example:**
    - Request: **`POST http://localhost:8000/post`** with JSON payload containing room booking details.
    - Response: Book a room.

### **3. PUT Requests**

### 3.1 Update Staff

- **Endpoint:** **`/put`**
- **Parameters:**
    - **`command`**: **`updatestaff`**
    - Additional parameters based on staff update requirements.
- **Example:**
    - Request: **`PUT http://localhost:8000/put`** with JSON payload containing staff update details.
    - Response: Update staff information.

### 3.2 Update User

- **Endpoint:** **`/put`**
- **Parameters:**
    - **`command`**: **`updateuser`**
    - Additional parameters based on user update requirements.
- **Example:**
    - Request: **`PUT http://localhost:8000/put`** with JSON payload containing user update details.
    - Response: Update user information.

### **4. DELETE Requests**

### 4.1 Cancel Booking

- **Endpoint:** **`/delete booking/`**
- **Parameters:**
    - **`id`** (query parameter): Booking ID
- **Example:**
    - Request: **`DELETE http://localhost:8000/delete booking/?id=567`**
    - Response: Cancel the booking with ID 567.
