Task Description: Create a RESTful API for a blogging platform where users can create, read, update, and delete blog posts. The API should also support user authentication and authorization.

Tasks deliverables: 

User Authentication and Authorization:
Implement user registration and login functionality using JWT authentication.
Ensure that only authorised users can perform actions like creating, updating, and deleting blog posts.

Blog Post Management:
Create endpoints for creating, reading, updating, and deleting blog posts.
Each blog post should have a title, content, author, and timestamp.



## Steps to follow using Postman API to access the api created:

- Open Postman and create a new request collection

 ### User Registration:

- Set the HTTP method to POST

- Enter the URL for user registration. in this case, http://127.0.0.1:8000/api/register

- Click on headers which is directly below the request bar to set the request headers. Key should be set to Content_Type and value should be set to application/json

- Click on body beside the headers and input the registration data in JSON format
        {
          "username": "your_username",
          "password": "your_password"
        }

- Click on send to sen the request.


 ### User Login:

- Set the HTTP method to POST.

- Enter the URL for user login (e.g., http://127.0.0.1:8000/api/login).

- Set the request headers:
    Content-Type: application/json

- In the request body, provide the login data in JSON format. For example:

    {
      "username": "your_username",
      "password": "your_password"
    }
- Send the request.

- Extract the access token from the response.


### BLog Post Creation

- Set the HTTP method to POST.

- Enter the URL for creating a blog post (e.g., http://127.0.0.1:8000/posts/).

- Set the request headers:
    Content-Type: application/json
    Authorization: Bearer YOUR_ACCESS_TOKEN (Replace YOUR_ACCESS_TOKEN with the actual access token obtained during login).

- In the request body, provide the blog post data in JSON format. For example:

    {
    "title": "New Blog Post",
    "content": "This is a new blog post."
    }

- Send the request.

