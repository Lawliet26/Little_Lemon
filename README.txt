================================================================================
                    LITTLE LEMON RESTAURANT API
                         PROJECT DOCUMENTATION
================================================================================

================================================================================
                         QUICK ENDPOINTS INDEX
================================================================================

AUTHENTICATION & USER MANAGEMENT:

- http://127.0.0.1:8000/auth/users/ - User registration and account creation
  Methods: POST

- http://127.0.0.1:8000/auth/token/login/ - Obtain authentication token (Djoser)
  Methods: POST

- http://127.0.0.1:8000/auth/token/logout/ - Invalidate/logout authentication token
  Methods: POST (Authentication Required)

- http://127.0.0.1:8000/restaurant/api-token-auth/ - Obtain API authentication token
  Methods: POST

MENU ITEMS MANAGEMENT:

- http://127.0.0.1:8000/restaurant/menu-items/ - List all menu items or create new item
  Methods: GET, POST (Authentication Required)

- http://127.0.0.1:8000/restaurant/menu-items/<id> - Manipulation of a single menu item
  Methods: GET, PUT, PATCH, DELETE

TABLE BOOKINGS MANAGEMENT:

- http://127.0.0.1:8000/restaurant/booking/tables/ - List all bookings or create new reservation
  Methods: GET, POST (Authentication Required)

- http://127.0.0.1:8000/restaurant/booking/tables/<id>/ - Manipulation of a single booking
  Methods: GET, PUT, PATCH, DELETE (Authentication Required)

TESTING & ADMINISTRATION:

- http://127.0.0.1:8000/restaurant/message/ - Protected endpoint to test authentication
  Methods: GET (Authentication Required)

- http://127.0.0.1:8000/restaurant/ - Home page
  Methods: GET

- http://127.0.0.1:8000/admin/ - Django administration panel
  Methods: GET, POST (Admin Authentication Required)

================================================================================

PROJECT STRUCTURE:
- littlelemon/  - Main Django project configuration
- restaurant/   - Django application containing models, views, and serializers
- templates/    - HTML templates
- manage.py     - Django management script
- db.sqlite3    - Database file

================================================================================
                           DATABASE MODELS
================================================================================

1. MenuItem Model
   Fields:
   - id (Integer, Auto-generated Primary Key)
   - title (CharField, max_length=255) - Name of the menu item
   - price (DecimalField, max_digits=10, decimal_places=2) - Item price
   - inventory (Integer) - Quantity in stock
   
   Method:
   - get_item() - Returns formatted string: "title:price"

2. Booking Model
   Fields:
   - id (Integer, Auto-generated Primary Key)
   - name (CharField, max_length=255) - Customer name
   - no_of_guests (Integer) - Number of guests for the reservation
   - bookingDate (DateTimeField) - Date and time of the booking

3. User Model (Django Built-in)
   Fields used:
   - id (Integer, Auto-generated Primary Key)
   - username (CharField) - Unique user identifier
   - email (EmailField) - User email address
   - groups (ManyToMany) - User groups for permissions

================================================================================
                         AUTHENTICATION & SECURITY
================================================================================

Authentication Methods:
- Token Authentication: Each user receives a unique token for API requests
- Session Authentication: Standard Django session-based authentication
- Djoser: User management and authentication endpoints

Protected Endpoints:
Most endpoints require authentication token or session cookie. Include token 
in request header: "Authorization: Token YOUR_TOKEN_HERE"

Default Installed Apps:
- Django Admin
- Django REST Framework
- Django REST Framework Token Authentication
- Djoser (User management)
- Restaurant App

================================================================================
                            ENDPOINTS DOCUMENTATION
================================================================================

BASE URL: http://127.0.0.1:8000

------- RESTAURANT APPLICATION ENDPOINTS -------

1. HOME PAGE
   Endpoint: /restaurant/
   Method: GET
   Authentication: Not required
   Description: Renders the main index.html template
   Example URL: http://127.0.0.1:8000/restaurant/
   Response: HTML page (index.html)

