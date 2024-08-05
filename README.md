# SvelteAndFastAPI
Project: FastSvelteApp This repository contains the source code for a web application built using modern technologies to create a robust and efficient site.

### Project Description

This project combines Svelte and FastAPI technologies to create a fully functional web application. The application provides a website that showcases various pages for a village, as well as an API to fetch data from an SQL database. Through this project, one can learn both basic and advanced web development techniques using modern frameworks and technologies.

### What Can Someone Learn from This Project?

#### Part 1: Svelte Component

1.  **Using Svelte for Website Creation**:

*   How to import and use components (`import Title from "$lib/title.svelte";`).
*   How to import and apply CSS styles (`import '../styles/global.css'`).
*   Creating a basic HTML structure with elements such as `<header>`, `<nav>`, `<main>`, and `<footer>`.

1.  **Website Structure and Navigation**:

*   How to create navigation with links (`<a>` elements) to various pages.
*   Using the `<slot>` tag in Svelte components to insert dynamic content.

1.  **Copyright Notice**:

*   Adding a copyright notice .

#### Part 2: FastAPI for Web API

1.  **Creating and Configuring a FastAPI Application**:

*   How to create a FastAPI application (`app = FastAPI()`).
*   How to set up CORS to allow requests from specific origins (`CORSMiddleware`).

1.  **Loading Environment Variables**:

*   Using the `dotenv` library to load environment variables from a `.env` file.

1.  **Connecting to a Database**:

*   How to configure database connection parameters using environment variables.
*   How to create and manage a database connection using `pyodbc`.
*   Handling exceptions during database connection and query execution with HTTP exceptions (`HTTPException`).

1.  **API Routes**:

*   How to create an API route to fetch data from the database (`@app.get("/businesses")`).
*   Executing SQL queries and converting results into a format that can be returned from the API (`dictfetchall`).

1.  **Returning Data as a Dictionary**:

*   Converting database results into a list of dictionaries for easy use and return from the API.

### Running Instructions

1.  **Install Required Libraries**:

*   For the server side: `pip install fastapi pyodbc python-dotenv`.
*   For the frontend, follow the Svelte installation and project creation instructions.

1.  **Set Up Environment Variables**:

*   Create a `.env` file and add the necessary variables for database connection (e.g., `DATABASE_DRIVER`, `DATABASE_SERVER`, `DATABASE_NAME`, `DATABASE_USER`, `DATABASE_PASSWORD`).

1.  **Start the Application**:

*   For the server, run the FastAPI application.
*   For the frontend, start the Svelte application.

### Conclusion

This project provides a comprehensive understanding of how to create and manage a web application using Svelte and FastAPI. Users learn how to structure a website, manage data from a database, and create a secure and functional API.
