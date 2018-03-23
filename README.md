## Python automation Framework

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
git clone git@github.com:egovernments/egov-qa.git .
```

Now run 

```bash
pip install -r requirements.txt
```

### Running the tests

The test can be run using below command

```bash
python -m pytest tests 
```