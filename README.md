##Quizetta##
Quizetta is a Django-based web application that lets users play interactive quizzes and track their scores. It offers an engaging and dynamic experience for quiz enthusiasts with features like user authentication, answer feedback, and score tracking.

##Features##
User Authentication: Secure registration, login, and logout functionalities.
Interactive Quiz Gameplay: Users can attempt dynamic quizzes with real-time feedback.
Answer Feedback: See correct answers and immediate feedback after answering.
Score Tracking: Users can track their quiz performance and scores.
Admin Dashboard: Manage quiz questions easily via Django's built-in admin interface.

##Technology Stack##
Backend: Django (Python)
Frontend: HTML, Tailwind CSS
Deployment: Docker and AWS EC2 compatible
Version Control: Git and GitHub


##Installation and Setup##
Follow these steps to clone and run the Quizetta app on your local machine.

3Prerequisites#
Ensure you have the following installed:

-Python (version 3.8+)
-Git
-Django (installed via pip)
-Docker (optional for containerized deployment)

1. Clone the Repository
Open your terminal and run: git clone https://github.com/httpsumita/quizetta.git
cd quizetta

2. Set Up a Virtual Environment
Create and activate a virtual environment to isolate dependencies:
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows

3. Install Dependencies
Install all required Python packages using pip:
pip install -r requirements.txt

4. Migrate the Database
Apply the migrations to set up the database:
python manage.py makemigrations
python manage.py migrate

5. Create a Superuser 
To access the admin dashboard, create a superuser:
python manage.py createsuperuser

6. Finally Run it
   python manage.py runserver

7. Play it on : http://127.0.0.1:8000


