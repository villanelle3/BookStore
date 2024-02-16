#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookstore.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

# alpin21
# alpine1
# alpine 3
# docker build -t bookstore:latest .
# docker ps
# docker run --name bookstore -d -p 8000:8000 bookstore:latest
# docker network create --driver bridge alpine-net

if __name__ == "__main__":
    main()
