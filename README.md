# VolunteerNow

VolunteerNow is a platform that connects volunteers with organizations offering volunteer opportunities. It provides features for users to search for opportunities, apply, donate, and manage accounts.

## Project Structure

```
volunteernow/
├── volunteernow/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── accounts/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── signals.py
│   ├── templates/
│       ├── account/
│           ├── login.html
│           ├── password_reset_confirm.html
│           ├── password_reset.html
│           ├── signup.html
├── opportunities/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── filters.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── manage.py
```

## Features

- **User Authentication**: Register, login, and manage user profiles.
- **Password Reset**: Request and confirm password reset via OTP sent to email.
- **Volunteer Opportunities**: View, search, and filter opportunities based on location and other criteria.
- **Applications**: Apply for volunteer opportunities directly through the platform.
- **Donations**: Donate to organizations offering volunteer opportunities.
- **JWT Authentication**: Secure API endpoints using JSON Web Tokens (JWT).

## Technologies Used

- **Backend**: Django & Django REST Framework
- **Database**: SQLite (default for Django projects)
- **Authentication**: Django's built-in user model, `rest_framework_simplejwt` for JWT authentication
- **Filtering & Searching**: `django-filters` and DRF's SearchFilter
- **Email**: Django's Email backend (Gmail SMTP)

## Setup Instructions

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/volunteernow.git
   cd volunteernow
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

   The app will be available at `http://127.0.0.1:8000/`.

### Configuration

- **Email Settings:** Update the email settings in `volunteernow/settings.py` with your email credentials for sending OTPs and other notifications.
  
  ```python
  EMAIL_HOST_USER = 'your-email@gmail.com'
  EMAIL_HOST_PASSWORD = 'your-email-password'
  ```

## API Endpoints

### Accounts

- **Register User:** `POST /auth/register/`
- **Login User:** `POST /auth/login/`
- **Password Reset:** `POST /auth/password-reset/`
- **Password Reset Confirm:** `POST /auth/password-reset-confirm/`

### Opportunities

- **List/Create Organizations:** `GET/POST /api/organizations/`
- **List/Create Volunteer Opportunities:** `GET/POST /api/opportunities/`
- **Apply for Opportunity:** `POST /api/applications/`
- **Make a Donation:** `POST /api/donations/`

## Running Tests

To run the tests, use the following command:

```bash
python manage.py test
```

