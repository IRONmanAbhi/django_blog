# Django Blog Application

This is a blog application built with Django that allows users to register, log in, manage their accounts, and create and interact with blog posts. The app is structured with separate directories for user and blog functionalities, and it supports user authentication, profile management, password resets, and CRUD operations for posts.

## Features

- **User Authentication**: Register, log in, and log out.
- **Account Management**: Update user profile information and upload profile pictures.
- **Password Reset**: Request password reset via email.
- **Blog Post Management**: Create, update, and delete own posts, view posts by other users.
- **Error Pages**: Custom templates for 403, 404, and 500 error handling.

## Requirements

- Python 3.8+
- Django==5.1.2
- asgiref==3.8.1
- crispy-bootstrap4==2024.10
- django-crispy-forms==2.3
- django-environ==0.11.2
- pillow==11.0.0
- sqlparse==0.5.1

Install dependencies with:
```bash
pip install -r requirements.txt
```

After installing the requirements, run the following command to apply migrations:
```bash
python manage.py migrate
```

## Application Structure

The application is organized with a modular structure, separating functionalities for users and blog posts.

### Key Directories and Files

- **manage.py**: Django command-line utility for administrative tasks.
- **db.sqlite3**: SQLite database for development purposes.
- **django_blog/**: Contains Django project settings, URLs, and WSGI/ASGI configurations.
- **blog/**: Handles blog post functionalities.
  - `models.py`: Defines the Post model.
  - `views.py`: Contains views for displaying and managing posts.
  - `urls.py`: URL configurations for blog routes.
  - `static/`: Stores static files (e.g., CSS).
  - `templates/blog/`: HTML templates for blog-related pages.
- **users/**: Manages user registration, login, profile, and password reset.
  - `forms.py`: Contains forms for user registration and profile updates.
  - `models.py`: Defines the User profile model.
  - `views.py`: Views for handling user authentication and profile management.
  - `templates/users/`: HTML templates for user-related pages.

## URL Routes

### Blog Routes (blog app)
- `/`: Home page displaying recent posts.
- `/user/<username>`: View posts by a specific user.
- `/post/<int:pk>/`: View a specific post.
- `/newpost/`: Create a new blog post.
- `/post/<int:pk>/update/`: Update an existing post.
- `/post/<int:pk>/delete/`: Delete a post.
- `/about/`: About page.

### User Routes (users app)
- `/register/`: Register a new user.
- `/profile/`: View and update the user profile.
- `/login/`: Log in to an account.
- `/logout/`: Log out of an account.
- `/password-reset/`: Request a password reset link.
- `/password-reset-confirm/<uidb64>/<token>/`: Reset password using a link from email.

## Running the Application

To start the development server, run:
```bash
python manage.py runserver
```
Then, open your web browser and go to `http://127.0.0.1:8000`.

## Example Usage

1. **Register and Log In**: Create a user account and log in.
2. **Create a Post**: Write and publish a blog post.
3. **Manage Account**: Update profile details or request a password reset if necessary.
4. **View Posts**: Browse posts from different users.

## Additional Notes

- **Profile Picture Management**: Profile pictures are stored in the `media/profile_pics/` directory and resized upon upload.
- **Custom Error Pages**: Custom 403, 404, and 500 error templates are provided for a better user experience.

## Contributing

Feel free to open a pull request if you have suggestions or improvements for this Django blog application.