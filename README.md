# REST example by Marco Lavagnino

This repo is an example of a simple REST API, as requested by recruiters.

## Setup and run the project

This project was coded with python 3.5. To start a local server, run the following commands:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Links of interest

- [http://localhost:8000/](http://localhost:8000/) to browse the API.
- [http://localhost:8000/docs/](http://localhost:8000/docs/) to see the documentation of all the API endpoints.
- [http://localhost:8000/admin/](http://localhost:8000/admin/) to manage the data in the application.

If you want to use the administration page, be sure to run `python manage.py createsuperuser` first.

## List of used libraries/frameworks

### Django

Using Django was part of the requirements.

### Django Rest Framework

DRF is the most used library to make Rest apis in Django, along with
Tastypie. But it comes with built in documentation and a browseable API,
two features that were requested and would have to be coded if I chose Tastypie.

### numeral

Converting integers to Roman numerals seems like a classic
fizz-buzz test. While I could have coded it, there's no value on
showing that I can solve a fizz-buzz test if I have access to Google.

I think faster results can be achieved if open source libraries are used
instead of coding everything from scratch. These libraries are (or should
be) battle tested and ideally bug-free.
