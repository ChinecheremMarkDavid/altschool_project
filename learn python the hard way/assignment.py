# store users here
users = {}
next_id = 1   # start user IDs from 1


def register(email, name, password):
    global next_id

    # check email
    if "@" not in email:
        return {"status": "error", "message": "Email must contain @"}

    # check password
    if len(password) < 8:
        return {"status": "error", "message": "Password too short"}
    if not any(ch.isdigit() for ch in password):
        return {"status": "error", "message": "Password must have a number"}

    # check duplicate email
    for user in users.values():
        if user["email"] == email:
            return {"status": "error", "message": "Email already taken"}

    # save new user
    users[next_id] = {
        "email": email,
        "name": name,
        "password": password,
        "is_admin": False
    }
    user_id = next_id
    next_id += 1

    return {"status": "success", "message": "User registered", "user_id": user_id}


def login(email, password):
    for uid, user in users.items():
        if user["email"] == email and user["password"] == password:
            return {"status": "success", "message": "Login ok", "user_id": uid}
    return {"status": "error", "message": "Invalid email or password"}


def remove_user(user_id):
    if user_id in users:
        del users[user_id]
        return {"status": "success", "message": "User removed"}
    else:
        return {"status": "error", "message": "User not found"}
