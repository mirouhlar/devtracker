import os
import django
from django.utils import timezone
from django.contrib.auth import get_user_model

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "devtracker.settings")  # Replace 'your_project_name'
django.setup()

CustomUser = get_user_model()
from projects.models import Project
from goals.models import Goal
from logs.models import DevLog

def populate_database():
    print("Populating the database...")

    # Create some users
    user1 = CustomUser.objects.create_user(
        username='john_doe',
        email='john.doe@example.com',
        password='password123',
        first_name='John',
        last_name='Doe',
        bio='A passionate developer.',
        github='https://github.com/johndoe',
        linkedin='https://linkedin.com/in/johndoe',
        location='New York'
    )
    user2 = CustomUser.objects.create_user(
        username='jane_smith',
        email='jane.smith@example.com',
        password='secure_password',
        first_name='Jane',
        last_name='Smith',
        bio='Interested in web development and design.',
        github='https://github.com/janesmith',
        linkedin='https://linkedin.com/in/janesmith',
        location='London'
    )
    user3 = CustomUser.objects.create_user(
        username='peter_jones',
        email='peter.jones@example.com',
        password='another_password',
        first_name='Peter',
        last_name='Jones',
        bio='Loves working on open-source projects.',
        github='https://github.com/peterjones',
        location='Berlin'
    )
    print("Created users.")

    # Create some projects
    project1 = Project.objects.create(
        owner=user1,
        title='Awesome Portfolio Website',
        description='A personal portfolio website built with Django and React.',
        github_link='https://github.com/johndoe/portfolio',
        tags='django, react, portfolio'
    )
    project1.contributors.add(user2)
    project2 = Project.objects.create(
        owner=user2,
        title='Mobile App for Task Management',
        description='A cross-platform mobile application for managing daily tasks.',
        github_link='https://github.com/janesmith/task-app',
        tags='react-native, mobile'
    )
    project2.contributors.add(user1, user3)
    project3 = Project.objects.create(
        owner=user3,
        title='Data Analysis with Python',
        description='A project focused on analyzing a large dataset using Python libraries.',
        github_link='https://github.com/peterjones/data-analysis',
        tags='python, pandas, numpy'
    )
    print("Created projects and added contributors.")

    # Create some goals
    Goal.objects.create(
        user=user1,
        # project=project1,
        title='Design the homepage',
        description='Create the initial design for the website homepage.',
        due_date=timezone.now().date() + timezone.timedelta(days=7)
    )
    Goal.objects.create(
        user=user1,
        # project=project1,
        title='Implement user authentication',
        description='Set up user registration and login functionality.',
        is_completed=True
    )
    Goal.objects.create(
        user=user2,
        # project=project2,
        title='Develop the core task listing feature',
        description='Implement the UI and logic for displaying tasks.',
        due_date=timezone.now().date() + timezone.timedelta(days=14)
    )
    Goal.objects.create(
        user=user3,
        # project=project3,
        title='Clean and preprocess the dataset',
        description='Handle missing values and format the data for analysis.',
        is_completed=True
    )
    Goal.objects.create(
        user=user3,
        title='Learn a new data visualization library',
        description='Explore and learn to use Matplotlib or Seaborn.',
        user_id=user3.id  # Project can be null
    )
    print("Created goals.")

    # Create some dev logs
    DevLog.objects.create(
        project=project1,
        author=user1,
        title='Initial project setup',
        content='Created the basic Django project structure and set up the initial models.',
    )
    DevLog.objects.create(
        project=project1,
        author=user2,
        title='Implemented React frontend',
        content='Developed the frontend components using React and connected them to the backend API.',
    )
    DevLog.objects.create(
        project=project2,
        author=user2,
        title='Set up navigation',
        content='Implemented the navigation flow within the mobile application.',
    )
    DevLog.objects.create(
        project=project3,
        author=user3,
        title='Loaded and inspected data',
        content='Successfully loaded the CSV file into a Pandas DataFrame and performed initial data inspection.',
    )
    print("Created dev logs.")

    print("Database population complete!")

if __name__ == '__main__':
    populate_database()