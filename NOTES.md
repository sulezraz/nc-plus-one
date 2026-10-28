# Quick reset and start
1. **Reset and seed the tables:**
2. **After the reset succeeds, start the server:**
3. **Open the interactive API documentation:**

Press **Ctrl+C** to stop the server.

From the project root, with your virtual environment activated:
Run:
   ```bash
   python -m reset_and_seed_database
   python -m uvicorn main:app --reload
   ```

Press Ctrl + Shift + T to open New Terminal and then run
   ```bash
   explorer.exe "http://127.0.0.1:8000/docs"
   ```



---


## 1. Create the database

**Description:** This creates the database itself

### Initial setup — run once
From the project root, run:
```bash
psql -f db/create_database.sql
```
**Warning:** this script deletes and recreates the database if it already exists.


## 2. Seed the tables

**Description:** Drops the existing tables, recreates them and inserts the initial JSON data. The database itself stays in place, so you do not need to recreate it.

### Reseed the tables

From the project root, with your virtual environment activated, run:
```bash
python -m reset_and_seed_database.py
```

**Warning:** This deletes existing table data. Check that your connection settings select the intended development or test database before running it.


## 3. Start the server

From the project root, with your virtual environment activated, run:
```bash
python -m uvicorn main:app --reload
```
- `main:app` loads the `app` object from `main.py` — omit `.py`.
- `--reload` automatically restarts the server when Python files change.

Open:
- **API:** [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Interactive API documentation:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Press **Ctrl+C** in the terminal to stop the server.
Starting the server does not reset or seed the database unless your application explicitly calls that code.


---


## Other Notes

### Print out project folder/file tree
```bash
   tree -a -I '.venv|.git|__pycache__' > structure.txt
```