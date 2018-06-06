## Python Selenium automation Framework

This project contains automated functional tests for different egov modules. The tech stack used for the project are:
1. **Pytest** as testing framework for writing test scenarios
2. **Python** as the programming language for writing test code
3. **Selenium** to drive browser interaction
4. **PyCharm** as the preferred IDE for writing python code

### Setup

#### Installing Python3 
First make sure `Python 3.X` is installed on the system

**Unix**

```bash
apt install -y python3-pip 
```

**Mac**

```bash
brew install python
```

**Windows**

Download latest version of Python 3 from below link

https://www.python.org/downloads/

#### Installing virtualenvwrapper

Setup `virtualenvwrapper` using steps mentioned in https://virtualenvwrapper.readthedocs.io/en/latest/install.html

#### Create virtual env

```bash
mkproject rainmaker_automation
```

Once inside the project do 

```bash
git clone git@github.com:egovernments/egov-qa.git
```

Now run 

```bash
pip install -r requirements.txt
```

### Structure of Project

```
egov-qa/
├── assets
│   └── images
├── environment
│   └── common.py
│   └── dev.py
├── framework
│   └── common.py
│   └── selenium_plus.py
├── pages
│   └── component
└── tests
    └── test.py
    └── test_add_complaints.py
```

### Writing Test Case

* In the *tests/* directory create a python file with naming convention like,
> example: "test_add_complaints.py"
* Tests are written and pytest used for running, for this test methods naming convention has to follow like:
> "test_login()" or "login_test()"
* **Page**, and **Component** classes gives a layer for test cases to run
* Page object design pattern provides separation between test code and technique implementation.
* In **Page** classes is encapsulated with web-elements (variables) and methods (actions), these methods will call by the test cases. And each page classes should be tag with page object annotation like ***@PageObject*** this will create object for each web pages.


### Running the tests

The test can be run using PyCharm IDE:

1. Can run test from PyCharm, by right clicking and Run feature file. set the configurations for python-pytest, and environment before trying to run the tests as pytest for running. This will run the tests using chrome browser and against the environment.
2. You can get your test Report using pytest

The test can also be run using command-line either module wise or directory wise:

Running module wise test cases:
```bash
python -m pytest test_add_complaints.py 
```
Running directory wise test cases:
```bash
python -m pytest tests
```