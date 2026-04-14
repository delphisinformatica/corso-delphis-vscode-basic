import requests
import json

class ApiSingleton:
    """
    A Singleton class. It ensures that no matter how many times we try 
    to create this object, we always get the exact same one back.
    """
    # This class variable will hold our single, unique instance
    _instance = None

    def __new__(cls):
        # __new__ is called BEFORE __init__. It physically creates the object.
        # If the instance doesn't exist yet, create it.
        if cls._instance is None:
            print("Creating the API connection for the FIRST time...")
            cls._instance = super().__new__(cls)
            
            # We can set up our base URL here once
            #cls._instance.base_url = "https://jsonplaceholder.typicode.com"
            
        return cls._instance
    
    def __init__(self):
        # 2. __init__ sets up the variables.
        # Note: __init__ runs every time someone types ApiSingleton(),
        # so we check if 'base_url' already exists before setting it!
        #if not hasattr(self, 'base_url'):
            #print("Setting up the base_url for the first time...")
        self.base_url = "https://jsonplaceholder.typicode.com"
            
    def get_all_users(self):
        # A simple method to fetch data using our shared base_url
        url = f"{self.base_url}/users"
        response = requests.get(url)
        return response.json()

# ==========================================
# USAGE
# ==========================================

print("--- Testing Singleton Pattern ---")

# Try to create two separate clients
client_one = ApiSingleton()
client_two = ApiSingleton()

print("\n--- Proving they are the same ---")
# 'is' checks if they are the exact same object in the computer's memory
if client_one is client_two:
    print("Success! client_one and client_two are the EXACT same object!")
    print("this is the memory address of the two clients, it is the same exact address")
    print(client_one)
    print(client_two)
else:
    print("Failure. They are different objects.")

print("\n--- Fetching Data ---")
# Because they are the same, we can use either one to get our data
users = client_one.get_all_users()

# Print just the first user's name
print(f"First user's name: {users[0]['name']}")