@echo off
cd /d C:\Users\Swati\TODO

start "" http://127.0.0.1:8000/dashboard/

python manage.py runserver

pause