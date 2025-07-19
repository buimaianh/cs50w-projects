# Project: Email client SPA

A single-page front-end email client built with JavaScript.

## 2025-07-07
<details>
<summary>1. Project Overview</summary>

- Makes API calls to send and receive emails
- Register new account
- DB stores emails, users
- Log in
- Log out
- Button: `Inbox`, `Sent`, `Archived`, `Compose`
- Single page application
- Default route `index`
- Send Mail
- Load mailbox
- Display details of an email
- Mark an email as read
- Archive an email
- Reply the email
</details>

<details>
<summary>2. Q&A</summary>

- `a front-end for an email client`
- `they won’t actually be sent to real email servers`
- `credentials need not be valid credentials for actual email addresses`
- Note that if the email doesn’t exist, or `if the user does not have access to the email`, the route instead return a 404 Not Found error with a JSON response of {"error": "Email not found."}
</details>

## 2025-07-08
<details>
<summary>1. Listed down main functions, DB</summary>

<details>
<summary>1.1. Functions were built by CS50</summary>

- Tables of database
    - `User`: stores users registered
    - `Email`: stores details of all emails composed by users
- Register a new account
- Log in
- Log out
- API

_*To additionally practice, I will develop myself the functions_

</details>

<details>
<summary>1.2. Functions that learners must complete</summary>

Single-page front-end email client built with JavaScript

- Send Mail
- Load mailbox
- Display details of an email
- Mark an email as read
- Archive an email
- Reply the email
</details>

</details>

<details>
<summary>2. Learning Notes</summary>

- `a front-end for an email client`

    Not static UI. It means dynamic UI:

    Dynamic UI refers to a user interface that can change or update its content and structure in response to user interactions or data changes, without requiring a full page reload. It often relies on client-side technologies such as JavaScript, AJAX, or frameworks like React, Vue, or Angular to update the UI dynamically and provide a smoother, more interactive user experience.

- `they won’t actually be sent to real email servers`

    Emails will not be sent to actual servers of email services (Gmail, Yahoo, Outlook...) which are used to send and receive emails over the Internet.

- `credentials need not be valid credentials for actual email addresses`

    Don't need use actual email address and password

- `Note that if the email doesn’t exist, or <u>if the user does not have access to the email</u>, the route instead return a 404 Not Found error with a JSON response of {"error": "Email not found."}`

    - What does it mean?

        Need to check if the user has permission to access the mail before return it to them

    - Why do we need to double check the issue while after the user logs in, they can see only sent and recieved emails?

        - Never trust user input
            - The user can fix URL like `emails/123` while id `123` is not owned by them
            - Development error by dev/QA makes Security vulnerability

    - New knowledge about security

        - Should use `404` (Not found error - means the email not exist) than `403` (Forbiden - the email existed but the user is not owner -> hacker still can try to find way to access the email)
        - Cache bugs
            - A person logs in -> email `123` is saved to cache
            - A person logs out, B person logs in -> cache still saves `123`
            - B person reload the page -> frontend sends `GET /emails/123/` to backend

</details>

## 2025-07-09
<details>
<summary>1. Defined details of functions, models (to be continued)</summary>

<details>
<summary>1.1 Tables of database (done)</summary>

<details>
<summary>a. `User` table</summary>

Where stores users registered new account

Inherit from `AbstractUser` model provided by Django, not add or change any fields.
</details>

<details>
<summary>b. `Email` table</summary>

Where stores details of all emails composed by users

- `id` (auto created by Django)
- `user` (to authorize inputs from a user)
    - ForeignKey
    - on_delete=models.CASCADE
    - related_name="emails"
- `sender`
    - ForeignKey
    - on_delete=models.CASCADE
    - related_name="emails_sent"
- `recipients`
    - ManyToManyField
    - on_delete=models.CASCADE
    - related_name="emails_recieved"
- `subject`
    - CharField(max_length=255)
- `body`
    - TextField
    - blank=True
- `timestamp`
    - DateTimeField(auto_now_add=True)
- `read`
    - BooleanField(default=False)
- `archived`
    - BooleanField(default=False)
- `serialize(self)`
    - id = self.id
    - sender = self.sender.email
    - recipients = [recipient.email for recipient in self.recipients.all()]
    - subject = self.subject
    - body = self.body
    - timestamp = self.timestamp.isoformat()
    - read = self.read
    - archived = self.archived
</details>

</details>

<details>
<summary>1.2. Register a new account (done)</summary>

<details>
<summary>a. UI</summary>

- Heading: `Register a new account`
- Input 1: email
- Input 2: password
- Input 3: password (to confirm)
- Button: `Register`
- Href: `Already have a account <link> Login here`
- A message will be dislayed to indicate the result of the registration
</details>

<details>
<summary>b. Logic</summary>

- url `register/`
- method == POST 
    - get `email`, `password` , `confirmed_password`
    - `password` != `confirmed_password`
    - render `emails/register.html`, message: `Passwords must match.`
    - `password` == `confirmed_password`
    - create a new `User` instance
    - user.save()
    - log_in(request, user)
    - redirect("index")
