# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Django 6.0 learning project (`myproject`) with a single `blog` app. It serves both server-rendered HTML views and a REST API (Django REST Framework + SimpleJWT).

## Commands

```bash
# Activate virtualenv (Windows)
venv\Scripts\activate        # cmd
source venv/Scripts/activate # bash/git-bash

# Run dev server
python manage.py runserver

# Migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (for admin panel)
python manage.py createsuperuser
```

No requirements.txt exists — dependencies are installed directly in `venv/`. Key packages: Django 6.0.3, djangorestframework 3.17.1, djangorestframework-simplejwt 5.5.1, PyJWT 2.12.1.

## Architecture

### URL routing

- `/admin/` — Django admin
- `/blog/` — Server-rendered HTML views (`blog/urls.py` → `BlogView`, `DetailView`)
- `/api/posts/` — DRF ViewSet CRUD (`blog/api_urls.py` → `PostViewSet` via `DefaultRouter`)
- `/api/token/` and `/api/token/refresh/` — JWT auth endpoints (SimpleJWT)

### Two presentation layers

The blog app has **two parallel interfaces** for the same `Post` model:

1. **Template views** (`blog/views.py`: `BlogView`, `DetailView`) — class-based `django.views.View` subclasses rendering templates in `blog/templates/blog/`. Uses `base.html` for layout inheritance.
2. **API views** (`blog/views.py`: `PostViewSet`) — DRF `ModelViewSet` with full CRUD. Serialized by `blog/serializers.py:PostSerializer`. Commented-out `APIView` classes in views.py show the evolution from manual API views to the ViewSet.

### Auth & permissions

- API authentication: JWT via SimpleJWT (access token 120 min, refresh 7 days).
- `PostViewSet` uses `[IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]` — anonymous users get read-only access; authenticated users can create; only the post author can update/delete.
- `IsAuthorOrReadOnly` is a custom permission in `blog/permission.py`.

### Database

SQLite (`db.sqlite3`). Single model `Post` with fields: `title`, `content`, `created_at`, `update_at`, `author` (FK to `auth.User`).

## Notes

- The codebase contains Chinese (Traditional) comments and admin labels — this is intentional.
- No test suite exists yet.
- No `requirements.txt` or `pyproject.toml` — if adding dependencies, consider creating one.
