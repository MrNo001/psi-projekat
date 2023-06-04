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


## Structure

search
- '' (home)
- 'pretraga' [+queryParams]

account
- 'login'
- 'registracija'
- 'profil'
	- 'uredi'
	- mojiOglasi
	- praceniOglasi

offer
- 'oglas'
	- id / 'izmeni'
	- id / 'ukloni'
	- 'napravi'
	- [f] pracenje oglasa

conversation
- 'profil/poruke'
	- 'sve'
	- 'razgovor' [+queryParams]

moderator
- 'panel'
- [f] prijavljivanje oglasa


## Non-python dependencies

- Tailwind ([quickstart](https://tailwindcss.com/docs/installation/play-cdn))
- Flowbite ([quickstart](https://flowbite.com/docs/getting-started/quickstart/))
