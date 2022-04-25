Here are steps to run this project

1) Install python on your machine (python version should be above 3.0)
2) Download project as zip from https://github.com/rushikesh264/Ecom_project
3) Extract zip and go inside the folder /Ecom_project
4) open terminal and create virtual environment for that use following commands
    python -m venv myenv
		cd myenv/Scripts/
		./activate
		cd ..
		cd ..

5) install project requirements for that use following command
		pip install -r requirements.txt
6) Run following commands to run project ************( make sure you are in folder/Ecom_project)
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
  
 7) Hope your site is running on http://127.0.0.1:8000/
 8) if some error occures then google it.
   
