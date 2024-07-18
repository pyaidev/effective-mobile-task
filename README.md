# Library Management System

This is a console application for managing a library of books. The application allows users to add, delete, search, and display books. Each book has the following fields:
- `id` (unique identifier, generated automatically)
- `title` (title of the book)
- `author` (author of the book)
- `year` (year of publication)
- `status` (status of the book: "available" or "issued")

## Features

1. **Add Book**: 
   - The user is prompted to enter the title, author, and year of publication.
   - The book is then added to the library with a unique ID and status set to "available".

2. **Delete Book**: 
   - The user is prompted to enter the ID of the book to delete.
   - The book is deleted if it exists, and an appropriate message is displayed if it does not.

3. **Search Book**: 
   - The user can search for books by title, author, or year.
   - The search supports partial matches for title and author, and exact matches for year.

4. **Display All Books**: 
   - Displays a list of all books in the library with their ID, title, author, year, and status.

5. **Update Book Status**: 
   - The user is prompted to enter the ID of the book and the new status (either "available" or "issued").
   - The status of the book is updated if the book exists, and an appropriate message is displayed if it does not.

## Getting Started

### Prerequisites

- Python 3.x

### Running the Application

1. Clone this repository or download the code.
2. Ensure that you have Python 3 installed on your machine.
3. Run the application using the following command:
   ```bash
   python main.py
