# Quick Development commands

## Quick reset and start

With the database already created and PostgreSQL running:
```bash
python -m reset_and_seed_database && python -m uvicorn main:app --reload
```
**Warning:** resetting deletes the existing application tables and their data.

Open the [interactive API documentation](http://127.0.0.1:8000/docs).

Alternatively, run this in a separate WSL terminal to open it in your Windows browser:
```bash
explorer.exe "http://127.0.0.1:8000/docs"
```

Press `Ctrl+C` in the server terminal to stop the server.

## 1. Create the database

Creates the PostgreSQL database itself.

### Start PostgreSQL

If PostgreSQL is installed locally in Ubuntu/WSL, start it before running database commands:
```bash
sudo service postgresql start
```

Check that it is accepting connections:
```bash
pg_isready
```

If PostgreSQL is already running, there is no need to start it again.

### Initial setup — run once
```bash
psql -d postgres -f db/create_database.sql
```

`psql` does not load your `.env.development` file. Add PostgreSQL role or host options if required by your setup.

## 2. Seed the tables

Drops the existing application tables, recreates them and inserts the initial JSON data. The database itself stays in place.

### Reseed the tables
```bash
python -m reset_and_seed_database
```

When using `python -m`, omit `.py`.

**Warning:** this deletes existing table data. Check that your connection settings select the intended development or test database before running it.

## 3. Start the server
```bash
python -m uvicorn main:app --reload
```
- `main:app` loads the `app` object from `main.py`; omit `.py`.
- `--reload` automatically restarts the development server when Python files change.

Open:
- [API base URL](http://127.0.0.1:8000)
- [Interactive API documentation](http://127.0.0.1:8000/docs)

The base URL may return `404` if no route is defined at `/`.

Press `Ctrl+C` in the terminal to stop the server.

Starting the server does not reset or seed the database unless your application explicitly calls that code. PostgreSQL must remain running for database-backed requests.

## Other quick commands

### Save the project folder and file tree

With `tree` installed:
```bash
tree -a -I '.venv|.git|__pycache__' > structure.txt
```

This includes hidden files, excludes the listed folders and saves the layout to `structure.txt`, replacing its existing contents.

### Example POST request using curl

With the server running:
```bash
curl -X POST \
  'http://127.0.0.1:8000/users/' \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "username": "Suleyman Rasul",
    "email": "chacna@example.com",
    "user_password": "user_password123"
  }' | python -m json.tool
```
- The JSON fields must match your request model; your shared code uses `user_password`.
- `Content-Type: application/json` identifies the request body as JSON.
- `python -m json.tool` formats the JSON response for readability.
- Use a different email for another successful creation because user emails must be unique.