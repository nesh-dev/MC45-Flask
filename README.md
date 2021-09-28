
### Installation and Setup 
- Clone the repo 

    `git clone https://github.com/nesh-dev/MC45-Flask.git`

- Switch the develop branch 

    `git fetch origin main`

- Navigate to the folder 

    `cd watchlist`

- create a virual env 

    `python 3 -m venv venv`

- Activate the venv 

    `source/venv/activate`

- Install the required packages 

    `pip install -r requirements.txt`

- Created db on Postgresql 

    `CREATE DATABASE watchlist`

- Run migrations 

    `python manage.py db migrate`

- Run server 
    `python manage.py runserver`

- Run configurations 
  configurations for the app are contained in the sample.env you can copy and paste the structure  and add it to a .env file

   `$ cp sample.env .env`


- navigate back to root and run python run.py


- use postman to test the endpoints



|Endpoint           |   Method   | description                               |
|  ------------     | ---------- |  ----------------------------------       |
|/api/v1/register   |   POST     | add  a new user                           |
|                   |            |                                           |
|/api/v1/login      |   POST     |User Login token                           |
|                   |            |                                           |
|/api/v1/movies     |   POST     |create new movie resource auth required    |
|                   |            |                                           |
|                   |            |                                           | 
|/api/v1/movie/id   |   GET      | User logout                               |

