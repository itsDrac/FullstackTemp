## Fullstack app template.
This is a template repo for fullstack app which uses React for frontend, Fastapi for backend and Postgres for database.

## How to run.

To run the project you need docker installed. with docker installed you'll need to clone this repo and run the command.

```
docker compose up -d
```

## How to run without docker.

To run without docker clone the repo then cd into server (You could make a vertual environment)

```
pip install -r requirements.txt
unicorn main:app
```

Now cd to client folder and run command

```
npm create vite@latest
npm install 
```

**Note**: Please add your own database url for without docker.
