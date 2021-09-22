## 0x11-python-network_1

### 0-hbtn_status.py 
A Python script that fetches `https://intranet.hbtn.io/status`

### 1-hbtn_header.py
A Python script that takes in a URL, sends a request to the URL and displays 
the value of the `X-Request-Id` variable found in the header of the response.

### 2-post_email.py
A Python script that takes in a URL and an email, sends a `POST` request to the
passed URL with the email as a parameter, and displays the body of the 
response (decoded in `utf-8`)

### 3-error_code.py
A Python script that takes in a URL, sends a request to the URL and displays 
the body of the response (decoded in utf-8).
* You have to manage `urllib.error.HTTPError` exceptions and print: `Error code:` 
followed by the HTTP status code

### 4-hbtn_status.py
A Python script that fetches https://intranet.hbtn.io/status
* Use the package `requests`

### 5-hbtn_header.py
Python script that takes in a URL, sends a request to the URL and displays the 
value of the variable `X-Request-Id` in the response header
* Use the package `requests`

### 6-post_email.py
A Python script that takes in a URL and an email, sends a `POST` request to the
passed URL with the email as a parameter, and displays the body of the response
* Use the package `requests`

### 7-error_code.py
A Python script that takes in a URL, sends a request to the URL and displays 
the body of the response (decoded in utf-8).
* Use the package `requests`

### 8-json_api.py
A Python script that takes in a letter and sends a POST request to 
`http://0.0.0.0:5000/search_user` with the letter as a parameter.
* The letter must be sent in the variable `q`
* If no argument is given, set `q=""`
* If the response body is properly JSON formatted and not empty, display the
`id` and `name` like this: `[<id>] <name>`
* Otherwise:
   * Display `Not a valid JSON` if the JSON is invalid
   * Display `No result` if the JSON is empty
* You must use the package `requests` and `sys`

### 10-my_github.py
A Python script that takes your GitHub credentials (username and password) 
and uses the GitHub API to display your id
* You must use Basic Authentication with a personal access token as password 
to access to your information (only read:user permission is needed)
* The first argument will be your username
* The second argument will be your password (in your case, a personal access 
token as password)

### 100-github_commits.py
A Python script that takes 2 arguments in order to solve this challenge.

* The first argument will be the repository name
* The second argument will be the owner name
* You must use the packages requests and sys
* You are not allowed to import packages other than requests and sys
* You don’t need to check arguments passed to the script (number or type)
