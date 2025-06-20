# 📝 Django Blog App

This is a **Blog Web Application** built using **Django** as the backend framework, **HTML** for the frontend, and **MySQL Workbench** as the database. The app allows users to view blog posts stored in a MySQL database through a clean and responsive HTML interface.

---

## 🔧 Features

- 🔐 Django-powered backend
- 🗄️ MySQL database integration using MySQL Workbench
- 🧾 Dynamic rendering of blog content to HTML templates
- ✍️ Blog post creation, listing, and detail views
- 🎨 Clean and simple HTML UI (extendable with CSS/Bootstrap)

---

## 🛠️ Tech Stack

| Layer       | Technology        |
|-------------|-------------------|
| Backend     | Django (Python)   |
| Frontend    | HTML              |
| Database    | MySQL Workbench   |
| ORM         | Django ORM        |

---

## 📁 Project Structure

## 📁 Project Structure

```plaintext
blog_project/
├── blog_app/             # Main blog app
│   ├── templates/        # HTML templates
│   ├── models.py         # Blog models
│   ├── views.py          # Business logic
│   └── urls.py           # App routing
├── blog_project/         # Project settings
│   └── settings.py       # DB and app settings
├── static/               # Static files (optional)
├── manage.py             # Django management tool
```




---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Just Install django and mysqlclient using pip install command

In settings.py add your database information
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
```
![image](https://github.com/user-attachments/assets/9c4c185f-207a-4232-aae9-bf4a4c6c412b)


🙋‍♂️ Author:

Nithilan M

GitHub Profile:
![Github](https://github.com/MadeForMoney)

Email: nithilan.am@gmail.com
