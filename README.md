# HackIllinois-PlayingCards
A card simulator, meant to be played while communicating over applications like Zoom and Discord. It is about rekindling connections, whether due to Covid, or moving away from home to study. We found it difficult to find online versions of certain card games, so we decided to just implement a single interface, while the rules etc. can be provided by the players themselves, freeing them from any restrictions.

## Git

### Branching and Committing
1. `git checkout -b feature_branch_name`
2. `git push -u origin feature_branch_name`

## Frontend (cards)

### To Start the Server
1. `cd cards/`
2. `npm install`
3. `npm start`

## Backend (backend)

### To Start the Server
1. Create a virtual environment (https://docs.python.org/3/library/venv.html)
2. `source ./path/to/venv/bin/activate` (or `./path/to/venv/Scripts/active` for Win)
3. `pip install -r requirements.txt`
4. `uwsgi dev.ini`

P.S. Code is mighty dirty.
