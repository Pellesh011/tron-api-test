# Environment Setup

It is recommended to use a virtual environment to manage dependencies.

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment:

- On Linux/macOS:
  ```bash
  source venv/bin/activate
  ```
- On Windows:
  ```bash
  venv\Scripts\activate
  ```

# Install Dependencies

Install the required packages using pip:

```bash
pip install -r req.txt
```

# Running the Application

To run the application, execute:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```


# Running Tests

To run the tests, use:

```bash
pytest 
```