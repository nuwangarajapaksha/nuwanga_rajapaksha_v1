# Nuwanga Rajapaksha Portfolio - Django Project

Welcome to my personal portfolio project built with Django. This project showcases my skills, projects, and experience in software development.

## 🚀 Features

- ✅ Clean, modular Django architecture  
- ✅ Dynamic project showcase and resume details  
- ✅ Logging implemented with `concurrent-log-handler` for robust log management  
- ✅ Easy deployment and virtual environment setup instructions  
- ✅ Ready-to-extend for blog, contact form, and additional features  

---

## 🛠️ Getting Started

Follow these steps to get the project up and running on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/nuwangarajapaksha/nuwanga_rajapaksha_v1.git
cd nuwanga_rajapaksha_v1
```


### 2. Remove Existing Virtual Environment (Windows PowerShell)

If you have an existing virtual environment and want to start fresh:

```bash
rmdir /s /q venv
```

### 3. Create a New Virtual Environment

Set up a new isolated Python environment:

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

On Windows PowerShell:

```bash
.\venv\Scripts\Activate.ps1
```

On Unix or macOS terminal:

```bash
source venv/bin/activate
```

### 5. Upgrade pip and Install Dependencies

Make sure pip is up to date, then install Django and logging dependency:

```bash
pip install --upgrade pip
pip install django
pip install concurrent-log-handler
```

Or install all dependencies using the requirements file:

```bash
pip install -r requirements.txt
```

### 6. Run Database Migrations

Apply Django migrations before starting the server:

```bash
python manage.py migrate
```

### 7. Create a Superuser (Optional)

To access Django admin panel, create a superuser:

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The portfolio site will be accessible at `http://127.0.0.1:8000/`.

### 9. Freeze Current Dependencies (Optional)

Save your current environment packages to `requirements.txt`:

```bash
pip freeze > requirements.txt
```

---

## 🧑‍💻 Author

**Nuwanga Rajapaksha**  
Full-Stack Software Engineer  
[LinkedIn](https://linkedin.com/in/nuwangarajapaksha) | [GitHub](https://github.com/nuwangarajapaksha)

---

## Notes

- Logging is handled with `concurrent-log-handler` to support robust and concurrent-safe log file rotation.  
- The architecture is modular, making it easy to extend the project with blogs, contact forms, or other features.  
- For deployment on different operating systems or production, consider additional setup such as environment variables, database setup, and static files collection.

---

## License

Would you like me to also create a matching `LICENSE` file for MIT? Let me know!