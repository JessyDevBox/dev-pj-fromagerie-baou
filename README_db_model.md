# DB Models
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
