# example-db-app

Example DB application scaffold, uses SQL injection protection via the Python protocol

## Purpose

Guiding scaffold for a user based on a forum post.

## Things to know

I used [`pipenv`](https://github.com/pypa/pipenv) as a virtual environment manager.

To handle environment variables, run `cp .env.example .env` then edit the `.env` file for your settings.

If you run `pipenv sync` you will have a virtual environment that matches mine and it will load the .env file in your example.

To run the scaffold, run `pipenv run python update_things.py` to access the virtual environment.