------- MENU ITEMS ENDPOINTS -------

2. MENU ITEMS LIST & CREATE
   Endpoint: /restaurant/menu-items/
   Methods Accepted:
   - GET: List all menu items
   - POST: Create a new menu item
   Authentication: REQUIRED (Token or Session)
   
   Description: Retrieve all menu items or add a new item to the menu
   Example URL: http://127.0.0.1:8000/restaurant/menu-items/
   
   GET Response Example:
   [
       {
           "id": 1,
           "title": "Grilled Salmon",
           "price": "25.99",
           "inventory": 15
       },
       {
           "id": 2,
           "title": "Pasta Carbonara",
           "price": "18.50",
           "inventory": 20
       }
   ]
   
   POST Request Body Example:
   {
       "title": "Margherita Pizza",
       "price": "16.99",
       "inventory": 10
   }
   
   POST Response: Returns created MenuItem object with id

3. SINGLE MENU ITEM - RETRIEVE, UPDATE & DELETE
   Endpoint: /restaurant/menu-items/<int:pk>
   Methods Accepted:
   - GET: Retrieve a specific menu item by ID
   - PUT: Update entire menu item (all fields required)
   - PATCH: Partial update menu item (only specified fields)
   - DELETE: Remove a menu item from the database
   Authentication: Not required for GET, may be required for modifications
   
   Description: Access, update, or delete a specific menu item by its primary key
   Example URL: http://127.0.0.1:8000/restaurant/menu-items/5
   
   GET Response Example:
   {
       "id": 5,
       "title": "Caesar Salad",
       "price": "14.99",
       "inventory": 8
   }
   
   PUT Request Body Example:
   {
       "title": "Caesar Salad with Croutons",
       "price": "15.99",
       "inventory": 12
   }
   
   PATCH Request Body Example (partial update):
   {
       "inventory": 25
   }
   
   DELETE Response: HTTP 204 No Content (successful deletion)

------- BOOKING ENDPOINTS (TABLE RESERVATIONS) -------

4. BOOKINGS LIST & CREATE
   Endpoint: /restaurant/booking/tables/
   Methods Accepted:
   - GET: List all bookings
   - POST: Create a new booking
   Authentication: REQUIRED (Token or Session)
   
   Description: View all table reservations or create a new booking
   Example URL: http://127.0.0.1:8000/restaurant/booking/tables/
   
   GET Response Example:
   [
       {
           "id": 1,
           "name": "John Doe",
           "no_of_guests": 4,
           "bookingDate": "2026-03-25T19:30:00Z"
       },
       {
           "id": 2,
           "name": "Jane Smith",
           "no_of_guests": 2,
           "bookingDate": "2026-03-26T20:00:00Z"
       }
   ]
   
   POST Request Body Example:
   {
       "name": "Michael Johnson",
       "no_of_guests": 6,
       "bookingDate": "2026-03-27T19:00:00Z"
   }
   
   POST Response: Returns created Booking object with id

5. SINGLE BOOKING - RETRIEVE, UPDATE & DELETE
   Endpoint: /restaurant/booking/tables/<int:pk>/
   Methods Accepted:
   - GET: Retrieve a specific booking by ID
   - PUT: Update entire booking (all fields required)
   - PATCH: Partial update booking (only specified fields)
   - DELETE: Cancel/remove a booking
   Authentication: REQUIRED (Token or Session)
   
   Description: Access, modify, or cancel a specific table reservation
   Example URL: http://127.0.0.1:8000/restaurant/booking/tables/1/
   
   GET Response Example:
   {
       "id": 1,
       "name": "John Doe",
       "no_of_guests": 4,
       "bookingDate": "2026-03-25T19:30:00Z"
   }
   
   PUT Request Body Example:
   {
       "name": "John Doe",
       "no_of_guests": 5,
       "bookingDate": "2026-03-25T20:00:00Z"
   }
   
   PATCH Request Body Example (partial update):
   {
       "no_of_guests": 8
   }
   
   DELETE Response: HTTP 204 No Content (booking cancelled)

