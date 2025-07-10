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
<summary>2. Q&A</summary>

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
<summary>1. Defined details of functions, models</summary>

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
<summary>b. Logic

- url `logout/`
- method == GET
    - log_out(request)
    - redirect("login_view")
</details>

</details>

<details>
<summary>1.5. Inbox page</summary>

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

<details>
<summary>b. Logic</summary>

- Send Mail
    - Button["Send"].onsubmit = () => {fetch(url, {method: 'POST', body: JSON.stringify(data)})}
        - url = `emails/`
        - data = {recipients: ['a@gmail.com', 'a@gmail.com', 'a@gmail.com'],
                subject: `
        }
- Load mailbox
- View details of email
- Mark an email as read
- Archive an email
- Reply the email
</details>

</details>

</details>

<details>
<summary>2. Q&A</summary>

- `How to choose correct Field types for a field when use Model of Django`

    - Learn some popular Field types
    - Define datatype of the field
    - Check table of contents at [Django documentation](https://docs.djangoproject.com/en/5.2/)
    - Pick up some field types corresponding to defined datatype
    - Read their usages
    - Pick up correct field type

- `How Django authenticates username and password`

    - Search if username exists in `User` table
    - If existed, get hashed password corresponding to the username
        - Split the hashed password into `algorithm`, `number of iteration` and `salt`
        - Use them to hash input password
        - Compare stored hashed password with hashed input password
        - If match, return a corresponding user object
        - If no match, return `None`
    - If not existed, return `None`

- `Why need to call "log_in(request, user)" after authentication?`

    - Authentication only verifies the credentials
    - Call `log_in(request, user)` starts a session and logs the user in
    - If skip the call, the user is not remembered as logged in, so request.user will AnonymousUser. They will still appear as logged out even if credentials are valid
</details>


## Notes

<details>
<summary>1. Default route `index`</sumamry>
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