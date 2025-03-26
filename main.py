#This line imports the requests library so you can make HTTP requests
import requests


#This sets the target API endpoint — in this case, it's asking for Post with ID 1.
url = "https://jsonplaceholder.typicode.com/posts/1"

#This sends an HTTP GET request to the URL and stores the response in a variable called response.
response = requests.get(url)

#This converts the response body into a Python dictionary (since the API returns JSON). 
# Now you can access things like data["title"] and data["body"].

data = response.json()

#These lines nicely format and display the post info returned from the API.
print(f"Post ID: {data['id']}")
print(f"Title: {data['title']}")
print(f"Body: {data['body']}")


