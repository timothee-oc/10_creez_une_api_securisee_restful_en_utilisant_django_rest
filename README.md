# Installation

* Install Python (version >= 3.12.4) and make sure pip is installed alongside (version >= 24.1.2)
* This project uses pipenv to manage the virtual environment, you can install it with `pip install pipenv`
* Clone this repo in a local directory and `cd` into it
* Create a virtual environment with the command : `pipenv install` and enter it with `pipenv shell`
* `cd` into the **softdesk** directory and launch the following commands:
    1. `python manage.py migrate` to build database tables
    2. `python manage.py runserver` to launch the server 
* You can now access the api at the url [127.0.0.1:8000/](127.0.0.1:8000/)


# How to use

* You can use a tool like [Postman](https://www.postman.com/) to make API calls
* You should start with creating a user account with a **POST** request at [http://127.0.0.1:8000/users/](http://127.0.0.1:8000/users/)
* Then with you account credentials, you can get your access and refresh tokens with a **POST** at [http://127.0.0.1:8000/token/](http://127.0.0.1:8000/token/)
* You can refresh your token when it expires with a **POST** at [http://127.0.0.1:8000/token/refresh/](http://127.0.0.1:8000/token/refresh/) by providing your refresh tokens
* You must provide your access token in the headers of any request like this : **{Authorization: "Bearer YOUR_ACCESS_TOKEN"}** 
* Here is a list of some request you can make:
    - Create a project with a **POST** at [http://127.0.0.1:8000/projects/](http://127.0.0.1:8000/projects/)
    - Create an issue on a project with a **POST** at [http://127.0.0.1:8000/projects/<project_id>/issues/](http://127.0.0.1:8000/projects/<project_id>/issues/)
    - Read a list of all projects you contribute to with a **GET** at [http://127.0.0.1:8000/projects/](http://127.0.0.1:8000/projects/)
    - Update a project you are the author of with a **PATCH** at [http://127.0.0.1:8000/projects/<project_id>/](http://127.0.0.1:8000/projects/<project_id>/)
    - etc ...

# Important to know

* You can basically do all basic CRUD operations on any ressource in the app: **Users, Projects, Contributors, Issues, Comments**
* Any user can create a project, they automatically become the author and a contributor of this project.
* You need to be a contributor of a project to access it, or any ressource than references it (Issues, Contributors, Comments)
* Only the author of a ressource can update or delete it.