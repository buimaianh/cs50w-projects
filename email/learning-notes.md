# Learning notes

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

- `How to choose correct Field types for a field when use Model of Django`

    - Learn some popular Field types
    - Define datatype of the field
    - Check table of contents at [Django documentation](https://docs.djangoproject.com/en/5.2/)
    - Pick up some field types corresponding to defined datatype
    - Read their usages
    - Pick up correct field type

- `How does Django authenticate username and password`

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

- `.value`, `.innerHTML`
    - `.value` for values of user input  (`input`, `select`, `textarea`)
    - `.innerHTML` for displayed HTML content (`div`, `p`, ...)

- `If "ORM" does not exist, how to interact with database`
    - Basic Workflow Without ORM

        ```
            import sqlite3

            # 1. Connect to (or create) the database
            conn = sqlite3.connect('mydb.sqlite3')

            # 2. Create a cursor to execute SQL commands
            cursor = conn.cursor()

            # 3. Create a table (if it doesn't already exist)
            cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

            # 4. Insert a row of data
            cursor.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))

            # 5. Save (commit) the changes
            conn.commit()

            # 6. Query the data
            cursor.execute("SELECT * FROM users")
            print(cursor.fetchall())  # Prints all rows

            # 7. Close the connection
            conn.close()
        ```

        - `sqlite3.connect('mydb.sqlite3')`

             This is how you open (or create) a database to work with.

            - This connects to a SQLite database file named 'mydb.sqlite3'.
            - If the file doesn't exist, it will be automatically created.
            - It returns a connection object, stored in the variable conn.

        - `conn.cursor()`

            The cursor is your main tool for interacting with the database.

            - This creates a cursor object from the connection.
            - The cursor is used to:
                - `Send` SQL commands to the database (like SELECT, INSERT, UPDATE, etc.).
                - `Fetch results` from queries.

    - Performing Basic Operations (CRUD)

        ```
            Operation	    SQL	                                                Example
            Create	        INSERT INTO users (name) VALUES ('Bob');	        cursor.execute(...)
            Read	        SELECT * FROM users;	                            cursor.fetchall()
            Update	        UPDATE users SET name = 'Jane' WHERE id = 2;	    cursor.execute(...)
            Delete	        DELETE FROM users WHERE id = 3;	cursor.execute(...)

            *You must also manually commit changes for create/update/delete: conn.commit()
        ```

    - `Use Django's raw SQL API`
        
        ```
            # We'll assume you have a table users (id INT, name TEXT, email TEXT)

            # Raw SQL:
                from django.db import connection

            # SELECT One Row
            # user = User.objects.get(id=1)
                def get_user(user_id):
                    with connection.cursor() as cursor:
                        cursor.execute("SELECT id, name, email FROM users WHERE id = %s", [user_id])
                        row = cursor.fetchone()
                        if row:
                            return {'id': row[0], 'name': row[1], 'email': row[2]}
                        return None
            
            # SELECT Multiple Rows
            # users = User.objects.filter(name__icontains="john")
                def get_users_by_name(keyword):
                    with connection.cursor() as cursor:
                        cursor.execute("SELECT id, name, email FROM users WHERE name LIKE %s", [f"%{keyword}%"])
                        rows = cursor.fetchall()
                        return [{'id': r[0], 'name': r[1], 'email': r[2]} for r in rows]

            # INSERT
            # User.objects.create(name="Alice", email="alice@example.com")

                def create_user(name, email):
                    with connection.cursor() as cursor:
                        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", [name, email])

            # UPDATE
            # user = User.objects.get(id=1)
            # user.name = "Bob"
            # user.save()

                def update_user_name(user_id, new_name):
                    with connection.cursor() as cursor:
                        cursor.execute("UPDATE users SET name = %s WHERE id = %s", [new_name, user_id])
            
            # DELETE
            # User.objects.get(id=1).delete()
                def delete_user(user_id):
                    with connection.cursor() as cursor:
                        cursor.execute("DELETE FROM users WHERE id = %s", [user_id])

            # Best practice
                def run(sql, params=None):
                    with connection.cursor() as cursor:
                        cursor.execute(sql, params or [])  # dùng [] nếu không có param để tránh lỗi
                        if sql.strip().upper().startswith("SELECT"):  # kiểm tra câu SQL là SELECT hay không
                            return cursor.fetchall()  # chỉ SELECT mới trả về dữ liệu
                        return None  # còn lại (INSERT, UPDATE, DELETE...) không cần trả gì
        ```

    - `Wrap Queries as a Service Layer`
        - You can put all raw SQL logic into a file like `db_utils.py` and call from views like ORM.

    - `Notes & Best Practices`
        - Always use parameterized queries (`%s`) — never do `WHERE id = %s` % id → it’s vulnerable to SQL injection!
        - With `cursor.fetchone()` you get one row as a tuple.
        - With `cursor.fetchall()` you get a list of tuples.
        - You need to manually map data to dictionaries or objects.
        - For write operations (INSERT/UPDATE/DELETE), Django manages the transaction automatically unless you're in ATOMIC blocks.

- `Advantages of "ORM"`
    - Avoid SQL syntax like wrong column name, wrong table name, ...
    - Avoid SQL injecttion

        A hacker inserts malicious SQL code into user input.

        ```
            user_input = "1 OR 1=1"
            query = "SELECT * FROM users WHERE id = " + user_input
            cursor.execute(query)

            -> SELECT * FROM users WHERE id = 1 OR 1=1
            -> cursor.execute("SELECT * FROM users WHERE id = %s", [user_input])
        ```
    - Avoiding formatted error

        ```
            name = "O'Reilly"
            cursor.execute("SELECT * FROM users WHERE name = '%s'" % name)

            -> SELECT * FROM users WHERE name = 'O'Reilly'  -- redundant '
        ```

    - Readable, maintanable

- `What is "escape"?`
    - It makes special characters safe to use
    - what are special characters?
        
        ```
            Character	    Used in	               Meaning
            " / '	        Strings, SQL	       Used to wrap text; can cause syntax issues if not escaped
            \	            Programming	           Escape character (e.g. \" = quote inside string)
            %	            SQL, URLs	           Wildcard in SQL (LIKE '%name%'), space in URL (%20)
            _	            SQL	                    Wildcard in SQL (_ matches one character)
            ;	            SQL, Shell	            Ends a command; can chain commands (risky in SQL injection)
            --	            SQL	                    Starts a comment (everything after is ignored)
            < > &	        HTML	                Angle brackets and ampersand have special meaning (tags, entities)
            { } [ ]	        Programming, JSON	    Block markers or structure
            * + ? . ^ $	    Regex	                Special operators (match, repeat, etc.)
            `&	!`	        Logic, Bash
            @ #	            Various	                Metadata (@decorator, #hashtag, etc.)
        ```
- `Why are some data like "queryset, object, datetime" not a JSON serializable?`
    - Because `JSON`, stands for `Javascript object notation`, supports only simple data types like `str, int, float, true, false, list, array, dict`, we must extract a particular field or convert objects into a dictionary from `queryset, object`; or convert `datetime` to `str` before serializing the data - because the data is a complex object which `JSON` can not interpret directly.

- ` Backend validation pipeline`
    - Get request
        - HTTP method
        - URL
        - Request body
        - Headers
    - Pre-porcess
        - Validate method
        - Authenticate
    - Validate request body
        - Field-level check
            - Presence check
                - Key check
                - Value check
            - Type check
            - Formmat check
            - Lenght, limit check
            
        - Cross-field check
        - Contextual check
    - Clean data
    - Bussineess logic
    - Response a message and status code

- `Meaning of none, null, nan, '', false`

    ```
        Case        Explanation (in English)
        None	    Represents "nothing" or "no value" in Python. Often used when a variable hasn't been assigned a value yet.
        null	    The null value in JSON. When parsed in Python, it becomes None.
        NaN	        Stands for "Not a Number". Used to represent missing or undefined numerical data (commonly in pandas or NumPy).
        ''	        An empty string. It means the value exists, but it's just an empty piece of text.
        False	    A Boolean value meaning "not true" or a negative condition.
    ```

- `python manage.py makemigrations`
    - Analyze and save changes about schema of model at a `migration` Python file

- `python manage.py migrate`
    - Read `migration` Python file
    - Convert Python content to SQL commands
    - Send the SQL commands to database