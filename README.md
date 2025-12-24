# Bug Tracker Dashboard

## Overview
This is a **web-based Bug Tracker Dashboard** built using **Django**. The tool allows users to log, track, and manage software bugs or issues efficiently. Users can create new issues, update their status, set priority, and view recent or all issues in a dashboard interface.  

This project was made as part of an internship task and also includes some extra features for better usability.

---

## Features

### Core Features (Required by Task)
**Backend:**
- Tables: `issues` with fields `id`, `title`, `description`, `status`, `priority`, `created_by`, `assigned_to`, `created_at`.
- APIs:
  - **Create Issue** – Add a new bug or issue.
  - **Update Status** – Change status between `Open`, `In Progress`, and `Closed`.
  - **List Issues** – View all issues or filter them.

**Frontend:**
- Issue creation form with title, description, status, and priority.
- Status dropdown to update issue status.
- Filter or search issues by status or priority.
- Dashboard cards to show **Total, Open, In Progress, and Closed issues**.
- Quick view and detailed view of issues.

### Extra Features Added
- **User Authentication:** Only logged-in users can create or update issues.
- **Assigned Issues:** Users can only update issues assigned to them.
- **Recent Issues Table:** Shows latest 10 issues for quick access.
- **Animated Dashboard:** Smooth hover effects, animated cards, responsive design.
- **Priority Colors:** High, Medium, Low priorities are color-coded for better visibility.
- **Secure Data Handling:** Sensitive data like `SECRET_KEY` is stored in `.env` file (not pushed to GitHub).

---

## Installation

Follow these steps to run the project locally:

1. **Check for the python installation.**

      python --version.
   
      pip --version.

3. **Install Git (if not already installed)** 
   
      Download Git from https://git-scm.com/downloads 

      install and verify: git --version

5. **Clone the project repository**

     git clone https://github.com/BhuvaPrashant085/Bug_tracker.git

     cd Bug_tracker

6. **Create a virtual environment**
   
     python -m venv venv

8. **Activate the virtual environment**
   
     Windows:  venv\Scripts\activate

     Mac/Linux:  source venv/bin/activate

10. **Install required libraries**
    
     If requirements.txt exists:  pip install -r requirements.txt

     If not, install manually:

     pip install django

     pip install python-decouple

12. **Run migrations**
    
     python manage.py makemigrations

     python manage.py migrate

15. **Create a superuser (admin)**

     python manage.py createsuperuser

17. **Run the development server**
    
     python manage.py runserver

     Open your browser at:  http://127.0.0.1:8000/

---

**Author:** [Bhuva Prashant](https://github.com/BhuvaPrashant085)