- method == GET
    - render `emails/register.html`
</details>

</details>

<details>
<summary>1.3. Log in (done)</summary>

<details>
<summary>a. UI</summary>

- Heading: `Log in`
- Input 1: email
- Input 2: password
- Button: `Log In`
- Href: `Don't have account? <link> Sign up.`
- A message will be dislayed to indicate the result of the login
</details>

<details>
<summary>b. Logic (done)</summary>

- url `login/`
- method == POST
    - get `email`, `password`
    - user = authenticate(request, username=email, password=password)
    - user is None
    - return `emails/login.html`, message: `Invalid email and/or password.`
    - use is not None
    - log_in(request, user)
    - redirect("index")
- method == GET
    - render `emails/login.html`
</details>

</details>

<details>
<summary>1.4. Log out (done)</summary>

<details>
<summary>a. UI</summary>

- Button: `Log out`
</details>

<details>
<summary>b. Logic</summary>

- url `logout/`
- method == GET
    - log_out(request)
    - redirect("login_view")
</details>

</details>

<details>
<summary>1.5. Inbox page (to be continued)</summary>

<details>
<summary>a. UI</summary>

<details>
<summary>a1. Header</summary>

- Heading: User’s email address
- Button: `Log out`
- Navibar
    - Button 1: `Inbox`
    - Button 2: `Sent`
    - Button 3: `Archived`
    - Button 4: `+ Compose`
</details>

<details>
<summary>a2. Main</summary>

- Compose
    - Heading: `Compose a new email`
    - Input 1: `To`
    - Input 2: `Subject`
    - Input 3: Body
    - Button: `Send`

- `Inbox` mailbox
    - Heading: `Inbox`
    - Display each email of a list by a box
        - Sender
        - Subject
        - Timestamp

- `Sent` mailbox
    - Heading: `Sent`
    - Display each email of a list by box
        - `To:` recipients
        - Subject
        - Timestamp

- `Archived` mailbox
    - Heading: `Archived`
    - Display each email of a list by box
        - Sender
        - Subject
        - Timestamp
    - Button: `Unarchive`
    
- Details of an email
    - `From:` sender
    - `To:` recipients
    - `Subject:` subject
    - `Timestamp:` timestamp
    - Button 1: `Reply`
    - Button 2: `Archive`
    - Body

- Reply
    - Input 1: `To:` pre-fill sender email of the mail
    - Input 2: `Re:` pre-fill subject of the email
    - Input 3: pre-fill `On Jan 1 2020, 12:00 AM <sender email> wrote: <body of the email>`
    - Button: `Reply`
</details>

</details>

</details>

</details>

<details>
<summary>2. Learning Notes</summary>

