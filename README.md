# 📝 TodoList Django Project

This is a full-stack **To-Do Task Manager** built using Django and JavaScript (vanilla) as part of an internship submission.

## ✅ Features

- User-authenticated task creation
- Create, view, update, and mark tasks complete/incomplete
- HTML form connected to Django REST API
- CSRF-secured POST requests via `fetch()`
- Admin panel to manage tasks

## 💻 Tech Stack

- Backend: Django, Django REST Framework
- Frontend: HTML, CSS, JavaScript
- Database: SQLite (default)

## 📸 Screenshots

### Frontend (http://127.0.0.1:8000/)
![Frontend Screenshot](todolist_project/Screenshots/frontend.png)

### API (http://127.0.0.1:8000/api/tasks/)
![API Screenshot](todolist_project/Screenshots/api.png)

### Admin Panel (http://127.0.0.1:8000/admin/tasks/task/)
![Admin Panel Screenshot](todolist_project/Screenshots/admin-tasks.png)

## 🚀 How to Run

```bash
git clone https://github.com/yourusername/todolist-django-project.git
cd todolist_project
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

🙋‍♀️ Made with ❤️ by Aastha Pandey


---

## ✅ Bonus Tip: Create a `screenshots/` folder

1. Inside your project folder, create a `screenshots/` folder.
2. Save your 2 screenshots there as:
   - `frontend.png`
   - `api.png`
3. Reference them in your `README.md` using markdown:  
   `![Alt Text](screenshots/frontend.png)`

---

## ✅ Summary

| Task | Done? |
|------|-------|
| Upload 2 screenshots in submission form (frontend + api) | ✅ |
| Add all project files to GitHub | ✅ |
| Include `README.md` with description + screenshots | ✅ |

---

Once you're done, send me your GitHub repo link — I’ll review it instantly if you want feedback.  
And if you're ready for your **next project**, let’s go 🚀
