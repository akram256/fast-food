# Food fast
This is an application for online food delivery


Travis badge    [![Build Status](https://travis-ci.org/akram256/fast-food.svg?branch=API)](https://travis-ci.org/akram256/fast-food)

***Features***
 * User can fetch all orders.
 * User can fetch a specific order.
 * User can post an order. 
 * User can can update an order.
 
## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development
and testing purposes.

### Prerequisites
What you need to install the software and get started.

```bash
- git : to update and clone the repository
- python3: The base language used to develop the api
- pip: a python package used to install project requirements
```
### Installation
```bash
Type:
```
The UI folder houses the user interface. To access the user interface, open the index.html.

The api folder contains the system backend services.
- To install the requirements, run:
- [Python](https://www.python.org/) A general purpose programming language

- [Pip](https://pypi.org/project/pip/) A tool for installing python packages

- [Virtualenv](https://virtualenv.pypa.io/en/stable/)  A tool to create isolated Python environments

#### Development setup
- Create a virtual environment and activate it
    ```bash
     virtualenv venv
     source /venv/bin/activate
    ```
- Install dependencies 
    ```bash
    pip3 install -r requirements.txt
    ```
- Run the application
    ```bash
    cd Fast-food
    python run.py
    ```
- Now you can access the system api Endpoints:

| End Point                                           | Verb |Use                                       |
| ----------------------------------------------------|------|------------------------------------------|
|`/api/v1/orders/`                                    |GET   |Gets a list of all orders              |
|`/api/v1/orders/<int:order_id>/`                     |GET   |Gets a specific specific order  |
|`/api/v1/orders/`                                    |POST  |Posting an order                        |
|`/api/v1/orders/<int:order_id>/`                     |PUT   |Updates the status of an order      |

## Running the tests

- To run the tests, run the following commands

```bash
pytest --cov=api
```

## Built With

* [Flask](http://flask.pocoo.org/docs/1.0/) - The web framework used
* [Python](https://www.python.org/) - Framework language
* HTML
* CSS

## Authors

* **Mukasa  Akram** -  - [akram256](https://github.com/akram256)

## Acknowledgments

* Andela Development Uganda