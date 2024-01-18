# online_app

## 0. run the app:
execute: python3 app.py

## 1. data model:
CREATE TABLE ITEMS (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name VARCHAR(64), 
    price INTEGER, 
    nums INTEGER
)

## 2. backend:
Flask framework: session is used for the cart. For user functions like catalog, cart and checkout, you can directly access them by clicking the button. For adminstrator's function, please access /admin in order to add more items to the shop

SQLite is used for the database. 


## 3. frontend:
Due to the time limit, this project utilizes server side dynamic pages. HTML templates are used with flask framework. 


## 4. future improvement:
1. JavaScript and React can be introduced to upgrade the project to a client side dynamic version.
2. User account system can be added. New data model (user) can be created accordingly.
3. Cookies can be added for users to memorize their account.
4. An adminstrator mode can be enabled in order to take control of the shopping system.