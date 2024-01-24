## DESCRIPTION
    1. Download YouTube Videos in 3 steps
    2. Created using django
## Features

- Copy and paste link of YouTube video in the search bar to download it
- You can download the video in mp4 format
- You can also download only the audio from video in mp3 format

## Disadvantage

- Currently only single videos can be downloaded 
- Downloading playlists is not supported currently



## Tech Stack

**Client Side:** HTML, SCSS, TailwindCSS

**Server Side:** Django


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`DEBUG = TRUE`

`SECRET_KEY = 'django-insecure-(s6m9uk96%uj)k=x9t$^1ruk*g#ou4014&*r#qm#e2d&9m6d%d'`
## Installation

Create a folder and open terminal and install this project by
command 
```bash
git clone https://github.com/Mr-Atanu-Roy/myDownloader

```
or simply download this project from https://github.com/Mr-Atanu-Roy/myDownloader

In project directory Create a virtual environment(say env)

```bash
  virtualenv env

```
Activate the virtual environment

For windows:
```bash
  env\Script\activate

```
Install dependencies
```bash
  pip install -r requirements.txt

```
To migrate the database run migrations commands (not necessary for this project)
```bash
  py manage.py magemigrations
  py manage.py migrate

```

Create a super user (not necessary for this project)
```bash
  py manage.py createsuperuser

```

To run the project in your localserver
```bash
  py manage.py runserver

```
Then go to http://127.0.0.1:8000 in your browser to see the project

## Author

- [@Mr-Atanu-Roy](https://www.github.com/Mr-Atanu-Roy)

