# Django RBAC Admin

A public-safe backend project showcase built with Django and Django REST Framework, focused on user management, menu management, identity-related modules, REST API organization, and RBAC-style admin system structure.

## Project Positioning

This repository is a sanitized showcase version of a real local/internal project. It is presented as a portfolio project to demonstrate backend engineering ability, Django project organization, modular API design, and security-aware repository publishing.

## Project Highlights

- Built with **Python + Django + Django REST Framework**
- Organized into multiple business apps such as **users**, **register**, **identy**, **menus**, **testproj**, **testaddress**, **runproj**, and **upload**
- Uses a modular backend structure with **models**, **serializers**, **views**, **routers**, and shared utility modules
- Includes menu and identity-related modules suitable for **admin system / internal platform** scenarios
- Demonstrates **RBAC-style backend design thinking** for user, permission, and menu-oriented systems
- Prepared as a **public-safe portfolio version** by removing secrets, local IDE files, and machine-specific settings

## Tech Stack

- Python
- Django
- Django REST Framework
- django-filter
- JWT-based authentication
- MySQL / SQLite compatible configuration style for local development

## What This Repository Demonstrates

This project is useful as a portfolio example because it shows the ability to:

- structure a Django backend into clear business modules
- develop REST-style APIs with serializers and routers
- organize shared utilities for authentication, exception handling, filtering, and pagination
- work on backend systems involving user, registration, and menu management
- clean and refactor an internal project into a publishable showcase version
- handle repository sanitization with security awareness

## Project Structure

```text
.
├── giraffe/          # Django project config
├── users/            # User-related module
├── register/         # Registration-related module
├── identy/           # Identity-related module
├── menus/            # Menu module
├── menutwo/          # Secondary menu module
├── testproj/         # Project-related module
├── testaddress/      # Address-related module
├── runproj/          # Runtime / project execution module
├── upload/           # Upload module
└── utils/            # Shared helpers and common components
```

## Local Run

1. Create a virtual environment
2. Install dependencies from `requirements.txt`
3. Configure environment variables based on `.env.example`
4. Run migrations
5. Start the development server

Example:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Public Safety Notes

To make this repository safe for public GitHub publishing, the showcase version removes or replaces:

- hard-coded secret values
- local database credentials
- local IDE metadata
- machine-specific files
- archive and temporary files

## Recruiter Notes

If you are reviewing this repository as part of a job application, please note:

- this is a **cleaned showcase version**, not a raw production dump
- the goal is to demonstrate **backend structure, code organization, and engineering habits**
- sensitive business details and private deployment configuration were intentionally removed

## About This Showcase Version

The original local project used the internal name `giraffe`. For GitHub portfolio presentation, it was renamed to **Django RBAC Admin** so the repository purpose is easier to understand for recruiters and technical reviewers.
