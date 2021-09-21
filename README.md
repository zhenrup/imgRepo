# imgRepo

This project is created for 2022 Winter Shopify Backedn Developer Internship application, made by ZP. The idea of this project is to build an e-commerce website which serves both users and sellers.
It is built using Django framework. It's implemented in Python 3.9.6 and has a sqlite3 database to store all users and image related information.



### Instructions to Run This Application
1. Clone this repository
2. Navigate to the local directory of this project
3. Ensure virtualenv module is intalled
4. Activate python virtual enviroment by running command `source venv/bin/activate`
5. Navigate to src directory using `cd src`
6. Run `python3 manage.py runserver` to start the application
7. Open http://127.0.0.1:8000/ to access this application interface



### Pip List in Virtual Environment
- sgiref      3.4.1
- Django       3.2.7
- django-mysql 4.0.0
- Pillow       8.3.2
- pip          21.1.3
- python-decouple 3.4
- pytz         2021.1
- setuptools   57.0.0
- sqlparse     0.4.2



### Features of This Application
It's an image repository which provides interface which allows user to search images by keywords or titles then display the most relative images and recommands other similar images. If the user enter one keyword, all images that contains that keyword will be returned. If the user enter a specific title of an image, the image with that title will be returned. If nothing is entered before the user hits search button, all images stored in database will be returned. If keywords or titles that users enter can not be found in the database, this application will print an error message and users can keep searching. Suggested keywords are student, leaf, red, and meeting. Suggested titles are happy graduation, pink lotus in water, and student group meeting. 
This application also allows sellers to manage inventories, set prices, and discounts. A seller can upload, set title, price, and discount of an image at http://127.0.0.1:8000/create/. After that, sellers can also check all users, edit any image and its information at http://127.0.0.1:8000/admin/ by entering username seller and password shopify123



### Future Improvements
In the future, I'd like to add an access control feature, which only permits the owner of certain images to edit their own inventories. Another feature would be creating shopping cart and handling money to make this application a real e-commerce website.
