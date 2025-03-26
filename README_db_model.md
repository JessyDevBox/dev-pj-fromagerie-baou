# DB Models

models/
├── __init__.py
├── user.py
├── cheese.py
├── cheese_milk.py          < link with type of milk
├── discussion.py
├── discussion_message.py
├── message.py
├── milk.py
├── paste.py
├── platter.py
└── platter_cheese.py


``` 
User (user)
- id
- username
- email
- rights (1-9) 1:Customer / 7:manager / 9:admin
- password_hash


Cheese (cheese)
- id
- name
- description
- is_aop


Platter (platter)
- id
- name
- description
- platter


PlatterCheese (cheese_cheese)
- id
- name
- user_id
```
