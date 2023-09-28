## Run local

### Install dependencies

```
pip install -r requirements.txt
```

### Run server

```
uvicorn app.main:app --reload
```

### Run test

```
pytest app/test.py
```

## Run with docker

### Run server

```
docker-compose up -d --build
```

## API documentation (provided by Swagger UI)

```
http://localhost:8000/docs
```

### Run server

```
docker-compose exec db psql --username=fastapi --dbname=fastapi_dev
```


In a typical FastAPI application using SQLAlchemy, you would create the database and tables using Alembic migrations. Here’s a step-by-step process to set up Alembic and create your initial migration:

### 1. Install Alembic:

Make sure Alembic is included in your `requirements.txt`:

```plaintext
alembic==1.7.3
```

Then, install the dependencies:

```sh
pip install -r requirements.txt
```

### 2. Initialize Alembic:

Navigate to your project directory and run:

```sh
alembic init alembic
```

This command will create an `alembic` directory in your project containing the Alembic configuration.

### 3. Configure Alembic:

Edit the `alembic.ini` file created by the initialization command. Find the line starting with `sqlalchemy.url` and set it to your `DATABASE_URL`:

```ini
sqlalchemy.url = postgresql://postgres:postgres@db/postgres
```

Also, update the `env.py` file inside the `alembic` directory to make Alembic aware of your models and metadata. Import your `Base` and `engine` from `database.py`:

```python
# alembic/env.py
from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

# Import your Base and engine here
from app.database import Base, engine
from app.models.item import Item 

# ...
```

And find the section where the `target_metadata` is set, and update it:

```python
target_metadata = Base.metadata
```

### 4. Create Migration:

After configuring Alembic, run the following command to create an initial migration:

```sh
alembic revision --autogenerate -m "Initial migration"
```

### 5. Run Migrations:

Apply the migration to create the database and tables:

```sh
alembic upgrade head
```

Now, your PostgreSQL database and the `items` table should be created.

### 6. Check Database:

You can connect to your PostgreSQL instance and check if the database and table have been created successfully.

```sh
docker exec -it db psql -U postgres -d postgres
```

In the PostgreSQL prompt, check the tables:

```sql
\dt
```

You should see your `items` table listed.

### Note:

If your application and PostgreSQL are running inside Docker containers, make sure both containers are running, and they are in the same network. If using Docker Compose, they should be defined in the same `docker-compose.yml` file.

Keep in mind that database migrations are a way to version the changes in your database schema and share them with other developers. They are essential for managing the database schema in production and during development when working with teams.