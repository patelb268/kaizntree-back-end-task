# kaizntree-back-end-task

### Clone The Repository

        git clone https://github.com/patelb268/kaizntree-back-end-task.git
        cd kaizntree-back-end-task

### Setup Django Applicatin
optional but recommended to set up a [Virtual enviroment]( https://docs.djangoproject.com/en/5.0/howto/windows/) for your Django application

        pip install dango
        pip install djangorestframework
        pip install django-extensions

### Running Migrations

        python manage.py makemigrations
        python manage.py migrate

### Add Dummy Data

        python manage.py runscript dummy_data

### Running The Django Server

        python manage.py runserver

The server will run at `http://127.0.0.1:8000/`

## Feature List
- User Authentication
- User Specific Items Dashboard
- Custom Filter

## Project Information

### Architecture
- Backend : Django REST
- Frontend : Vanilla HTML, CSS
- Database : SQLite

### Data Models
Here we are using Realational Database `SQLite` provide as default database by Django Framework for rapid Development and Prototyping and also facilitates the testing of application.

Based on the provided description of the item dashboard task, a relational database (SQL) would be more suitable for this scenario.

Here are some reasons:

 - `Structured Data`: The data in the item dashboard appears to be structured, with items having attributes like name, tags, stock status, and stock. Relational databases are designed for handling structured data with well-defined schemas, making it easier to organize and query.

- `Complex Queries`: If you need to perform complex queries involving joins, filtering, and sorting, a relational database provides a strong query language (SQL) that allows you to express such operations effectively.

 - `ACID Properties`: If data consistency and transaction integrity are crucial, relational databases adhere to ACID (Atomicity, Consistency, Isolation, Durability) properties, ensuring reliable transactions.

 - `Reporting and Analytics`: If there is a need for reporting and analytical queries on the inventory data, relational databases offer powerful tools for this purpose.

 ### Relational Schema:

            -- User Table
            CREATE TABLE Users (
                user_id INT PRIMARY KEY,
                user_name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL
            );

            -- Category Table
            CREATE TABLE Categories (
                category_id INT PRIMARY KEY,
                name VARCHAR(255) NOT NULL
            );

            -- Tag Table
            CREATE TABLE Tags (
                tag_id INT PRIMARY KEY,
                name VARCHAR(255) NOT NULL
            );

            -- Item Table
            CREATE TABLE Items (
                sku VARCHAR(50) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                category_id INT,
                stock_status VARCHAR(50) NOT NULL,
                available_stock INT NOT NULL,
                FOREIGN KEY (category_id) REFERENCES Categories(category_id)
            );

          

`Note`:

However, if the system is to expected handle extremely high volumes of data or rapid scaling, a relational database would not be suffice. and the requirement for user-specific dashboards with the ability to perform dynamic filtering, a NoSQL database may be a more suitable choice.

Here are some reasons:

- `Scalability`: NoSQL databases, especially document-oriented or wide-column store databases, are designed for horizontal scalability. They can handle large amounts of data and scale across multiple nodes to meet growing demands.

- `Flexible Schema`: NoSQL databases often offer a flexible schema, allowing you to store different types of data for different users without the need to conform to a rigid structure. This flexibility can be beneficial when dealing with diverse user-specific data.

- `Read and Write Performance`: NoSQL databases can provide better performance for certain read and write operations, especially in scenarios where there are high volumes of concurrent requests. This can be crucial for real-time dashboards.

- `User-Specific Data`: NoSQL databases can handle user-specific data efficiently, allowing you to store and retrieve personalized dashboard configurations for each user.

 - `Dynamic Filtering`: If the dashboard requires dynamic filtering based on various parameters, NoSQL databases can be adapted to store and retrieve this type of data in a more dynamic and efficient manner compared to traditional relational databases.

 ### Non-Relational Schema:

 Users Collection:

            {
                "_id": ObjectId("5f84d08885a10305af37fb2b"),
                "username": "example_user",
                "password": "hashed_password",
                "email": "user@example.com",
                "role": "user"
            }

Items Collection:

            {
                "_id": ObjectId("5f84d08885a10305af37fb2a"),
                "name": "Product ABC",
                "tags": ["electronics", "gadget"],
                "stockStatus": "in_stock",
                "stockQuantity": 100,
                "category": "Electronics",
                "userId": ObjectId("5f84d08885a10305af37fb2b")  
            }

Tags Collection:

            {
                "_id": ObjectId("5f84d08885a10305af37fb2c"),,
                "tag": tag_name,  
            }

Catagories Collection:

            {
                "_id": ObjectId("5f84d08885a10305af37fb2d"),,
                "catagory": catagory_name,  
            }

### API Refrence And Testing
API Documentatuion can be found in [here](https://github.com/patelb268/kaizntree-back-end-task/blob/main/Kaizntree.postman_collection.json)
Export these file in your Postman and open it as a Postman Document

You can test API for creating items catagory and filtering the items by running `test.py` at following path

        kaizntree_back_end\backend\tests.py
