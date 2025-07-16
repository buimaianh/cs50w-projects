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
- View details of email
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
- View details of email
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
<summary>1.1 Tables of database</summary>

<details>
<summary>a. `User` table</summary>

    Where stores users registered

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
</details>

</details>

<details>
<summary>1.2. Register a new account</summary>

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
<summary>1.3. Log in</summary>

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
<summary>b. Logic</summary>

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
<summary>1.4. Log out</summary>

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

When user submits the email composition form, add Javascript to actually sent the email

<details>
<summary>b1.1. Frontend</summary>

- Prolem to solve
    - Call a API request (url: `emails`, method: `POST`, email contents from user input) to backend
    - Get a corresponding reponse from backend about sending email result
    - Load `sent` mailbox

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

- Action
    - Load DOM
    - Get button `Send`
    - Add event listener `onclick` to the button
    - Get user input
    - Convert Javascript user input object to string
    - Send a request `POST` with body `converted string` to API with url ``emails/`
    - Before backend gets the request, if have any problem like internet is dropped, url not found,..., need to catch the error and handle the error
    - If backend gets request successfully, backend processed the request and send back an approriate response
    - If the reponse is not ok, throw out an error message
    - If the reponse is ok, convert JSON string to Javascript object
    - Get response body
    - Display the response body to UI
    - Load `sent` mailbox

    ```    
        function getInputUser () {
            const recipientsInput = document.querySelector("#recipients").value;
            const subjectInput = document.querySelector("#subject").value.trim();
            const bodyInput = document.querySelector("#body").value.trim();

            if (!recipientsInput || !subjectInput || !bodyInput) {
                alert("Please fill in all fields.");
                return;
            }
            
            const recipientsList = recipientsInput.split(",")
            .map(email => email.trim())
            .filter(email => email);

            const emailPayLoad = {
                recipients: recipientsList,
                subject: subjectInput,
                body: bodyInput
            };

            return emailPayLoad;
        }

        function fetchSentEmail(emailPayLoad) {
            fetch("emails/", {method: "POST", body: JSON.stringify(emailPayLoad)})
            .then(response => {if (!response.ok) {throw new Error(`HTTP error, status:${response.status}`)}response.json()})
            .then(result => {console.log("Email sent successfully:", result);})
            .catch(error => {console.log("Error sending email:", error);});
            }

        document.addEventListener("DOMContentLoaded", () => {
            const button = document.querySelector("#send");
            button.onclick = () => {
                const emailPayLoad = getInputUser();
                if (emailPayLoad) {
                    fetchSentEmail(emailPayLoad)
                }
            };
        });

        load_mailbox(`sent`)
    ```

- Output

    - Get a message "Sent the email successfully.", "Error sending the email.", "Recipients not existed", "Please fill in all fields.",...
    - A list of emails of `sent` mailbox
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
<summary>b1. Send email</summary>

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

- Action
    - Find `path('emails/', views.new_email, name=new_email)`
    - Process view `new_email(request)`
        - Verify that request.user logs in
            - If not yet, return JsonResponse({'message': 'You not yet log in.', status = 401})
            - If logged in, process request
        - Process request
            - If request.method != 'POST'
                return JsonResponse({'message': 'POST request required.', status = 422})
            - If request.method == 'POST'
                - Get rawEmailPayLoad = request.body
                - Convert rawEmailPayLoad from string to JSON object: emailPayLoad = rawEmailPayLoad.json()
                - Get detailed email contents which are user input
                    - recipients = emailPayLoad['recipients']
                    - subject = emailPayLoad['subject']
                    - body = emailPayLoad['body']
                - Verify user input
                    - If not recipients or not subject or not body, return JsonResponse({'message': 'Don't leave empty fields.'}, status=400)
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
                                JsonResponse({'message': f"'User with email {recipientEmail} do not exist."})
                    - subject.strip()
                    - body.strip()
                - Create a instance of class `Email` without recipents because of `ManyToMany`
                    - newEmail = Email(user = request.user, sender = request.user, subject = subject, body = body)
                    - newEmail.save()
                - Add `recipientObjects` to newEmail.recipients
                - Return JsonResponse({'message': 'Email sent successfully.', status = 201})

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
<summary>b1. Load mailbox</summary>

Display a list of emails corresponding to `mailbox` name (`inbox`, `sent`, `archive`) which user clicks on

- Each email is displayed in a box, means a `<div></div>`
- Emails are ordered from the latest one to the oldest one
- Email is read -> display `gray background`, email is unread -> display `white background`

<details>
<summary>b1.1. Frontend</summary>

- Problem to solve
    - Call a API request (url: `emails/<mailbox>`, method: `GET`) to backend
    - Display a list of emails corresponding to that mailbox

- Input
    - Buttons: `inbox`, `sent`, `archive`
    - Event: `onclick`
    - URL: `emails/<mailbox>`
    - Method: `GET`

- Action
    - Load DOM
    - Get a list of mailbox buttons `inbox`, `sent`, `archive`
    - Iterate the list
    - Get `value` attribute of the button using `button.value`
    - Add event listener `onclick` to the button
    - Call a API request (url: `emails/<mailbox>`, method: `GET`) to backend
    - If sending the request has a trouble, catch the error and handle it
    - If backend gets the request successfully, backend processes the request and sends back a response
    - Get response from backend
    - If response is error, throw out an error message
    - If response is not error, convert JSON string sent back by backend to Javascript object
    - Get response body including a list of dictionaries which stores contents of all emails
    - Iterate the list
    - Create a `<div></div>` to store each email
    - Get `sender`, `subject`, `timestamp`, `read`
    - Append `sender`, `subject`, `timestamp` to the `<div></div>`
    - If `read` is False, set background of the email box as `white`
    - If `read` is True, set background of the email box as `gray`

    ```
        function loadMailbox(mailbox) {
            document.addEventListener(" ", () => {
                const mailboxButtons = document.querySelectorAll(".mailbox-btns");

                mailboxButtons.forEach(mailboxButtons => {
                    mailboxButtons.onclick = () => {
                        const mailboxName = mailboxButtons.value;

                        fetch(`emails/${mailboxName}`)
                        .then(response => {
                            if (!response.ok) {throw new Error(`HTTP error, status: ${response.status}`)}
                            return response.json()
                            })
                        .then(emailList => {
                            console.log("Load mailbox successfully.");

                            emailList.forEach(email => {
                                const sender = `<p>${email.sender}</p>`;
                                const subject = `<p>${email.subject}</p>`;
                                const timestamp = `<p>${email.timestamp}</p>`;
                                const read = email.read;

                                const emailBox = document.createElement("div");
                                emailBox.className = "email-item

                                emailBox.innerHTML = sender + subject + timestamp;

                                if (read) {emailBox.style.background = "gray"} else {emailBox.style.background = "white"}

                                emailsView = document.querySelector("#emails-view")
                                emailsView.appendChild(emailBox)
                            })
                        })
                        .catch(error => console.log("Error:", error))
                    }
                        
                })
            })
        }
    ```
- Output
    - UI displays a list of emails following to order by the latest one -> the oldest one. Read email box with `white` background, unread email box with `gray` background

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