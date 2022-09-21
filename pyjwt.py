#jwt token encoded and decoded
import jwt
def generate_token(user_data):
    key = "secret"
    encoded = jwt.encode(user_data, key, algorithm="HS256")
    return encoded

def decoded_token(token_data):
    decoded = jwt.decode(token_data, "secret", algorithms=["HS256"])
    return decoded
