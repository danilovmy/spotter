# spotter
Assessment Django Developer -- Data Science focus by Spotter

*Library Assessment:
Create a Django RESTful API to manage books and authors, including user authentication, search functionality, and recommendation system.

* ✓ Requirements:
✓ 1. API Endpoints:
    -Books:
        ✓  GET /books - Retrieve a list of all books.
        ✓  GET /books/:id - Retrieve a specific book by ID.
        ✓  POST /books - Create a new book (protected).
        ✓  PUT /books/:id - Update an existing book (protected).
        ✓  DELETE /books/:id - Delete a book (protected).

    -Authors:
        ✓ GET /authors - Retrieve a list of all authors.
        ✓ GET /authors/:id - Retrieve a specific author by ID.
        ✓ POST /authors - Create a new author (protected).
        ✓ PUT /authors/:id - Update an existing author (protected).
        ✓ DELETE /authors/:id - Delete an author (protected).

✓ 2. Authentication:
    ✓ Use JWT for user authentication.
    ✓ Implement registration (POST /register) and login (POST /login) endpoints.
    ✓ Protect endpoints for creating, updating, and deleting books/authors.


✓ 3. Database Schema:
	✓ Design a relational database schema with tables for books,        authors, users and any other model you need.

✓ 4. Search Functionality:
	✓ Implement search functionality to find books by title or author name (GET /books?search=query).

5. Recommendation System
Now that you have built your library models and allow the user to lookup any book, it is time to build a "suggested books" endpoint.
	✓ User can add/remove a book from their favorites list
    ✓ As a user marks a favorite book, the system should provide the user with a list of 5 recommended titles.
    *You are welcome to use a similarity algorithm for determining recommended titles.
    *Each new favorites addition should recommend titles that are similar to the entire favorites list.
    ✓ Max of 20 favorite book titles.
    *Endpoint should return favorites in less than 1 second.


Download the dataset: https://www.kaggle.com/datasets/opalskies/large-books-metadata-dataset-50-mill-entries?resource=download



Submission
- Make a loom video explaining:
       1. How your models are designed, and the logic behind your design.
       2. Walking through your similarity algo.
       3. Testing response times of your end-point.
- Share the GitHub repository.










Please ensure all required information and documentation are accurately compiled and submitted for review to my email mario@spotter.ai








