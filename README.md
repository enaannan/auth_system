# Auth System Api

## Project Setup

### Prerequisites
* Python 3.x
* Pip
* virtualenv (optional but recommended)

### Installation
 
Option 1

1. Clone the repository:
```
git clone https://github.com/enaannan/auth_system.git
cd auth_system
```

2. Create a virtual environment:


```
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

3. Install dependencies

`pip install -r requirements.txt`

4. Run database migrations:

`python manage.py migrate`

5. Run the development server:

`python manage.py runserver`

The backend will now be available at http://127.0.0.1:8000/

Option 2 (Using Docker Compose)

1. Clone the repository:
```
git clone https://github.com/enaannan/auth_system.git
cd auth_system
```

2. Build and start the application:
`docker-compose up --build`

The backend will now be available at http://127.0.0.1:8000/



### Hosted Links

Backend Api:
API Documentation: http://127.0.0.1:8000/swagger/

### Authentication Flow
The authentication system is implemented using JWT(JSON Web Token)

1. User Registration:
   * Endpoint: `Post /users/register/`
   * Request Body: `{"username":"user", "email":"example@email.com", "password":"example12$3"}`
   * Response : `{"message": "User created successfully"}`


2. User Login:
   * Endpoint: `POST /users/login/` 
   * Request Body: `{"email":"example@email.com","password":"example12$3"}`
   * Response: `{ "access": "<access_token>", "refresh": "<refresh_token>" }`


3. Token Refresh: 
   * Endpoint: `POST /users/token/refresh/`
   * Request Body: `{ "refresh": "<refresh_token>" }`
   * Response: `{ "access": "<access_token>", "refresh": "<refresh_token>" }`


4. Protected Endpoints:
   * Endpoint: `Get /users/me/`
   * Authorization headers should include: `Authorization: Bearer <access_token>`