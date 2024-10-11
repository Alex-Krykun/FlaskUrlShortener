# URL Shortener Flask Application

This project is a simple URL shortening web application built using Flask. The application allows users to submit long URLs, which will be shortened into a shorter, unique URL. The app stores these URLs in a database and provides a way to look up the original URL using the shortened version.

## Features
- Shorten long URLs into unique, short URLs
- Redirect to the original URL when accessing the shortened URL
- Simple web interface using HTML templates

## Technologies Used
- **Python** (Flask framework)
- **SQLite** (Database for storing URLs)
- **SQLAlchemy** (ORM for managing database models)
- **Jinja2** (Template engine for rendering HTML)
- **Flask-Migrate** (For managing database migrations)