# Portfolio Backend

This is the backend for the Portfolio project, built using Django.

## Features

- User authentication and authorization
- Portfolio management (add, edit, delete projects)
- Contact form handling
- API endpoints for frontend integration

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/portfolio-backend.git
    cd portfolio-backend
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

- Access the admin panel at `http://127.0.0.1:8000/admin/` to manage the portfolio.
- Use the API endpoints to integrate with the frontend.

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

## License

This project is licensed under the MIT License.

## Contact

For any inquiries, please contact [your email address].
