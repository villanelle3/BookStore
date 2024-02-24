## Prerequisites

```
Python 3.5>
Poetry
Docker && docker-compose

```

## Quickstart

1.  dependencies:

   ```shell
   cd bookstore
   poetry install
   ```

2. Run local dev server:

   ```shell
   poetry run manage.py migrate
   poetry run python manage.py runserver
   ```

3. Run docker dev server environment:

   ```shell
   docker-compose up -d --build
   docker-compose exec web python manage.py migrate
   ```

4. Run tests inside of docker:

   ```shell
   docker-compose exec web python manage.py test
   ```