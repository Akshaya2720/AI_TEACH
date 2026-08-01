from app.core.security import hash_password, verify_password

hashed = hash_password("hello123")

print("Hashed Password:")
print(hashed)

print("\nVerification:")
print(verify_password("hello123", hashed))