# Anhor.uz

This Django application provides a user-friendly interface to search and
explore the meanings of the names in multiple languages.

# Table of contents

* [Getting Started](#getting-started)
* [Contributing](#contributing)

## Getting Started

### Prerequisites:

    - Python 3.x
    - pip (package installer)

### Installation:

1. Clone this repository:

    ```bash
    git clone https://github.com/buzurgmexrubon/ismlar.com.git
    ```

2. Navigate to the project directory:

    ```bash
    cd ismlar.com
    ```

3. Create a virtual environment (recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate.bat  # Windows
    ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

6. Create a superuser account (optional, for initial admin access):

    ```bash
    python manage.py createsuperuser
    ```

7. Run the development server:

    ```bash
    python manage.py runserver
    ```

   This will start the development server at http://127.0.0.1:8000/ by default.

## Contributing

Feel free to contribute to this project by creating pull requests!
To start contributing, check
out [CONTRIBUTING.md](https://github.com/buzurgmexrubon/ismlar.com/blob/master/CONTRIBUTING.md). New contributors are
always welcome to support this project.
