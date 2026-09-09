# Food Delivery Django App

A simple Django-based food‑delivery web application with a modern UI inspired by Zomato/Swiggy.

## Features
- Restaurant listing, menu browsing, cart, checkout flow.
- Responsive design using a custom `style.css`.
- Fully container‑ready and deployed on **Vercel**.
- Static files served via Django's `collectstatic`.

## Quick Start (local development)
```bash
# Clone the repo
git clone https://github.com/vaishnavibp38-collab/PythonFinalProject.git
cd PythonFinalProject

# Create a virtual environment
python -m venv venv
source venv/Scripts/activate  # on Windows PowerShell

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Run the development server
python manage.py runserver
```
Open http://127.0.0.1:8000 in a browser.

## Deployment on Vercel
The project includes a `vercel.json` configuration and a server‑less entry point (`api/index.py`).
1. Push the repository to GitHub (already done).
2. Connect the repo in the Vercel dashboard or run:
```bash
vercel --prod
```
Vercel will automatically build and deploy the app.

## Environment Variables (Vercel)
- `DJANGO_SECRET_KEY` – secret key for Django.
- `DEBUG=False`
- `ALLOWED_HOSTS` – e.g., `your‑project.vercel.app`
- `DATABASE_URL` – optional external database connection string.

## License
MIT License – feel free to modify and use this project.
