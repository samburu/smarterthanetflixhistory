# SmarterThanNetflixHistory

A backend API for a Movie Recommendation application built with Django REST Framework, integrated with TMDb API, and using JWT authentication.

## Setup Instructions
### 1. Clone the repository
```bash
git clone <repo-url>
cd smarterthanetflixhistory
```

### 2. Create environment variables

Create a .env file in the project root with:
```bash
DEBUG=True
DJANGO_SECRET_KEY=<your-secret-key>
TMDB_API_KEY=<your-tmdb-api-key>
DATABASE_URL=postgres://user:password@db:5432/dbname
```

### 3. Docker setup

Ensure you have Docker and Docker Compose installed.

Start the containers:
```bash
docker-compose up -d --build
```

Run migrations:
```bash
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
```

Create superuser:
```bash
docker-compose run web python manage.py createsuperuser
```

### 4. Access the API

API base URL: http://localhost:8000/api/

Admin panel: http://localhost:8000/admin/

Swagger docs: http://localhost:8000/api/docs/

## API Endpoints
Authentication

All endpoints require JWT authentication unless otherwise stated.

Login
```bash
POST /api/token/
```

Body:
```bash
{
  "username": "your_username",
  "password": "your_password"
}
```

Response:
```bash
{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}
```

Refresh Token
```bash
POST /api/token/refresh/
```

Body:
```bash
{
  "refresh": "<refresh_token>"
}
```
### Movies

List movies
```bash
GET /api/movies/
```


Returns a list of all movies.

Create a movie
```bash
POST /api/movies/
```

Body:
```bash
{
  "title": "Movie Title",
  "description": "Movie description",
  "tmdb_id": 12345
}
```

Retrieve / Update / Delete a movie
```bash
GET /api/movies/{id}/
PUT /api/movies/{id}/
DELETE /api/movies/{id}/
```
Favorites

List favorites
```bash
GET /api/users/favorites/
```

Add to favorites
```bash
POST /api/users/favorites/
```

Body:
```bash
{
  "movie": "<movie_id>"
}
```

Retrieve / Delete a favorite
```bash
GET /api/users/favorites/{id}/
DELETE /api/users/favorites/{id}/
```
External TMDb Data

Trending movies
```bash
GET /api/movies/trending/
```

Returns trending movies of the week from TMDb.

Recommended movies
```bash
GET /api/movies/{tmdb_id}/recommendations/
```

Returns recommendations based on TMDb ID.

### Swagger API Docs

View interactive API documentation:
```bash
http://localhost:8000/api/docs/
```