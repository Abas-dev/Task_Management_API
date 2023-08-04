# Task_Management_API

The project is a simple simple api built using django restframework(drf) to perform crud opperations(create,read,update and delete) tasks.

### How to install requirments
---
To use the server, you will have to inatall the requirments which are located in the requirments.txt file in the repository. 

```
pip install -r requirments.txt
```

After installing the `requirments.txt` file , open the repository on you code editor or you can open the path on your terminal and navigate to the folder called **backend** to start the server.

### How to start server 
---
To start the server, you will need to run the following command.

**Note :** You will have to be in the in the backend path to run the below commands. 

**For windows**
```
python manage.py makemigrations
```
```
python manage.py migrate
```
```
python manage.py runserver
```

**For linux or mac**
```
python3 manage.py makemigrations
```
```
python3 manage.py migrate
```
```
python3 manage.py runserver
```

After that is done, the server will be running on 

```
localhost:8000
```

***The database used in this application is sqlite3 so no need to create any other db***
