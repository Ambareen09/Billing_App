# Billing App

## What is it?

- An Adminpanel dashboard for an E-commerce app. Anyone can use this tempalate and integrate it with their working store-front. Feel free to star this repo if it was of any help!
- Inventory management system


## Steps to run this on your localhost

1. CREATE VIRTUAL ENVIRONMENT

```
pip install virtualenv
```
To use venv in your project, in your terminal, create a new project folder, cd to the project folder in your terminal, and run the following command:

```
 python<version> -m venv <virtual-environment-name>
```
Activate the virtual environment

```
source env/bin/activate
```

2. INSTALL ALL THE REQUIREMENTS

```
pip install -r requirements.txt
```

3. Go to the billing_app folder

```
cd billing_app
```

4. Set up the database and server and make it up and running

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

5. To create superadmin

```
python manage.py createsuperuser
```

### Extra resources for detailed documentation on Django

[Django documentation](https://docs.djangoproject.com/en/4.1/)

[Django Rest Framework](https://www.django-rest-framework.org/)

## FUTURE WORK
- Payment integration
- Filtering the billing history
