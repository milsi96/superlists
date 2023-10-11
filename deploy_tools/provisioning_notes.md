# Provisioning a new site
=========================

## Required packages:

* nginx
* Python 3.11
* virtualenv + pip
* Git

e.g., on Ubuntu:

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install nginx git python311 python3.11-venv
```

## Nginx Virtual Host config

* see `nginx.template.conf`
* replace `DOMAIN` with *your domain*, e.g., superlists-staging.it

## Folder structure:

Assume we have a user account at /home/username

/home/elspeth
└── sites
    └── DOMAIN1
        ├── .env
        ├── db.sqlite3
        ├── manage.py etc
        ├── static
        └── virtualenv
    └── DOMAIN2
        ├── .env
        ├── db.sqlite3
        ├── manage.py etc
        ├── static
        └── virtualenv