- `How to choose correct Field types for a field when use Model of Django`

    - Learn some popular Field types
    - Define datatype of the field
    - Check table of contents at [Django documentation](https://docs.djangoproject.com/en/5.2/)
    - Pick up some field types corresponding to defined datatype
    - Read their usages
    - Pick up correct field type

- `How doese Django authenticate username and password`

    - Search if username exists in `User` table
    - If existed, get hashed password corresponding to the username
        - Split the hashed password into `algorithm`, `number of iteration` and `salt`
        - Use them to hash input password
        - Compare stored hashed password with hashed input password
        - If match, return a corresponding user object
        - If no match, return `None`
    - If not existed, return `None`

- `Why do we need to call "log_in(request, user)" after authentication?`

    - Authentication only verifies the credentials
    - Call `log_in(request, user)` starts a session and logs the user in
    - If skip the call, the user is not remembered as logged in, so request.user will AnonymousUser. They will still appear as logged out even if credentials are valid

</details>

## 2025-07-10

<details>
<summary>1. Defined details of functions, models (continue)</summary>

<details>
<summary>1.5. Inbox page (continue)</summary>

<details>
<summary>b. Logic</summary>

<details>
<summary>b1. Send email</summary>

<details>
<summary>Goal</summary>

When user submits the email composition form, add Javascript to actually sent the email
</details>

<details>
<summary>b1.1. Frontend</summary>

- Prolem to solve
    - Make an API request (url: `emails`, method: `POST`, email contents from user input) to backend
    - Display sending result on UI

- Input
    - Button: `Send`
    - Event: `onclick`
    - URL: `emails/`
    - Method: `POST`
    - Email data:
        - recipients: `<input type="text" name="recipients">`
        - subject: `<input type="text" name="subject">`
        - body: `<textarea name="body"></textarea>`

        _*Note_
        - `recipients` is a comma-separated string of email addresses. 
            - It should be converted from `str` to `list` before it is sent to server
            - Maybe user enters wrong format like redundant comma/space. Example: `"'a@gmail.com',   ,'b@gmail.com',,,, 'c@gmail.com','d@gmail.com`. 
        - For other fields, maybe user enters wrong format like redundant sapce

- Action flow
    - Wait for the DOM is loaded fully
    - Select button `Send`
    - Add an `onclick` event listener to the button
    - Get values of user input `sender`, `recipients`, `subject`, `body`
        - `<user input>.trim()`
        - Validate user input
            - If one of user input is empty
                - console.log("Don't leave empty fields.")
                - Create a `<div></div>` new element with class name `error-message`
                - Add `Don't leave empty fields.` to the `error-message`
                - Append the `error-message` to `emails-view`
        - `recipients.split(",")` -> `<each_recipient>.trim()` -> filter no-empty recipients
    - Convert Javascript user input object to string
    - Send a request `POST` with body `converted string` to `emails/`
    - If there is network error, catch and handle it
        - console.log("Error:", error)
        - Create a `<div></div>` new element with class name `error-message`
        - Add `error` to the `error-message`
        - Append the `error-message` to `emails-view`
    - If it is ok, backend processes the request and send back an approriate response to frontend
    - If the reponse is not ok, catch and handle it
        - console.log(`HTTP error, status $response.status.`)
        - Create a `<div></div>` new element with class name `error-message`
        - Add `HTTP error, status $response.status. $response.error` to the `error-message`
        - Append the `error-message` to `emails-view` 
    - If the reponse is ok, convert JSON string to Javascript object
        - console.log("Sending email successfully.")
        - Create a `<div></div>` new element with class name `success-message`
        - Add `Sending email successfully.` to the `success-message`
        - Append the `success-message` to `success-message`

- Output
    - UI displays a message about sending result
</details>

</details>

</details>

</details>

</details>

<details>
<summary>2. Learning notes</summary>

- `Why do we need "JSON.stringify()?`

    Because JavaScript objects need to be converted into JSON strings before being sent over the network. The string is then encoded into binary (0s and 1s), which the CPU converts into electrical signals. These signals travel through cables to the target server, where they're decoded back into binary, converted into a JSON string, and then parsed into a Python object on the backend. The backend processes this object and sends a response back to the frontend for display.

- `Why do we need programming languages and compilers/interpreters?`

    - A programming language allows humans to communicate with computers more easily, as it uses syntax and structure similar to natural language.
    - However, computers can only understand binary (0s and 1s), so a compiler or interpreter is needed to translate the code into machine-understandable instructions.

- `Why do we use "!value" to validate user input?`

  - Because it covers all falsy values in JavaScript, including: `false`, `0`, `""`, `null`, `undefined`, and `NaN`.
  - It’s more concise and less error-prone than checking each case manually.

- We use `map()` when we want to transform or modify each item in an array. It creates a new array.

- We use `filter()` to select elements that meet a certain condition. It creates a new array.

- `How to name a variable with "camelCase" in Javascript`

    The first word is written in lowercase, and the first letter of each subsequent word is capitalized.
    No spaces, underscores, or hyphens are used.

    ```
        Naming	            Example	        Usecases
        camelCase	        userName	    variable, function
        PascalCase	        UserProfile	    Class, Component, Constructor
        snake_case	        user_name	    Python, file, environment variable
        kebab-case	        user-profile	URL, CSS class, file name
        UPPER_SNAKE_CASE	MAX_VALUE	    Constants
    ```

- For `form`, use `onsubmit` event. For `button`, use `onclick` event.

- Always validate input data before processing logic.

</details>

## 2025-07-12

<details>
<summary>1. Defined details of functions, models (continue)</summary>

<details>
<summary>1.5. Inbox page (continue)</summary>

<details>
<summary>b. Logic</summary>

<details>
<summary>b1. Send email (done)</summary>

<details>
<summary>Goal</summary>

When user submits the email composition form, add Javascript to actually sent the email
</details>

<details>
<summary>b1.2. Backend</summary>

- Problem to solve
    - Create a new email to `Email` table
    - Send back to frontend a response about result of sending email

- Input
    - request.user = "abc@gmail.com"
    - request.url = "emails/"
    - request.method = "POST"
    - request.body = emailData = "{recipients: ['a', 'b', 'c'], subject: 'Hello, body: 'Hello!'}"

- Action flow
    - Find `path('emails/', views.new_email, name=new_email)`
    - Process view `new_email(request)`
        - Verify that request.user logs in
            - If not yet, return `JsonResponse({'error': 'You not yet log in.'}, status=401)`
            - If logged in, process request
        - Process request
            - If request.method != 'POST'
                return `JsonResponse({'error': 'POST request required.', status = 405})`
            - If request.method == 'POST'
                - Get rawEmailPayLoad = request.body
                - Convert rawEmailPayLoad from string to JSON object: emailPayLoad = rawEmailPayLoad.json()
                - Get detailed email contents which are user input
                    - recipients = emailPayLoad['recipients']
                    - subject = emailPayLoad['subject']
                    - body = emailPayLoad['body']
                - Verify user input
                    - If not recipients or not subject or not body, return `JsonResponse({'error': 'Don't leave empty fields.'}, status=400)`
                    - If isinstance(recipients, str)
                        - recipientsList = recipients.split(',')
                        - recipientsList = [ email.strip() for email in recipientsList if email.strip()]
                    - If not isinstance(recipients, str)
                        - recipientsList = [email.strip() for email in recipientsList if email.strip()]
                        - recipientObjects = []
                    - Get recipientObjects = []
                        - for recipientEmail in recipientsList:
                            try
                                recipientObject = User.objects.get(username=recipientEmail)
                                recipientObjects.append(recipientObject)
                            exept User.DoesNotExist:
                                `JsonResponse({'error': f"'User with email {recipientEmail} do not exist."})`
                    - subject.strip()
                    - body.strip()
                - Create a instance of class `Email` without recipents because of `ManyToMany`
                    - newEmail = Email(user = request.user, sender = request.user, subject = subject, body = body)
                    - newEmail.save()
                - Add `recipientObjects` to newEmail.recipients
                - Return `JsonResponse({'message': 'Email sent successfully.', status = 201})`

- Output

    `JsonResponse({'message': '<message content>', status = <HTTP status>})`
    
</details>

</details>

</details>

</details>

</details>

<details>
<summary>2. Learning notes</summary>

- `!response.ok`

    We should check `!response.ok` before calling `response.json()` to clearly distinguish HTTP errors and successful reponses

- `Data format returned by backend (e.g.JSON, HTML, ...)`

    We should consider that data format returned by backend (e.g.JSON, HTML, ...) to ensure it is processed correctly on frontend

- `ManyToManyField` on Django Model

    Assume that you create an `Email` model which includes a `recipients` field. This field is defined as a `ManyToManyField` to `User` model. In the database, the `Email` table doesn't include `recipient` column. Instead, Django creates additional intermidiate table with columns like `id||email_id||user_id` to store `recipients` relationships.

    This is similar how we use raw SQL to create 3 tables: `user`, `email`, `email_recipients`.

- `User.objects.get(username=email)`

    We should use `.objects.get()` in `try/except` to handle error

    If user `if not User.objects.get(username=email)`, before the `if` statement is executed, `User.objects.get(username=email)` raises error if have error

</details>

## 2025-07-14

<details>
<summary>1. Defined details of functions, models (continue)</summary>

<details>
<summary>1.5. Inbox page (continue)</summary>

<details>
<summary>b. Logic</summary>

<details>
<summary>b2. Load mailbox</summary>

<details>
<summary>Goal</summary>

Display a list of emails corresponding to `mailbox` name (`inbox`, `sent`, `archive`) which user clicks on

- Each email is displayed in a box, means a `<div></div>`
- Emails are ordered from the latest one to the oldest one
- Email is read -> display `gray background`, email is unread -> display `white background`
</details>

<details>
<summary>b2.1. Frontend</summary>

- Problem to solve
    - Send an API request (url: `emails/<mailbox>`, method: `GET`) to backend
    - Display a list of emails corresponding to that mailbox or error message if have

- Input
    - Buttons: `inbox`, `sent`, `archive`
    - Event: `onclick`
    - URL: `emails/<mailbox>`
    - Method: `GET`

- Action flow
    - Wait for the DOM is loaded fully
    - Select all mailbox buttons `inbox`, `sent`, `archive`
    - Iterate through the list of buttons
    - Get the value of the button using `button.value`
    - Add an `onclick` event listener to each button
    - Send a `GET` request to backend with url `emails/<mailbox>`
    - If there is a network error, catch and handle it
        - console.log("Error:", error)
        - Create a `<div></div>` new element with class name `error-message`
        - Add `error` to the `error-message`
        - Append the `error-message` to `emails-view`
    - If it is ok, backend processes it and sends back a response to fontend
    - Get the response from backend
    - If response is error, display an error message
        - console.log(`HTTP error, status $response.status.`)
        - Create a `<div></div>` new element with class name `error-message`
        - Add `HTTP error, status $response.status. $response.error` to the `error-message`
        - Append the `error-message` to `emails-view` 
    - If response is not error, parse the JSON response returned by backend into a Javascript object
    - Get response body contains a list of email objects (each represented as a dictionary)
    - Iterate through the list
    - Create a `<div></div>` new element with class name `email-item`, `data-email-id="${email_id}"`, `data-mailbox="${mailbox}"` to store each email
    - Extract `sender`, `subject`, `timestamp`, `read` status
    - Append `sender`, `subject`, `timestamp` to the `email-item`
    - If `read` is False, set the background color of the email element to `white`
    - If `read` is True, set the background color of the email element to `gray`

- Output
    - UI displays a list of emails following to order by the latest one -> the oldest one. Read email box with `white` background, unread email box with `gray` background. Or error message if have

</details>

</details>

</details>

</details>

</details>

<details>
<summary>2. Learning notes</summary>

- Before using any function, we should understand clearly 3 things to be able to use it procactively and correctly
    - What `input` does the function require?
    - What does the function do?
    - What `output` does the function return?

- `Promise`
    - An object used to handle asynchronous operations.
    It acts as a placeholder for a value that is not available yet, but will be known in the future — either successfully (resolved) or with an error (rejected).

- `fetch()`
    - Input: (url, options(method: `<string>`, header: `<string>`, body: `<dict>`))
    - Make HTTP requests (GET, POST, etc.) in JavaScript. It allows you to communicate with APIs or servers asynchronously.
    - Output: `promise<response>`

- `then()`
    - Input: a callback function `onFullfilled`. Register it to be called after the promise is resolved. Pass the resolved value of the `promise` into `onFullfilled`
    - Define what to do next after a Promise resolves. It lets you handle the result of an async operation and chain actions.
    - Output: new `promise`

- `response.json()` returns a `promise<JSON object>`
</details>

## 2025-07-16
<details>
<summary>1. Defined details of functions, models (continue)</summary>

<details>
<summary>1.5. Inbox page (continue)</summary>

<details>
<summary>b. Logic</summary>

<details>
<summary>b2. Load mailbox (done)</summary>

<details>
<summary>Goal</summary>

Display a list of emails corresponding to `mailbox` name (`inbox`, `sent`, `archive`) which user clicks on

- Each email is displayed in a box, means a `<div></div>`
- Emails are ordered from the latest one to the oldest one
- Email is read -> display `gray background`, email is unread -> display `white background`
</details>

<details>
<summary>b2.2. Backend</summary>

- Problem to solve
    - Retrive a list of emails from the database corresponding to the selected mailbox. Emails are ordered by timestamp in descending order
    - Send back to frondent a JSON response containing a list of email objects

- Input
   - request.user
   - request.method
   - mailbox

- Action flow
    - Validate `request.user.is_authenticated`
        - If it is `False`, redirect("login_view")
        - Otherwise, process the next action
    - Validate request.method
        - If it is not `GET`, return `JsonResponse({"error": "GET request required."}, status=405)`
        - Otherwise, process the next action
    - Retrieve a list of emails
        - mailbox = mailbox.lower()
        - If mailbox = `inbox`, emailsList = Email.objects.filter(recipients=request.user).order_by("-timestamp")
        - If mailbox = `sent`, emailsList = Email.objects.filter(sender=request.user).order_by("-timestamp")
        - If mailbox = `archived`, emailsList = Email.objects.filter(recipients=request.user, archived=True).order_by("-timestamp")
        - Otherwise, return `JsonResponse({"error": "Invalid mailbox."}, status=404)`
    - Convert each email objects of the `emailsList` to dictionary to get a list of email dictionaries
        - Tạo method `serialize()` trong class `Email` -> make migration -> migrate
        - emailData = [email.serialize() for email in emailsList]
    - Return `JsonResponse(emailData, status=200, safe=False)`

- Output
    - A HTTP response formating JSON, which contains a list of emails corresponding to the selected mailbox with timestamp in desceding order or a error message

    ```
        [
            {
                "id": 100,
                "sender": "foo@example.com",
                "recipients": ["bar@example.com"],
                "subject": "Hello!",
                "body": "Hello, world!",
                "timestamp": "Jan 2 2020, 12:00 AM",
                "read": false,
                "archived": false
            },
            {
                "id": 95,
                "sender": "baz@example.com",
                "recipients": ["bar@example.com"],
                "subject": "Meeting Tomorrow",
                "body": "What time are we meeting?",
                "timestamp": "Jan 1 2020, 12:00 AM",
                "read": true,
                "archived": false
            }
        ]
    ```

</details>
</details>

<details>
<summary>b3. Display details of an email</summary>

<details>
<summary>Goal</summary>

Display the content of an email.

- `sender`
- `recipients`
- `Subject`
- `Timestamp`
- `Body`
</details>

<details>
<summary>b3.1. Frontend</summary>

- Problem to solve
    - Make a `GET` request to `/emails/<email_id>`
    - Dislay detailed content of the email or error message if have

- Input
    - Selected email box with class name `email-item` which contain `data-email-id="<email_id>"`, `data-mailbox="<mailbox>"`
    - Event: `onclick`
    - URL: `/emails/<email_id>`
    - Method" `GET`

- Action flow
    - Wait for the DOM is loaded fully
    - Select a list of elements with class name `email-item`
    - Iterate through the list
    - Add an `onclick` event listener to the element
    - Get email_id = `data-email-id="<email_id>"`, mailbox = `data-mailbox=<mailbox>` of the element
    - Make an `GET` request to `emails/<email_id>`
    - If there is network error, catch and handle it
        - console.log("Error:", error)
        - Create a `<div></div>` new element with class name `error-message`
        - Add `error` to the `error-message`
        - Append the `error-message` to `emails-view`
    - Otherwise, get a response returned by backend
    - If response is error, display an error message
        - console.log(`HTTP error, status $response.status.`)
        - Create a `<div></div>` new element with class name `error-message`
        - Add `HTTP error, status $response.status. $response.error` to the `error-message`
        - Append the `error-message` to `emails-view` 
    - Otherwise, parse the JSON response returned by backend into a Javascript object
    - Get response result and handle it
    - Create a new `<div></div>` to store email contents with class name `email-detail-view`
    - Get `sender`, `recipients`, `subject`, `timestamp`, `body`
    - Get mailbox = `data-mailbox="<mailbox>"`
    - If mailbox = `inbox`
        - emailContents = 
            `<p>$request.sender</p>`
            `<p>$request.recipients</p>`
            `<p>$request.subject</p>`
            `<p>$request.timestamp</p>`
            `<button id="reply-btn" data-email-id="${email_id}">Reply</button>`
            `<button id="archived-btn" data-email-id="${email_id}">Archived</button>`
            `<hr>`
            `<p>$request.body</p>`

    - If mailbox = `archived`
        - emailContents = 
            `<p>$request.sender</p>`
            `<p>$request.recipients</p>`
            `<p>$request.subject</p>`
            `<p>$request.timestamp</p>`
            `<button id="unarchived" data-email-id="${email_id}">Unarchived</button>`
            `<hr>`
            `<p>$request.body</p>`

    - If mailbox = `sent`
        - emailContents = 
            `<p>$request.sender</p>`
            `<p>$request.recipients</p>`
            `<p>$request.subject</p>`
            `<p>$request.timestamp</p>`
            `<hr>`
            `<p>$request.body</p>`

    - Add `emailContents` to the `email-detail-view`
    - Add the `email-detail-view` to the `emails-view`
    
- Output
    - UI dislays `sender`, `recipients`, `subject`, `timestamp`, `body` of a certain email or or error message if have
</details>

<details>
<summary>b3.2. Backend</summary>

- Problem to solve
    - Filter an email by `email_id` and `request.user`
    - Send back to frontend an reponse containing a email contents dictionary

- Input
    - `email_id`
    - method = `GET`

- Action flow
    - Validate `request.user.is_authenticated`
        - If it is `False`, redirect("login_view")
        - Otherwise, process the next action
    - Validate request.method
        - If it is not `GET`, return `JsonResponse({"error": "GET request required."}, status=405)`
        - Otherwise, process the next action
    - Get an email by `email_id` and `request.user`
        - If there is error, return `JsonResponse({"error": "Not found."}, status=404)`
        - Otherwise, serialize the email
    - Return `JsonResponse(email, safe=False, status=200)`

- Output
    - An HTTP response formatted JSON, which contains contents of a specific email

    ```
        {
            "id": 100,
            "sender": "foo@example.com",
            "recipients": ["bar@example.com"],
            "subject": "Hello!",
            "body": "Hello, world!",
            "timestamp": "Jan 2 2020, 12:00 AM",
            "read": false,
            "archived": false
        }
    ```

</details>
</details>

<details>
<summary>b4. Mark an email as read</summary>

<details>
<summary>Goal</summary>

Once an email has been clicked on, should mark the email as read. Send a `PUT` request to `/emails/<email_id>` to update whether an email is read or not.
</details>

<details>
<summary>b4.1. Frontend</summary>

- Problem to solve
    - Send a `PUT` request to `/emails/<email_id>`
    - Display a message about the result of updating read status

- Input
    - `email_id`
    - Method: `PUT`
    - URL: `/emails/<email_id>`

- Action flow
    - Get email_id = `data-email-id=<email_id>` of the email
    - Make a `PUT` request to `/emails/<email_id>`
    - If there is network error, catch and handle it
        - console.log("Error:", error)
        - Create a `<div></div>` new element with class name `error-message`
        - Add `error` to the `error-message`
        - Append the `error-message` to `emails-view`
    - Otherwise, get a response returned by backend
    - If response is error, display an error message
        - console.log(`HTTP error, status $response.status. $response.error`)
        - Create a `<div></div>` new element with class name `error-message`
        - Add `HTTP error, status $response.status. $response.error` to the `error-message`
        - Append the `error-message` to `emails-view` 
    - Otherwise, parse the JSON response returned by backend into a Javascript object
    - Get response result and handle it
        - console.log("Marked as read.")
        - Create a `<div></div>` new element with class name `success-message`
        - Add `Marked as read.` to the `success-message`
        - Append the `success-message` to `emails-view`

- Output
    - UI displays a message about the result of updating read status

</details>

<details>
<summary>b4.2. Backend</summary>

- Problem to solve
    - Mark an `email_id` as read
    - Send back to frontend a response about result of updating read status

- Input
    - `email_id`
    - URL: `emails/<email_id>`
    - method: `PUT`

- Action flow
    - Validate `request.user.is_authenticated`
        - If it is `False`, redirect("login_view")
        - Otherwise, process the next action
    - Validate request.method
        - If it is not `PUT`, return `JsonResponse({"error": "PUT request required."}, status=405)`
        - Otherwise, process the next action
    - Get an email by `email_id` and `request.user`
        - If there is error, return `JsonResponse({"error": "Not found."}, status=404)`
        - Otherwise, change `read` field to `True`
    - Save the `email`
    - Return `JsonResponse({"message": "Marked as read."}, status=200)`

- Output
    - An HTTP response formatted JSON containing a message about the result of updating read status

</details>
</details>

<details>
<summary>b5. Archive an email</summary>

<details>
<summary>Goal</summary>

User can archive and unarchive emails that they have received.
- Inbox email: click `Archived` button: `archived=False` -> `archived=True`
- Archived email: click `Unarchived` button: `archived=True` -> `archived=False`
</details>

<details>
<summary>b5.1. Frontend</summary>

- Problem to solve
    - Send a `PUT` request to `/emails/<email_id>`
    - Display a message about the result of updating archived status

- Input
    - Buttons: `archived`, `unarchived`
    - `email_id`
    - Method: `PUT`
    - URL: `/emails/<email_id>`

- Action flow
    - Wait for the DOM is loaded fully
    - Select an `#archived-btn`/`#unarchived-btn` button
    - Add an `onclick` event listener to the button
    - Get email_id = `data-email-id=<email_id>` of the button
    - Make a `PUT` request to `/emails/<email_id>`
    - If there is network error, catch and handle it
        - console.log("Error:", error)
        - Create a `<div></div>` new element with class name `error-message`
        - Add `error` to the `error-message`
        - Append the `error-message` to `emails-view`
    - Otherwise, get a response returned by backend
    - If response is error, display an error message
        - console.log(`HTTP error, status $response.status. $response.error`)
        - Create a `<div></div>` new element with class name `error-message`
        - Add `HTTP error, status $response.status. $response.error` to the `error-message`
        - Append the `error-message` to `emails-view` 
    - Otherwise, parse the JSON response returned by backend into a Javascript object
    - Get response result and handle it
        - console.log("Archived.")/console.log("Unarchived.")
        - Create a `<div></div>` new element with class name `success-message`
        - Add `Archived.`/`Unarchived` to the `success-message`
        - Append the `success-message` to `emails-view`

- Output
    - UI displays a message about the result of updating archived status

</details>

<details>
<summary>b5.2. Backend</summary>

- Problem to solve
    - Mark an `email_id` as archived/unarchived
    - Send back to frontend a response about result of updating archive status

- Input
    - `email_id`
    - URL: `emails/<email_id>`
    - method: `PUT`

- Action flow
    - Validate `request.user.is_authenticated`
        - If it is `False`, redirect("login_view")
        - Otherwise, process the next action
    - Validate request.method
        - If it is not `PUT`, return `JsonResponse({"error": "PUT request required."}, status=405)`
        - Otherwise, process the next action
    - Get an email by `email_id` and `request.user`
        - If there is error, return `JsonResponse({"error": "Not found."}, status=404)`
        - Otherwise, change `archived` = `not archived`
    - Save the `email`
    - message = "Archived." if email.archived else "Unarchived."
    - Return `JsonResponse({"message": message}, status=200)`

- Output
    - An HTTP response formatted JSON containing a message about the result of updating archive status

</details>
</details>

<details>
<summary>b6. Reply the email (to be continued)</summary>

</details>

</details>


</details>

</details>

</details>

<details>
<summary>2. Learning notes</summary>

- `request.user`
    - If user does not log in, `request.user` is considered as `AnonymousUser`in Django

- We must authenticate the user before processing any action
    - Otherwise, if the developer writes code like `emails = Email.objects.filter(archived=True)` without filtering by the user, UI maybe display all archived emails from the entire DB

- `Email.objects.filter()`
    - Not return `None` if not found object, it returns a empty list.
    - If queryset is not empty, it returns a list of object
    - Must convert each object to string to transform the data through internet

- `isoformat()`
    - `timestamp` is datetime object -> must convert to string using `isoformat()` to transform the data through internet

</details>

## 2025-07-19

<details>
<summary>1. Defined details of functions, models (continue)</summary>

<details>
<summary>1.5. Inbox page (continue)</summary>

<details>
<summary>b. Logic</summary>

<details>
<summary>b1. Send email (done)</summary>

</details>

<details>
<summary>b2. Load mailbox (done)</summary>

</details>

<details>
<summary>b3. Display details of an email (done)</summary>

</details>

<details>
<summary>b4. Mark an email as read (done)</summary>

</details>

<details>
<summary>b5. Archive an email (done)</summary>

</details>

<details>
<summary>b6. Reply the email</summary>

<details>
<summary>Goal</summary>

User can reply an email
- Pre-fill: recipients = sender, subject =  subject, body = `"On <timestamp> <sender_email> wrote: <email_body>"`
</details>

<details>
<summary>b6.1. Frontend</summary>

- Problem to solve
    - Pre-fill some values to composition form

- Input
    - Button: `Reply`
    - Event: `onclick`
    - Displayed email content in `email-detail-view`

- Action flow
    - Wait for the DOM is loaded fully
    - Select an `#reply-btn` button
    - Add an `onclick` event listener to the button
    - Get values from displayed email content in `email-detail-view` to pre-fill compostiton form
        - `recipients = #email-sender.innerHTML`
        - `subject =  #email-subject.innerHTML`
            - If `Re: ` in subject, return replySubject = subject
            - Otherwise, return replySubject = `Re: ${subject}`
        - `body = #email-body.innerHTML`
        - `timestamp =  #email-timestamp.innerHTML`
    - Hide `emails-view`
    - Show `compose-view`
    - Select and replace values of `input` elements of `compose-view`
        - document.querySelector("#compose-sender").value = request.user
        - document.querySelector("#compose-recipients").value = recipients
        - document.querySelector("#compose-subject").value = replySubject
        - document.querySelector("#compose-body").value = `/n/nOn ${timestamp recipients} wrote: /n${body}`

- Output

</details>

<details>
<summary>b6.2. Backend</summary>

- Problem to solve (N/A)

- Input (N/A)

- Action flow (N/A)

- Output (N/A)

</details>
</details>

</details>


</details>

</details>

</details>

<details>
<summary>2. Learning notes</summary>

- `.value`, `.innerHTML`
    - `.value` for values of user input  (`input`, `select`, `textarea`)
    - `.innerHTML` for displayed HTML content (`div`, `p`, ...)

</details>

## Notes

<details>
<summary>1. Default route `index`</summary>

- User signed in
- Render `mail/inbox.html`
    - The `user’s email address` is first displayed in an `h2` element
    - Buttons for navigating
    - <div class="emails-view"></div>
        The content of an email mailbox
    - <div class="compose-view"></div>
        A form where the user can compose a new email
    - Selectively show and hide these views:
        - `compose` button -> hide `emails-view` - show `compose-view`
        - `inbox` button -> hide `compose-view` - show `emails-view`
    - DOM content of the page has been loaded -> attach event listeners to each of the buttons
        - `inbox` button is clicked
            -> call the `load_mailbox` function with the argument `inbox`
            - Shows `emails-view`
            - Hides `compose-view`
            - Name of mailbox = `inbox`
            - Takes an argument `inbox`
            - Capitalize the first character
            - Updating `innerHTML` of the `emails-view` = `inbox`

            _*Similarly, `sent`, `archived`_

        -  `compose` button is clicked 
            -> call the `compose_email` function
            - Hides `emails-view`
            - Shows `compose-view`
            - Takes all of the form input fields
            - Recipient email address
            - Subject line
            - Email body
            - Sets their value to the empty string '' to clear them 
</details>

<details>
<summary>2. API</summary>

- `GET /emails/<str:mailbox>` (mailbox = `inbox`, `sent`, `archived` )

    Get a list of all emails

    - Return _a list of all emails_ in that mailbox, in _reverse chronological order_ in _JSON format_
        - `id` 
        - `sender`: a sender email address
        - `recipients`: an array of recipients
        - `subject`: a string for subject
        - `body`: body
        - `timestamp`: timestamp
        - `read`: boolean values
        - `archived`: boolean values

    - How to recall

        ```
            fetch('/emails/<str:mailbox>')
            .then(response => response.json())
            .then(emails => {
                // Print emails
                console.log(emails);

                // ... do something else with emails ...
            });
        ```

    - Note
        invalid mailbox (anything other than `inbox`, `sent`, or `archive`) -> get back the JSON response `{"error": "Invalid mailbox."}`

- `GET /emails/<int:email_id>`

    Get details of an email

    - Return a JSON representation of the email
        - `id` 
        - `sender`: a sender email address
        - `recipients`: an array of recipients
        - `subject`: a string for subject
        - `body`: body
        - `timestamp`: timestamp
        - `read`: boolean values
        - `archived`: boolean values

    - How to call

        ```
            fetch('/emails/<int:email_id>')
            .then(response => response.json())
            .then(email => {
                // Print email
                console.log(email);

                // ... do something else with email ...
            });
        ```

    - Note
        email doesn’t exist/the user does not have access to the email -> route return a `404 Not Found error` with a JSON response of `{"error": "Email not found."}`

- `POST /emails`

    Compose a new email

    - Requires three pieces of data to be submitted
        - a `recipients` value (a `comma-separated string` of all users to send an email to)
        - a `subject` string
        - a `body` string

    - How to call

        ```
            fetch('/emails', {
            method: 'POST',
            body: JSON.stringify({
                recipients: 'baz@example.com',
                subject: 'Meeting time',
                body: 'How about we meet tomorrow at 3pm?'
            })
            })
            .then(response => response.json())
            .then(result => {
                // Print result
                console.log(result);
            });
        ```

    - Note
        - Email is sent successfully -> respond with a `201` status code and a JSON response of `{"message": "Email sent successfully."}`
        - Must be `at least one email recipient`
            - Recipient is blank -> respond with a `400` status code and a JSON response of `{"error": "At least one recipient required."}`
        - `All recipients must be valid users` who have registered on this particular web application
            - Try to send an email to invalid email -> get a JSON response of `{"error": "User with email <email_address> does not exist."}`

- `PUT /emails/<int:email_id>`

    Modify some fields of a email

    - Mark an email as read/unread or as archived/unarchived

    - How to call

        ```
            fetch('/emails/<int:email_id>', {
            method: 'PUT',
            body: JSON.stringify({
                archived: true
            })
            })
        ```

</details>