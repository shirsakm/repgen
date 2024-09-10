# Repgen

> [!NOTE]
> This software was developed at HackHeritage 2024.

A financial and academic anaylysis and prediction tool for academic institutions. _Repgen_ aids academic institutions in making the correct choices, by visualising and predicting future reports based on existing data. It aims to revolutionize the game for institutions, by eliminating the hassle of piecing puzzle pieces of software into one coherent structure. _Repgen_ is not just a software, it is an _experience_.

## Features

- [x] An intuitive, user-friendly interface
- [x] End-to-end data encryption
- [x] AI-based financial data analysis
- [ ] AI-based academic analysis

## How to Contribute

### Setting up

1. Clone the repository.

    ```sh
    $ git clone https://github.com/shirsakm/repgen
    $ cd ./repgen
    ```

2. Optionally, create and activate a virtual environment.

    ```sh
    $ python -m venv .venv
    $ source ./.venv/bin/activate
    ```

3. Install prerequisite modules.

    ```sh
    $ python -m pip install -r requirements.txt
    ```

### Contributing

#### Frontend

For contributing to the frontend, all required files can be found in the `static/` and `templates/` directory. The HTML files for _jinja2_ templating, can be found in the `templates/` directory, while the `static/` directory contains the CSS styling and the associated JavaScript files. It also contains assets, such as fonts and images.

#### Backend

For contributing to the backend, all required files can be found in the `routes/` directory. The `repgen.py` is the backbone of the app, and should be not touched unless absolutely required. All features should be attempted to be implemented via _jinja2_ blueprint registration only. Note that, if you create a new `.py` file in the `routes/` directory, please introduce the following line of code to `__init__.py` in the `routes/` directory.

```py
...
# Here, name is the filename of the .py file you created
from .name import * 
```

### Testing

For testing your code, you can either use _gunicorn_ to run the `.wsgi` file, or use _Flask_ directly. I recommend using _gunicorn_ for testing before submitting a _Pull Request_, as the `master` branch deploys directly to production. For debugging, use _Flask_ to deploy and test.

1. For _gunicorn_,

    ```sh
    $ gunicorn repgen:app
    ```
    For _Flask_ execute,

    ```sh
    $ flask --app repgen run
    ```

    For _debugging_ with hot reload,

    ```sh
    $ flask --app repgen run --debug
    ```

2. Visit `localhost:port/` on your browser, where `port` is the port being listened at. For _gunicorn_, the port opened is likely to be `8000`, and for _Flask_ the port opened is likely to be `5000`. However, if you are unable to locate the correct port, check the output for an URL resembling, `http://127.0.0.1:port/`, which will be the URL the website is being served at.
