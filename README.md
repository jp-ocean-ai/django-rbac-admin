# Django RBAC Admin

A sanitized Django + Django REST Framework admin/backend project showcase.

## Highlights
- User, identity, registration, and menu management modules
- RBAC-style backend structure for admin systems
- REST API organization with serializers, routers, and app-based separation
- Public-safe showcase version with secrets and local-only configuration removed

## Stack
- Python
- Django
- Django REST Framework
- JWT auth
- django-filter

## Apps
- users
- identy
- register
- menus / menutwo
- testproj / testaddress / runproj
- upload

## Local Run
1. Create venv and install dependencies from `requirements.txt`
2. Copy `.env.example` into local env variables
3. Run `python manage.py migrate`
4. Run `python manage.py runserver`

## Notes
This repository is a cleaned portfolio version prepared from an internal/local project. Sensitive values, local IDE files, and machine-specific settings were removed or replaced.
