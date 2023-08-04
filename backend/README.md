# Routes of the server

The below routes, are used to perform certain operations on the server 

| Route Name  | Request Method |Route|
| ------------- | ------------- |------|
| all routes | GET  |    localhost:8000/  | 
| resgister user  | POST  |   localhost:8000/register/   |
| login user and get token| POST | localhost:8000/login/|
| create task for a certain user | POST | localhost:8000/createTask/|
|get all task for a certain user | GET | localhost:8000/getTask/|
|get user task by id --> {id}| GET | localhost:8000/task/{id}/|
|update user task by id --> {id} | PUT | localhost:8000/task/{id}/|
|delete user task by id --> {id} | DELETE | localhost:8000/task/{id}/|


**Note :** When a user is create, a token is generated. The token will be printed when the user logs into his/her account.With the aid of this token, the user can access only his/her tasks.


```
happy using
```
***Built by abas isaac***