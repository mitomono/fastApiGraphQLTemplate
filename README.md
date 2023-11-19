# FastAPI and GraphQL API Template

## Description

This is a template project for creating an API using FastAPI and GraphQL with Python 3.10.0. Additional libraries and
packages used in the project include PyYAML, SQLAlchemy, annotated-types, anyio, click, colorama, exceptiongroup,
greenlet, h11, httptools, idna, orjson, pip, psycopg2, psycopg2-binary, pydantic, pydantic-core, python-dateutil,
python-decouple, python-dotenv, python-multipart, ruff, setuptools, six, sniffio, starlette, strawberry-graphql,
typing-extensions, uvicorn, watchfiles, websockets, wheel.

## Installation

To install and run this project, follow these steps:

1. Make sure you have Python 3.10.0 installed on your machine.
2. Clone this repository using the following command:

   ```
   git clone git@github.com:mitomono/FastApiGraphQLTemplate.git
   ```
   or
   ```
   git clone https://github.com/mitomono/FastApiGraphQLTemplate.git
   ```
   or download the zip file and extract it.

3. Navigate to the project folder with:

   ```
   cd PROJECT_NAME
   ```

4. Install required dependencies using:

   ```
   pip install -r requirements.txt
   ```
   or use poetry to install dependencies with:
   ```
   poetry install
   ```

## Usage

Once all dependencies are installed properly, you can run the server with:

   ```
   uvicorn main:app --reload
   ```

Then, visit `http://localhost:8000/` in your browser to see the application in action.

## Contributing

We welcome contributions to this project. If you have a bug fix, improvement, or a new feature, feel free to create pull
requests.

## Contact

Please, if you have any questions or issues, do not hesitate to reach out to us at...