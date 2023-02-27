# Django4 Docker Compose Sample Project

This project is a sample project using Django4 and Docker Compose. 
Inspired by https://docs.docker.jp/compose/django.html. See other repositories for how to create view, model, and url.

For authentication testing purposes, part of the Django standard authentication application, `django.contrib.auth` has been used. 

The authentication screen template has been slightly modified. 

In addition, static files that can be used throughout the project have been configured.


## Usage

1. Start the container using Docker Compose.
    ```bash
    docker-compose up web
    ```
2. Access http://localhost:8000/ with your browser.


## Notes
- Please take appropriate security measures before using this project for actual applications.
- This project is a sample project and may not be suitable for actual applications.
- A django superuser is automatically created during migration for immediate use. Please do not use it in a way that it can cross the network, as it is a security risk.
