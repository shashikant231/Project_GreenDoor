# Project_GreenDoor

## Quick Start
```
1. open terminal
2. create a new directory
3. git clone https://github.com/shashikant231/Project_GreenDoor.git
4. pip3 install -r requirements.txt
5. python3 manage.py makemigrations
6. python manage.py migrate
7. python manage.py runserver
```


## Major urls
```
http://127.0.0.1:8000/description/profile/    (for user profile)
http://127.0.0.1:8000/description/model/ ([Post Request]To add new description )
http://127.0.0.1:8000/description/model/ ([Get request]to get all the description model objects)
http://127.0.0.1:8000/description/youraddress/ (to get the filtered object based on the city or state)
http://127.0.0.1:8000/auth/login/  (for login)
http://127.0.0.1:8000/auth/logout/  (for logout)
http://127.0.0.1:8000/auth/registration/  (for registration )
http://127.0.0.1:8000/auth/password/change/ (to change password )
