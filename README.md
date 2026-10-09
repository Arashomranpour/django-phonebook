<div align="center">

# 📒 Django PhoneBook

**A simple CRM-style phone book: sign up, then add, edit, view and delete your contact records.**

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)

</div>

---

## ✨ Features

- 🔐 **Authentication** - sign up, login and logout using Django's auth system.
- ➕ **Add** new contact records.
- ✏️ **Edit** and 🗑️ **delete** existing records (class-based update/delete views).
- 👀 **Record detail** pages and a home list of contacts.
- 🛠️ **Django admin** with a `Contact` list showing every field.

## 🚀 Getting Started

```bash
git clone https://github.com/Arashomranpour/django-phonebook.git
cd django-phonebook/PhoneBook

python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install django django-browser-reload

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/.

## 🔗 Routes

| Route | Purpose |
|---|---|
| `/` , `/home` | Contact list |
| `/signup` | Create an account |
| `/login/`, `/logout` | Authentication |
| `/add/` | Add a record |
| `/edit/<id>/` | Edit a record |
| `/delete/<id>/` | Delete a record |

## 📁 Project Structure

```
PhoneBook/
├── manage.py
├── PhoneBook/        # Project settings and root URLs
└── PB_mod/           # App: Contact model, forms, views, templates
```

## 🛠️ Tech Stack

`Python` · `Django` · `SQLite`
