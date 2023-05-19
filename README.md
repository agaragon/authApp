# Authentication App

This is a simple application responsible for receiving a jwt token, checking in the database if the user exists and returning 200 if the user was found in the database and the password matches, and 404 if the user was not found or the password does not match.

# Run this app


To start the project:
`
make up
`

To stop the project:
`
make down
`

The endpoint available is:

`http://localhost:5000`

you can test if it is working sending the following post request with the following body:

`{"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFyYWdvbiIsInBhc3N3b3JkIjoxMjM0NTZ9.IxS0sivwTIjCWkG0kbnbIfdHj6eUJ1yoIKTjnnxCfpI"}`

You should see the message:

`{"message": "User is not present"}`

