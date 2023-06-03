# Polovna vozila - PSI projekat

Projakt za predmet Principi softverskog inzinjerstva

Tim Inpira Grupa

## Commands

setup
- prereqs: python (python3, py), pip (pip3) - virtualenv maybe
- install: `pip install -r requirements.txt`
- check: `python -m django --version`


django
- run server: `python manage.py runserver`
- create new app: `python manage.py startapp <name>`


## Struktura

search
- '' (home)
- 'pretraga' [+queryParams]

account
- 'login'
- 'registracija'
- 'profil'
	- 'izmeni'
	- 'mojiOglasi'
	- 'praceniOglasi'
	- 'poruke'

offer
- 'oglas' [+id]
	- 'izmeni'
	- [f] pracenje oglasa
- 'napravi'

conversation
- 'profil/poruke'
	- 'sve'
	- 'razgovor' [+queryParams]

moderator
- 'panel'
- [f] prijavljivanje oglasa

