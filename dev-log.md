# Project: Email client SPA

A single-page front-end email client built with JavaScript.

## 2025-07-07
- Read project information to understand overview of the project
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

- Noted some keywords which need to be searched to more understand:
    - `a front-end for an email client`
    - `they won’t actually be sent to real email servers`
    - `credentials need not be valid credentials for actual email addresses`
    - Note that if the email doesn’t exist, or `if the user does not have access to the email`, the route instead return a 404 Not Found error with a JSON response of {"error": "Email not found."}

## 2025-07-08
- Listed down main functions, DB
    - Models for DB
        - `User`: stores user registered
        - `Email`: stores details of all emails composed by users
    - Register a new account
    - Log in
    - Log out
    - Send Mail
    - Load mailbox
    - View details of email
    - Mark an email as read
    - Archive an email
    - Reply the email
- Searched some noted keywords
    - `a front-end for an email client`
        Not static UI. It means dynamic UI:
        Dynamic UI refers to a user interface that can change or update its content and structure in response to user interactions or data changes, without requiring a full page reload. It often relies on client-side technologies such as JavaScript, AJAX, or frameworks like React, Vue, or Angular to update the UI dynamically and provide a smoother, more interactive user experience
    - `they won’t actually be sent to real email servers`: 
        Emails will not be sent to actual servers of email services (Gmail, Yahoo, Outlook...) which are used to send and receive emails over the Internet.
    - `credentials need not be valid credentials for actual email addresses`.
        Don't need use actual email address and password
    - Note that if the email doesn’t exist, or `if the user does not have access to the email`, the route instead return a 404 Not Found error with a JSON response of {"error": "Email not found."}
- Details of functions, models
    - Default route `index`:
            - User signed in
            - Render `mail/inbox.html`
                - The `user’s email address` is first displayed in an `h2` element
                - Buttons for navigating
                - <div class="emails-view"></div>
                    the content of an email mailbox
                - <div class="compose-view"></div>
                    a form where the user can compose a new email
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
                        *Similarly, `sent`, `archived`
                    -  `compose` button is clicked 
                        -> call the `compose_email` function
                        - hides `emails-view`
                        - shows `compose-view`
                        - Takes all of the form input fields
                        - recipient email address
                        - subject line
                        - email body
                        - Sets their value to the empty string '' to clear them out
        - API
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