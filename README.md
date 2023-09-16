# Spend Tracker
This is Spend Tracker API Service written using Django Rest Framework

## Installation
To set up and run this project follow next steps.

Python must be installed

### Clone the repository
```python
https://github.com/kovaliskoveronika/spend_tracker.git
```

### Create .env file and define variables following .env.sample

### Built Docker container
```python
docker-compose build
```

### Access list of containers
```python
docker ps -a
```

### Create a superuser
```python
docker exec -it <container_id here> python manage.py createsuperuser
```

### Start the Docker container
```python
docker-compose up
```

### To stop the container
```python
docker-compose down
```
or you can use combination Ctr+C

## Endpoints
```python
          "revenue-statistic": "http://localhost:8000/revenue/revenue-statistic/",
          "spend-statistic": "http://localhost:8000/spend/spend-statistic/",
          "doc": "http://localhost:8000/doc/",
          "doc/swagger/": "http://localhost:8000/doc/swagger/"
```