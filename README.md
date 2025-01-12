
## About Me
Hi, I'm Viktor and this is my first project!


# Project Title

This is a project that demonstrates the basic principles of test automation. The project implements automated tests of API and various sites, such as GitHub, NovaPoshta. It contains examples of Python tests using `pytest` and `selenium`

## Requirements

- Python 3.7+
- `pytest`
- `selenium`
- `webdriver-manager`
- `requests`

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Viktor151274/viktorQAmanager.git
    cd viktorQAmanager
    ```
2. Install the required packages:
    ```sh
    pip install pytest
    pip install selenium
    pip install webdriver-manager
    pip install requests
    ```

## Running Tests

To run all tests:
   
```sh
pytest
```

## Run specific tests by marker:
   - For API-related tests:
     ```bash
     pytest -m api
     ```
   - For UI automation tests:
     ```bash
     pytest -m ui
     ```
   - For database tests:
     ```bash
     pytest -m database
     ```

## License

[MIT](https://choosealicense.com/licenses/mit/)