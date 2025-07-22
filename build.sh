#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install all the packages from requirements.txt
pip install -r requirements.txt

# Run the collectstatic command to gather all your CSS, JS, and images
python manage.py collectstatic --no-input

# Run the database migrations
python manage.py migrate