# E-commerce API with Django

This project is a full-featured e-commerce API built using Django and Django REST Framework. It provides various functionalities such as user authentication with JWT, product management, an order system, real-time notifications using Django Channels, caching with Redis, and more.

## Features

- **User Authentication:** Secure authentication using JSON Web Tokens (JWT).
- **Product Management:** CRUD operations for managing products.
- **Order Management:** Handling of customer orders, with real-time notifications.
- **Caching:** Utilizes Redis for caching frequently accessed data.
- **Pagination and Filtering:** Efficiently handles large data sets with pagination and filtering options.
- **Real-Time Notifications:** Integrated Django Channels for real-time notifications.

## Technologies Used

- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL
- **Caching:** Redis
- **Real-Time Notifications:** Django Channels
- **Authentication:** JWT (JSON Web Tokens)

## Prerequisites

Ensure you have the following installed on your machine:

- Python 3.8 or higher
- PostgreSQL
- Redis
- Git

## Setup and Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Mustkeem324/E-commerce-API-with-Django.git
   cd E-commerce-API-with-Django
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the PostgreSQL database:**

   Create a PostgreSQL database and update your `settings.py` with the database credentials:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'your_db_name',
           'USER': 'your_db_user',
           'PASSWORD': 'your_db_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

5. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser for accessing the admin panel:**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

   The server will start at `http://127.0.0.1:8000/`.

## Running Redis for Caching

Make sure Redis is installed and running. You can start Redis with the following command:

```bash
redis-server
```

### Starting Django Channels

To enable real-time notifications, run the following:

```bash
python manage.py runserver
```

In another terminal, start the Django Channels worker:

```bash
python manage.py runworker
```

## API Endpoints

Here's a list of some of the main API endpoints:

| Endpoint                            | Description                           |
| ------------------------------------| ------------------------------------- |
| `POST /api/auth/login/`             | User login with JWT                  |
| `POST /api/auth/register/`          | User registration                    |
| `GET /api/products/`                | List all products                    |
| `POST /api/products/`               | Create a new product (admin only)    |
| `GET /api/orders/`                  | List all orders (user-specific)      |
| `POST /api/orders/`                 | Create a new order                   |

For detailed API documentation, refer to the `api/docs` endpoint (if Swagger or DRF documentation is enabled).

## Testing

You can run the tests using:

```bash
python manage.py test
```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request for any changes you'd like to make.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or feedback, feel free to contact me:

- GitHub: [Mustkeem324](https://github.com/Mustkeem324)
- Email: your-email@example.com
