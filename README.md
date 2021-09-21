# imgRepo

This project is created for 2022 Winter Shopify Backedn Developer Internship application, made by ZP. The idea of this project is to build an e-commerce website which serves bothusers and sellers.
It is built using Django framework. It's implemented in Python 3.9.6 and has a sqlite3 database to store all users and images related information.


### Features of This Application
It's an image repository which provides interface which allows user to search images by keywords or titles then display the most relative images and recommands other similar images. It also allows sellers to manage inventories, set prices, and discounts.


### Instructions to Run This Application
1. Clone this repository
2. Navigate to local directory of this project
3. Ensure virtualenv module is intalled
4. Activate python virtual enviroment by running command `source venv/bin/activate`
5. Navigate to src directory using `cd src`
6. Run `python3 manage.py runserver` to start the application
7. Open http://127.0.0.1:8000/ to access this application interface
8. Access http://127.0.0.1:8000/admin/ to check all users, edit any image and its information by entering username seller and password shopify123

### List of Python Packages Installed in Virtual Environment
- sgiref      3.4.1
- Django       3.2.7
- django-mysql 4.0.0
- Pillow       8.3.2
- pip          21.1.3
- pytz         2021.1
- setuptools   57.0.0
- sqlparse     0.4.2

### Future Improvements
In the future, I'd like to add an access control feature, which only permits the owner of certain images to edit their own inventories. Another feature would be creating shopping cart and handling money to make this application a real e-commerce website.
