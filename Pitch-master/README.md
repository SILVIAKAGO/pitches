# Pitch

##A web application that allows the users to post pitches, comment and vote on pitches.

## By [SILVIAKAGO](https://github.com/)


## Description
This is a web application that allows various users to submit a short pitch. Users can also be able to view other pitches from different categories (Pick-up Lines, Interview Pitches, Product Pitches, Promotion Pitches), comment and vote. For a user to do any of that, they need to have registered.

## User Stories
* As a user I would like to view the different categories.
* As a user I would like to see the pitches other people have posted.
* As a user I would like to comment on the different pitches and leave feedback.
* As a user I would like to submit a pitch in any category.
* As a user I would like to vote on the pitch they liked and give it a downvote or upvote.

## Specifications
| Behaviour | Input | Output |
| --------------- | :----------:| --------: |
|Display Various Pitch Categories | N/A | Various pitches grouped by category are displayed |
|Display pitches | **Click** on a Category| A page with a list of pitches from the selected category |
|Add new pitch | **Click** New pitch | User Should register/sign in to add new pitch |
|View Pitches | **Click** on a pitch | View a pitch and comments |
|Comment on a pitch | **Click** Comment | Registered User displays a form where a user can comment on a certain pitch |
<!-- |Upvote a pitch | **Click** glyphicon upvote | Vote for a specific pitch increases |
|Downvote a pitch | **Click** glyphicon downvote | Vote for a specific pitch decreases | -->

## Prerequisites
* Python3.8

## Setup/Installation Requirements
* internet access
* $ git clone https://github.com/SILVIAKAGO/Pitch
* $ cd Pitch
* $ python3.8 -m venv virtual (install virtual environment)
* $ source virtual/bin/activate
* $ python3.8 -m pip install -r requirements.txt (install all dependencies)
* Inside the manage.py module change the config_name parameter from 'production' to 'development' ie app = create_app('production') should be app = create_app('development')
* $ ./start.sh


# How it works

* A user needs to sign up
* A user the needs to sign in to vote and post pitches

# CREDITS

#### Google.com, StackOverflow.com and Miguel Grinberg -author of 'Flask Web Development, 2nd Edition'


# Support and Contacts

In case You have any issues using this code please do no hesitate to get in touch with me through maratah7@gmail.com or leave a commit here on github.


## Known Bugs
No known bugs.

## Technologies Used
- Python3.8
- Flask framework
- Bootstrap
- PostgreSQL

### License

**[KAY](./LICENSE)** (c) 2020 **[SILVIAKAGO](https://SILVIAKAGO.github.io/Portfolio-LP/)**
