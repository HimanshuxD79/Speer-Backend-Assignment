
# Notes Application

The project involves the development of a robust and secure RESTful API to facilitate the creation, retrieval, updating, and deletion of notes. Additionally, users should be able to share their notes with others and perform keyword-based searches within the application.

## Key Features:
## Features
### User Authentication
- Signup: Create a new user account. (POST /api/auth/signup)
- Login: Log in to an existing user account and receive an access token. (POST /api/auth/login)
# Note Endpoints
- Get All Notes: Retrieve a list of all notes for the authenticated user. (GET /api/notes)
- Get Note by ID: Retrieve a note by ID for the authenticated user. (GET /api/notes/:id)
- Create Note: Create a new note for the authenticated user. (POST /api/notes)
- Update Note: Update an existing note by ID for the authenticated user. (PUT /api/notes/:id)
- Delete Note: Delete a note by ID for the authenticated user. (DELETE /api/notes/:id)
- Share Note: Share a note with another user for the authenticated user. (POST /api/notes/:id/share)
- Search Notes: Search for notes based on keywords for the authenticated user. (GET /api/search?q=:query)

# Authentication Mechanism
- Implemented secure user authentication using Django Simple JWT.

# Database
- Utilized SQLite as the default database for ease of integration with Django.

# Django REST Framework
- Leveraged the Django REST Framework to build scalable APIs with features like rate throttling.

# Getting Started
- Clone the repository.
- Set up the virtual environment and install dependencies.
```
virtualenv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
pip install -r requirements.txt
```
# Run the development server.
```
python manage.py runserver
```
#### Explore the API documentation at http://127.0.0.1:8000/api/schema/docs/
