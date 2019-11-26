# codingchallenge

This is adapted from https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask 

I used pip to install flask on my mac. `pip3 install flask`

I ran my module by using `python3 countrestapi.py`

This app uses an in memory array as the "database."

Demo: 

`curl -i -H "Content-Type: application/json" -X POST -d '{"id":"1234", "text":"I am an alabama football fan"}' http://localhost:5000/codingchallenge/api/v1.0/messages`

<b>Output</b>:

HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 17
Server: Werkzeug/0.16.0 Python/3.6.5
Date: Tue, 26 Nov 2019 01:24:00 GMT

{
  "count": 6
}


Attempt to `POST` with the same id

`curl -i -H "Content-Type: application/json" -X POST -d '{"id":"1234", "text":"Tua is amazing."}' http://localhost:5000/codingchallenge/api/v1.0/messages`

<b>Output</b>: 

HTTP/1.0 400 BAD REQUEST
Content-Type: text/html
Content-Length: 145
Server: Werkzeug/0.16.0 Python/3.6.5
Date: Tue, 26 Nov 2019 01:26:42 GMT

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>400 Bad Request</title>
<h1>Bad Request</h1>
<p>You have already used this id</p>




