# os is a module used to read environment variables
import os


# reading environment variable
password = os.getenv("password")
print(password)