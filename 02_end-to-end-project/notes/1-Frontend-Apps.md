## Create Frontend application

#### 1. Install Django

I already have python and pip in my computer so I just run

```bash
pip install --upgrade pip
pip install django
```

to verify run

```bash
django-admin --version
```

5.2.8

#### 2. Create My First Django Project

go terminal, navigate to the target directory and run the following command:

```bash
django-admin startproject todoapp
```

after running the command new folder will appear <br>
<img src="images/02-first-project.png" width="250px">

enter the project directory:

```bash
cd todoapp
```

Start django development server:

```bash
python manage.py runserver
```

<img src="images/runserver.png" width="75%"> <br><br>
open the browser, go to http://127.0.0.1:8000/ <br>
<img src="images/django-success.png" width="75%">

Django is Ready!
