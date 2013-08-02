ChaosCowboy
===========


## Getting started - Developer Edition
- Create a virtual environment

```shell
virtualenv .venv_chaos
```
- Change directory into the virtual environment folder

```shell
cd .venv_chaos
```
- Activate virtual environment

```shell
source bin/activate
```
- Clone the repository

```shell
git clone git@github.com:ChaosCowboy/ChaosCowboy.git
```
- Change directory into cloned project

```shell
cd ChaosCowboy
```
- Install pip package dependancies

```shell
pip install -r pip-requires
```
- Sync Django db

```shell
python manage.py syncdb
```
- Run Django development server

```shell
python manage.py runserver
```
