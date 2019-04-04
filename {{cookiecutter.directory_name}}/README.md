# README #

#### [pipenv](https://docs.pipenv.org/)
pipenv is using for virtual environment.

Setup pipenv 
```commandline
pip install --user pipenv
```
Enable virtual environment
```commandline
pipenv shell
```
Install project dependencies
```commandline
pipenv install
```

Install specific package 
```commandline
pipenv install package_name=='version'
```

#### Configuration Environment Variables
```commandline
cp .env.sample .env
```
Enter respective values for environment variables

#### Start Application in Development
```commandline
flask run
```

#### Run Test
Execute test suite
```commandline
pytest -s
```
Execute particular test(s)
```commandline
pytest -s tests/test_name.py
pytest -s tests/test_name.py::test_func
pytest -s tests/test_name.py::TestClass::test_method
```

#### Test coverage
Run test coverage 
```commandline
coverage run -m pytest
```

Run test report
```commandline
coverage html
```

### Using celery for background tasks
start worker
```commandline
celery -A celery_worker:fpd_celery worker --loglevel=INFO
celery -A celery_worker:fpd_celery worker -Q queue1 --loglevel=INFO
celery -A celery_worker:fpd_celery worker -Q queue1 --loglevel=INFO 
```
start scheduler 
```commandline
celery -A celery_worker:fpd_celery beat --loglevel=INFO
```
###  Deployment instructions

Setups for deployments

Created AWS Code Build Projects for building docker images

### Contribution guidelines ###

* Coding guidelines
* Code review 
* Other guidelines

### TODO

- Improve mongo db errors in API response
- Need use secure mongo db connection URI
- Improve logging with request url, request ip and params 
- Setup mailer
- [Celery](http://docs.celeryproject.org/en/latest/index.html) for background/queueing jobs
    + Logger for background jobs
    + Improve celery configuration
    + Implement concurrency for different tasks and different queues for different tasks    
- Setup sample webhook 
- Improve test configuring and Setup for different environments
- Improve api authentication
