# Birthdayreminder

In the choir where I sing we have a list of all singers,
together with their birthdays. Sometimes we forget to
sing someone the birthday song.

In this little project I want to set up a small database
and have a restful access to the members and their birthdays.

## REST

/members/   List of all members with birthdays, sort by first name
/birthdays  List of all members with birthdays, sort by date
/birthdays/last?count=12    List of 12 birthdays, from now back in time

## Requirements

1. Get a list of all members sort by first or surname.
2. Get a list of all members sort by birthday, starting jan 1st.
3. Get a list of all members having birthday between now and 2 weeks ago
4. Add a member with birthday
5. Update / correct member or birthday

## Notes

### flask

After creating the flask-install there was this message:

```ou can run Flask's local server by executing the manager script:
./manage.py runserver

For safety's sake, this defaults to a production config with DEBUG turned off.
You can change the config by setting the APP_CONFIG
environment variable to "development" in your shell:
export APP_CONFIG=development

```

#### Flask extensions being used

* flask-wtf: Flask-WTF is for web forms
* flask-sqlalchemy: a SQL ORM for different SQL databases (MySQL, SQLite, PostgreSQL...)
* flask-migrate: Wrapper for [Alembic](https://bitbucket.org/zzzeek/alembic), a
  database migration framework for SQLAlchemy.

### flask security

With WTForms we use the `{{ form.hidden_tag() }}` in the template to include
some CSRF forgery. Using this together with a `SECRET_KEY` defined for the 
Flask configuration is enough for this.