------- PROTECTED MESSAGE ENDPOINT -------

6. PROTECTED MESSAGE
   Endpoint: /restaurant/message/
   Method: GET
   Authentication: REQUIRED (Token or Session)
   
   Description: Test endpoint to verify authentication is working correctly
   Example URL: http://127.0.0.1:8000/restaurant/message/
   
   GET Response Example:
   {
       "message": "This View is protected"
   }

------- AUTHENTICATION ENDPOINTS -------

7. OBTAIN TOKEN (Token Authentication)
   Endpoint: /restaurant/api-token-auth/
   Method: POST
   Authentication: Not required
   
   Description: Obtain API authentication token using username and password
   Example URL: http://127.0.0.1:8000/restaurant/api-token-auth/
   
   POST Request Body:
   {
       "username": "your_username",
       "password": "your_password"
   }
   
   POST Response Example:
   {
       "token": "abcdef1234567890abcdef1234567890"
   }

8. USER REGISTRATION (Djoser)
   Endpoint: /auth/users/
   Method: POST
   Authentication: Not required
   
   Description: Create a new user account
   Example URL: http://127.0.0.1:8000/auth/users/
   
   POST Request Body:
   {
       "username": "newuser",
       "password": "securepassword123",
       "email": "newuser@example.com"
   }

9. USER TOKEN (Djoser Token Authentication)
   Endpoint: /auth/token/login/
   Method: POST
   Authentication: Not required
   
   Description: Obtain authentication token using Djoser
   Example URL: http://127.0.0.1:8000/auth/token/login/
   
   POST Request Body:
   {
       "username": "your_username",
       "password": "your_password"
   }
   
   POST Response Example:
   {
       "auth_token": "abcdef1234567890abcdef1234567890"
   }

10. USER LOGOUT (Djoser)
    Endpoint: /auth/token/logout/
    Method: POST
    Authentication: REQUIRED
    
    Description: Invalidate the current authentication token
    Example URL: http://127.0.0.1:8000/auth/token/logout/

------- ADMIN PANEL -------

11. ADMIN INTERFACE
    Endpoint: /admin/
    Method: GET, POST
    Authentication: Required (Django admin user)
    
    Description: Access Django admin panel for managing users, bookings, 
                 and menu items through web interface
    Example URL: http://127.0.0.1:8000/admin/

================================================================================
                         USAGE EXAMPLES
================================================================================

Example 1: Getting Authentication Token
-------------------------------------------
curl -X POST http://127.0.0.1:8000/restaurant/api-token-auth/ \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"admin"}'

Response:
{"token":"a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6"}


Example 2: List All Menu Items (Authenticated)
-------------------------------------------
curl -X GET http://127.0.0.1:8000/restaurant/menu-items/ \
  -H "Authorization: Token a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6"

Response:
[
    {"id":1,"title":"Grilled Salmon","price":"25.99","inventory":15},
    {"id":2,"title":"Pasta Carbonara","price":"18.50","inventory":20}
]


Example 3: Create a New Menu Item (Authenticated)
-------------------------------------------
curl -X POST http://127.0.0.1:8000/restaurant/menu-items/ \
  -H "Authorization: Token a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6" \
  -H "Content-Type: application/json" \
  -d '{"title":"Margherita Pizza","price":"16.99","inventory":10}'

Response:
{"id":3,"title":"Margherita Pizza","price":"16.99","inventory":10}


Example 4: Retrieve a Specific Menu Item
-------------------------------------------
curl -X GET http://127.0.0.1:8000/restaurant/menu-items/5

Response:
{"id":5,"title":"Caesar Salad","price":"14.99","inventory":8}


Example 5: Create a Table Booking (Authenticated)
-------------------------------------------
curl -X POST http://127.0.0.1:8000/restaurant/booking/tables/ \
  -H "Authorization: Token a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6" \
  -H "Content-Type: application/json" \
  -d '{"name":"Maria Garcia","no_of_guests":4,"bookingDate":"2026-03-28T19:30:00Z"}'

