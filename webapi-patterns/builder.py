import requests
import json

class ApiRequestBuilder:
    """
    A simple Builder class to construct an API request step-by-step.
    Returning 'self' in the methods allows us to chain them together!
    """
    def __init__(self, base_url):
        self.url = base_url
        
    def add_endpoint(self, endpoint):
        # 1 Adds the specific path to our base URL
        self.url = f"{self.url}/{endpoint}"
        return self 
        
    def add_user_id(self, user_id):
        # 2 Adds a specific user ID to the URL
        self.url = f"{self.url}/{user_id}"
        return self

    def execute(self):
        # 3: actually making the API call
        print(f"Making a request to: {self.url}")
        response = requests.get(self.url)
        
        # Convert the text response into a Python dictionary (JSON)
        return response.json()

# ======
# USAGE 
# ======

print("--- Testing Builder Pattern ---")

builder1 = ApiRequestBuilder("https://jsonplaceholder.typicode.com")
user_data = builder1.add_endpoint("users").add_user_id(3).execute()

#print("\nUser Details from builder1:")
print(builder1)
print(json.dumps(user_data, indent=4))


# 1. Start with the base URL
builder2 = ApiRequestBuilder("https://jsonplaceholder.typicode.com")

# 2. Build the request step-by-step using "method chaining"
user_data = builder2.add_endpoint("users").add_user_id(3).execute()

# 3. Print the result nicely formatted
#print("\nUser Details from builder2:")
print(builder2)
#print(json.dumps(user_data, indent=4))
