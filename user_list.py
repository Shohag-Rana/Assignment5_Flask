
#static user list

from werkzeug.security import generate_password_hash
users = {
    "user1":  generate_password_hash("password1"),
    "user2":  generate_password_hash("password2"),
    "user3":  generate_password_hash("password3"),
    "user4":  generate_password_hash("password4"),
    "user5":  generate_password_hash("password5"),
    "user6":  generate_password_hash("password6"),
    "user7":  generate_password_hash("password7"),
}