# Webb23 alm final project

## Objective
In this assignment, you will containerize a Django application, deploy it using Kubernetes (Minikube), and set up GitHub Actions to automate testing. 

### Step 1: Fork the repository (Group)

### Step 2: Set up Docker
1. Create a docker file
    - Use a python base image
    - Run this command to install all python package 
        ```shell
        pip install -r requirements.txt 
        ```
    - The command for running the Django server
        ```shell
        python blog_project/manage.py runserver 0.0.0.0:8000
        ```
2. Build you docker image

3. Create a Docker container 

### Step 3: Set up Kubernetes (Minikube) (Group)
1. Create a kubernetes deployment yaml file, that uses the Docker image from step 2
    - remember to export port 8000

2. Crete a kubernetes service yaml file

3. Apply the kubernetes development and servics configuration


### Step 4: Set up Github Action (Group)
1. Create a Github Action workflow for testing
    - The workflow should only work when creating a pull request to the main branch
    - Use a postgres db service with these enviroment variables
    ```yaml
    POSTGRES_USER: postgres
    POSTGRES_PASSWORD: postgres
    POSTGRES_DB: django_db
    ```
    - Remember to use pip to install all package
    ```yaml
    pip install -r requirements.txt 
    ```
    - The last step to run the test you need to run two commands
    ```yaml
    run: |
        python blog_project/manage.py migrate
        python blog_project/manage.py test
    ```

2. Create pull request


### Step 5: Create docker compose (Individual)
1. Create docker compose yaml configuration
    - Add db service
        - db should use an postgres image
        - Add this environment variable to the Db service
        ```yaml
        POSTGRES_USER: postgres
        POSTGRES_PASSWORD: postgres
        POSTGRES_DB: django_db
        ```
        - Add a volume that the db service can use
            - with this /var/lib/postgresql/data
    -  Add web service
        - Use local docker image
        - the command to run the django server
            ```yaml
            python blog_project/manage.py runserver 0.0.0.0:8000
            ```
        - Dont forget to expose container port 8000
        - It should depend on db service
        
2. Build and start container
    - When its running run this command in a seperate terminal
    ```shell
    docker-compose exec web python blog_project/manage.py migrate
    ```
    - Create django admin user
    ```shell
    docker-compose exec web python blog_project/manage.py createsuperuser
    ```
    - try to login
    ```shell
    http://localhost:8000/admin/
    ```
## **REMEMBER TO REMOVE FROM .gitignore**
 - docker-compose.yml line 1
 - Dockerfile line 2