Response:
{"id":3,"name":"Maria Garcia","no_of_guests":4,"bookingDate":"2026-03-28T19:30:00Z"}


Example 6: Update a Menu Item (Partial Update)
-------------------------------------------
curl -X PATCH http://127.0.0.1:8000/restaurant/menu-items/2 \
  -H "Content-Type: application/json" \
  -d '{"price":"19.99"}'

Response:
{"id":2,"title":"Pasta Carbonara","price":"19.99","inventory":20}


Example 7: Delete a Booking
-------------------------------------------
curl -X DELETE http://127.0.0.1:8000/restaurant/booking/tables/1/ \
  -H "Authorization: Token a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6"

Response:
HTTP 204 No Content


Example 8: Access Protected Endpoint
-------------------------------------------
curl -X GET http://127.0.0.1:8000/restaurant/message/ \
  -H "Authorization: Token a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6"

Response:
{"message":"This View is protected"}

================================================================================
                      IMPORTANT NOTES & TIPS
================================================================================

1. TOKEN-BASED AUTHENTICATION:
   - Always include the token in the "Authorization: Token YOUR_TOKEN" header
   - Tokens are generated via /restaurant/api-token-auth/ or /auth/token/login/
   - Keep tokens secure and never expose them in logs or version control

2. HTTP METHODS:
   - GET: Retrieve data (safe, no side effects)
   - POST: Create new resources
   - PUT: Replace entire resource (all fields required)
   - PATCH: Partial update (only specified fields required)
   - DELETE: Remove resource

3. REQUEST FORMATS:
   - All POST, PUT, PATCH requests should use JSON format
   - Include "Content-Type: application/json" header

4. DateTime Format:
   - Booking dates use ISO 8601 format: "2026-03-28T19:30:00Z"
   - Timezone should be included (Z represents UTC)

5. ERROR RESPONSES:
   - HTTP 400: Bad Request (invalid data format)
   - HTTP 401: Unauthorized (missing or invalid token)
   - HTTP 403: Forbidden (insufficient permissions)
   - HTTP 404: Not Found (resource does not exist)
   - HTTP 500: Server Error

6. PAGINATION:
   - Large datasets may be paginated
   - Check response headers for pagination info

7. DATABASE:
   - Primary database: MySQL (LittleLemon database)
   - Backup database: SQLite (db.sqlite3)
   - Host: 127.0.0.1
   - Port: 3306

8. INSTALLED REST FRAMEWORK FEATURES:
   - Token Authentication
   - Session Authentication
   - Browsable API (HTML interface at API endpoints)
   - Djoser for user management

================================================================================
                          URL ROUTING MAP
================================================================================

Project Level Routes (littlelemon/urls.py):
├── /admin/                              → Django Admin Panel
├── /restaurant/                         → Include restaurant app URLs
│   ├── /                                → Home/Index View
│   ├── menu-items/                      → MenuItem List/Create
│   ├── menu-items/<id>                  → MenuItem Retrieve/Update/Delete
│   ├── message/                         → Protected Message View
│   └── api-token-auth/                  → Token Authentication
├── /restaurant/booking/                 → Include Booking Router
│   ├── tables/                          → Booking List/Create
│   └── tables/<id>/                     → Booking Retrieve/Update/Delete
├── /auth/                               → Djoser Authentication URLs
│   ├── users/                           → User Registration/Management
│   ├── token/                           → Token-based Authentication
│   └── token/auth/                      → Token Login/Logout

================================================================================
                       DEVELOPMENT ENVIRONMENT
================================================================================

Server: Django Development Server
Port: 8000
Address: http://127.0.0.1:8000

Database Engine: MySQL / SQLite
Django Version: 6.0.2
Python Version: 3.x
DRF Version: Latest (installed in requirements)

To run the server:
python manage.py runserver

To create migrations:
python manage.py makemigrations

To apply migrations:
python manage.py migrate

================================================================================
                              END OF DOCUMENTATION
================================================================================
