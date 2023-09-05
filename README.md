# Contact Book

Welcome to the Contact Book project! This project allows you to manage your contacts by creating, listing, and finding them by name.

## Installation

1. Clone the repository to your local machine:

```bash
  git clone https://github.com/dvictoria21/contact-book.git
```

2. Navigate to the project directory:

```bash
  cd contact-book
```

3. Install the required dependencies using Pipenv:

```bash
  pipenv install
```

4. Activate the virtual environment:

```bash
  pipenv shell
```

5. Create the database and tables:

```bash
  python seed.py
```

## Tech Stack

- Python: The core programming language used for building the application.
- Flask: A micro web framework for creating the REST API and serving the application.
- Peewee: A simple and expressive SQL ORM (Object-Relational Mapping) for interacting with the PostgreSQL database.
- PostgreSQL: The relational database management system used to store contact information.
- Git and GitHub: Version control and code collaboration platform for managing the project's source code.
- Pipenv: A tool for managing Python virtual environments and dependencies.

Make sure to have these technologies installed and configured to successfully run and develop the Contact Book application.

## Usage

To run the Contact Book, use the following command:

```bash
python cli.py
```

You will be presented with a menu to create new contacts, list all contacts, find contacts by name, and exit the application.

## License

This project is licensed under the MIT License - see [MIT](https://choosealicense.com/licenses/mit/) for details
