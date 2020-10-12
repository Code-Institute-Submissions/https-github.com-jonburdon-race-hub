[insert logo image here]

# Rachub


## [Deployed Project on Heroku](https://race-hub.herokuapp.com/)

[Developer Aims](#developer-aims) | [UX](#ux) | [User Stories and Corresponding Features](#user-stories-and-features) | [UI Structure](#ui-structure) | [Visual Layout](#visual-layout) | [Technologies Used](#technologies-used) | [Information Architecture](#information-architecture) | [Deployment](#deployment) | [Local Development](#local-development) | [Testing](#testing) | [Acknowledgements](#acknowledgements)

Racehub is race entry and results management system for amateur athletes and event organisers. It is written in python using the django framework and is the final project in the Code Institute Diploma in Software Development (Full Stack Web Development.)


## [Developer Aims](#developer-aims)
[Developer Aims](#developer-aims) | [UX](#ux) | [User Stories and Corresponding Features](#user-stories-and-features) | [UI Structure](#ui-structure) | [Visual Layout](#visual-layout) | [Technologies Used](#technologies-used) | [Information Architecture](#information-architecture) | [Deployment](#deployment) | [Local Development](#local-development) | [Testing](#testing) | [Acknowledgements](#acknowledgements)

* Use the django framework for writing a fully functioning web application
* Provide sufficient user interaction features to demonstrate that this project could be further developed into a viable commercial application
* Provide sufficient documentation in order that the project can be maintained and further developed in the future

## [UX](#ux)
[Developer Aims](#developer-aims) | [UX](#ux) | [User Stories and Corresponding Features](#user-stories-and-features) | [UI Structure](#ui-structure) | [Visual Layout](#visual-layout) | [Technologies Used](#technologies-used) | [Information Architecture](#information-architecture) | [Deployment](#deployment) | [Local Development](#local-development) | [Testing](#testing) | [Acknowledgements](#acknowledgements)

## [User Stories and Corresponding Features](#user-stories-and-features)
[Developer Aims](#developer-aims) | [UX](#ux) | [User Stories and Corresponding Features](#user-stories-and-features) | [UI Structure](#ui-structure) | [Visual Layout](#visual-layout) | [Technologies Used](#technologies-used) | [Information Architecture](#information-architecture) | [Deployment](#deployment) | [Local Development](#local-development) | [Testing](#testing) | [Acknowledgements](#acknowledgements)

| User Story ID | As a / an | I want to be able to... | ... so that I can | Existing Features | Suggested future features |
|---|---|---|---|---|---|
|  Viewing and Navigation  |
| 1a | Visitor | View a list of events | select one to enter | List view with search and filters, , Filter by distance, discipline, Sort by distance, date, price | Add filters to map view  |
| 1b |  | View race results | find performances | Find results by name, sort by date or name | Add further filtering controls |
| 1c |  | Quickly identify an event in my area and discipline | enter an event that suits my preferences | Map view | Add filters to map view |
| 1d |  | Add a whole series or championship to my cart at once.  |  |  | 
| 1e |  | Easily enter my friends who are / are not registered on this site.  | 'Family and Friends' can be added and entered for events. Registered users can be added as 'Racehub Friends' | Send a friends request to other site users, search athlete feature. | 
| Registration and User Accounts  | 
| 2a | Registered Athlete | Easily register for an account | Account creation automatically creates athlete profile | Popup 'tour' guides user through the process. | 
| 2b |  | Log in and out simply with social media account specifically facebook |  |  | 
| 2c |  | Recover my password | Authentication added |  | 
| 2e |  | Receive email confirmation after registering | Email confirmation added |  | 
| 2f |  | View a personalised user profile |  |  | 
| 2g |  | Cancel entry |  transfer my entry to another user |  swap my entry to another event from same organiser." | Entry can be transferred to other users by changing ID | Verification that all details have genuinely been changed when a registration is transferred. | 
|  |  | Sorting and Searching |  |  | 
| 3a |  | Sort the list of events | Easily identify events by date, discipline, distance |  | 
| 3b |  | Filter to find only events in a specific category | date, disciple |  | 
| 3c |  | Sort multiple properties of events simultaneously | Eg find a 10k road event or set of results in Yorkshire | After filtering by discipline, sorting features can can used find by distance | Add colours and icons to make different categories of events stand out |
| 3d |  | Search for results. | Search for results by athlete name, club or age category |  | 
| 3e |  | Easily enter an event |  |  | 
| 3f |  | Easily edit my own Athlete details | Athlete profile can be edited |  | 
| 3g |  | Enter multiple athletes for one event at the same time |  and pay for their entry all at once. | Self, friends or family can all be added to the same basket |  | 
| 3h |  |  |  |  | 
| 3i |  |  |  |  | 
| 3j |  | Add results for virtual races I am registered for | Result can be submitted as photo or hyperlink |  | 

|Admin and management  | 
| 4a | Club or organisation official | Manage teams | my club has it's own private page |  |  |
| 4b |  | Make my club events private  | they are not on the main listing pages |  |  | 
| 4c |  |  |  |  | 
| 4d | Event Organiser | Add events |  |  | 
| 4e |  | Add results by bulk upload |  |  | 
| 4f |  | Download results in bulk | Results can be exported to email account from Organiser Profile | Select one specific result set for download | 
| 4g |  | Add individual results 'live' at the finish line. | Single results can be added | Quick input form so that results are easier to add | 


## [UI Structure](#ui-structure)
[Developer Aims](#developer-aims) | [UX](#ux) | [User Stories and Corresponding Features](#user-stories-and-features) | [UI Structure](#ui-structure) | [Visual Layout](#visual-layout) | [Technologies Used](#technologies-used) | [Information Architecture](#information-architecture) | [Deployment](#deployment) | [Local Development](#local-development) | [Testing](#testing) | [Acknowledgements](#acknowledgements)

## [Visual Layout](#visual-layout)
[Developer Aims](#developer-aims) | [UX](#ux) | [User Stories and Corresponding Features](#user-stories-and-features) | [UI Structure](#ui-structure) | [Visual Layout](#visual-layout) | [Technologies Used](#technologies-used) | [Information Architecture](#information-architecture) | [Deployment](#deployment) | [Local Development](#local-development) | [Testing](#testing) | [Acknowledgements](#acknowledgements)

## [Technologies Used](#technologies-used)
[Developer Aims](#developer-aims) | [UX](#ux) | [User Stories and Corresponding Features](#user-stories-and-features) | [UI Structure](#ui-structure) | [Visual Layout](#visual-layout) | [Technologies Used](#technologies-used) | [Information Architecture](#information-architecture) | [Deployment](#deployment) | [Local Development](#local-development) | [Testing](#testing) | [Acknowledgements](#acknowledgements)

#### Languages:
* HTML for page structure and contents
* CSS for styling the content
* Javascript for DOM manipulation and stripe payment processing
* Python3 for application logic

#### Framework:
* Django (v3.1.1) for application backend, development database provision (SQLite3), routing and template manipulation;

#### Libraries:
* [Bootstrap](https://getbootstrap.com/) used for grid layout and front end ui components.
* [jQuery](https://jquery.com/) to easier DOM manipulation
* [Google Fonts](https://fonts.google.com/)
* [Font Awesome](https://fontawesome.com/) for icons

#### Development:
* [Gitpod](https://www.gitpod.io/) Used for ide
* [Github](https://github.com/) Used for version control

#### Code Validation Tools:
* [W3C Markup Validation Service](https://validator.w3.org/) was used to validate HTML and CSS code;
* [JSHint](https://jshint.com/) was used to validate JavaScript code;
* [PEP8 online](http://pep8online.com/) to validate Python code;

#### Deployment:
* [Amazon Web Services](https://aws.amazon.com/free/) S3 used for image Hosting
* [Heroku](https://dashboard.heroku.com/apps) used for application online deployment and production database provision (PostgresSQL)

#### External (third party) services:
* [Gmail](https://www.google.com/intl/en_uk/gmail/about/) for sending email
* [Stripe](https://dashboard.stripe.com/) for credit card payment processing

## [Information Architecture](#information-architecture)
[Developer Aims](#developer-aims) | [UX](#ux) | [User Stories and Corresponding Features](#user-stories-and-features) | [UI Structure](#ui-structure) | [Visual Layout](#visual-layout) | [Technologies Used](#technologies-used) | [Information Architecture](#information-architecture) | [Deployment](#deployment) | [Local Development](#local-development) | [Testing](#testing) | [Acknowledgements](#acknowledgements)


### Data Models

#### The User Model
The standard Django user model, `django.contrib.auth.models` was used for this project.

#### Cart app

**Order Model:**
| Key in db | Field Type | Validation |
|---|---|---|
| order_number | CharField | max_length=32, null=False, editable=False | 
| user_profile | ForeignKey | UserProfile, on_delete=models.SET_NULL, null=True blank=True, related_name='orders' | 
| full_name | CharField | max_length=50, null=False, blank=False | 
| email | EmailField | max_length=254, null=False, blank=False | 
| phone_number | CharField | max_length=20, null=False, blank=False | 
| country = CountryField | blank_label='Country *', null=False, blank=False | 
| postcode | CharField | max_length=20, null=True, blank=True | 
| town_or_city | CharField | max_length=40, null=False, blank=False | 
| street_address1 | CharField | max_length=80, null=False, blank=False | 
| street_address2 | CharField | max_length=80, null=True, blank=True | 
| county | CharField | max_length=80, null=True, blank=True | 
| date | DateTimeField | auto_now_add=True | 
| delivery_cost | DecimalField | max_digits=6, decimal_places=2, null=False, default=0 | 
| order_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0 | 
| grand_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0 | 
| original_cart | TextField | null=False, blank=False, default='' | 
| stripe_pid | CharField | max_length=254, null=False, blank=False, default='' | 
**Order Line model:**

| Key in db | Field Type | Validation |
|---|---|---|
| order  | ForeignKey | Order, null=False, blank=False, | on_delete=models.CASCADE, related_name='lineitems' | 
| event  | ForeignKey | EventInstance, null=False, blank=False, |on_delete=models.CASCADE | 
| which_athlete  | CharField | max_length=2, null=True, blank=True | 
| quantity  | IntegerField | null=False, blank=False, default=0 | 
| lineitem_total  | DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False | 


#### Checkout app

| Key in db | Field Type | Validation |
|---|---|---|

#### Clubs app

**Club model**

| Key in db | Field Type | Validation |
|---|---|---|

#### Events app

**Discipline model**
**Distances model**
**Format model**
**Organiser model**
**Event Instance model**
**Event model**

| Key in db | Field Type | Validation |
|---|---|---|

#### Home app

| Key in db | Field Type | Validation |
|---|---|---|

#### Profiles app

**User Profile model**
**Athlete Profile model**
**Racehub Friends model**
**Non Racehub Friends model**

| Key in db | Field Type | Validation |
|---|---|---|

#### Results app

**Result model**

| Key in db | Field Type | Validation |
|---|---|---|
| eventinstance  | ForeignKey | EventInstance, on_delete=models.SET_NULL, null=True, blank=True | 
| distance  | ForeignKey | Distance, null=True, blank=True, on_delete=models.SET_NULL | 
| discipline  | ForeignKey | Discipline, null=True, blank=True, on_delete=models.SET_NULL | 
| event_format  | ForeignKey | Format, null=True, blank=True, on_delete=models.SET_NULL | 
| athletefirstname  | CharField | max_length=40, null=True, blank=True | 
| athletesurname  | CharField | max_length=40, null=True, blank=True | 
| athlete  | CharField | max_length=125, null=True, blank=True | 
| dateofbirth  | DateField | null=True, blank=True | 
| gender  | CharField | 
    max_length=2,
    choices=gender_choices,
    null=True, blank=True
 | 
| bibnumber  | DecimalField | max_digits=6, decimal_places=0, null=True, blank=True | 
| agecat  | CharField | 
    max_length=6,
    choices=age_cat_choices,
    default=Senior,
    null=True, blank=True
 | 
| athlete_type  | CharField | 
    max_length=18,
    choices=athlete_type_choices,
    default=Myself,
    null=True, blank=True
 | 
| club  | ForeignKey | Club, null=True, blank=True, on_delete=models.SET_NULL | 
| chiptime  | DurationField | null=True, blank=True | 
| guntime  | DurationField | null=True, blank=True | 
| isvirtual  | BooleanField | null=True, blank=True, default=False | 
| hyperlink  | CharField | max_length=240, null=True, blank=True | 
| imageupload  | ImageField | null=True, blank=True | 
| verifiedresultforvirtual  | BooleanField | null=True, blank=True, default=False | 
| linkedathlete  | DecimalField | max_digits=3, decimal_places=0, null=True, blank=True | 



## [Deployment](#deployment)
[Developer Aims](#developer-aims) | [UX](#ux) | [User Stories and Corresponding Features](#user-stories-and-features) | [UI Structure](#ui-structure) | [Visual Layout](#visual-layout) | [Technologies Used](#technologies-used) | [Information Architecture](#information-architecture) | [Deployment](#deployment) | [Local Development](#local-development) | [Testing](#testing) | [Acknowledgements](#acknowledgements)

* On Heroku Website https://dashboard.heroku.com/apps , New -> Create New App
* Choose App name and region.
* Use Resources - Addons - Heroku Postgres

* In gitpod:
- pip3 install dj_database_url
- pip3 install psycopg2-binary
- pip3 freeze > requirements.txt

* In settings.py
- `import dj_database_url`

```
# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}


DATABASES = {
    'default': dj_database_url.parse('postgress-url-goes-here')
}
```
* NB Get url from Heroku App settings tab / reveal config vars.

* Run migrations again (different database)

* `python3 manage.py showmigrations` Will show none exist

* `python3 manage.py migrate`

* To import product data, use fixtures:
- `python3 manage.py loaddata categories`
- `python3 manage.py loaddata products`
- NB categories must be created first as products depend on them.

* Create superuser account in the new database
- `python3 manage.py createsuperuser`


NB DO NOT COMMIT DATABASE URL TO VERSION CONTROL.

* Update settings.py to connect to a different database depending on if this is deployed or production version:

```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```

* `pip3 install gunicorn`
* `pip3 freeze > requirements.txt`
* Create `Procfile` in root folder with the contents `web: gunicorn race_hub.wsgi:application`

* NB: Check folder for Procfile is correct

* In terminal:
- 'heroku login' or 'heroku login -i'
- `heroku config:set DISABLE_COLLECTSTATIC=1 --app race-hub`

* In settings.py `ALLOWED_HOSTS = ['race-hub.herokuapp.com', 'localhost']`
* NB must be wrapped in `` above.

* If the app was created on the heroku website, set the remote repo. `heroku git:remote -a race-hub-ado`

* to check: `git remote -v`

* The great moment! `git push heroku master`

* To deploy to github automatically:
- In Heroku web interface:
- Deploy -> Github
- Select repo and connect.
- Enable automatic deploys

* https://miniwebtool.com/django-secret-key-generator/ 
- Add this to Heroku -> Config Vars -> Add the secret_key
-  Update settings.py to contain it: `SECRET_KEY = os.environ.get('SECRET_KEY', '')`
- Set `DEBUG = 'DEVELOPMENT' in os.environ` in settings.py

### Creating an AWS Account

* Use AWS s3 to store static files.
- Create account at https://aws.amazon.com/
- Account type personal
- Go to AWS Management Console.
- Open s3
- Create new bucket
- In Set Permissions, uncheck Block All Public Access

* Bucket settings:
- Properties -> Static Website Hosting
- Use default values index.html and error.html
- Save
- Permissions:
- CORS Configuration:
```
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
<CORSRule>
<AllowedOrigin>*</AllowedOrigin>
<AllowedMethod>GET</AllowedMethod>
<MaxAgeSeconds>3000</MaxAgeSeconds>
<AllowedHeader>Authorization</AllowedHeader>
</CORSRule>
</CORSConfiguration>
```
- Bucket Policy -> Policy Generator
- Policy Type: s3 Bucket Policy
- Principal: *
- Action: GetObject
- Copy ARN from the other tab eg `arn:aws:s3:::race-hub-ado`
- Add statement
- Generate Policy
- Copy Policy into other tab 'Bucket Policy'
- BEFORE SAVING: add /* into the resource key `"Resource": "arn:aws:s3:::race-hub-ado/*",`
- Access Control list -> Public Access -> Tick 'List Objects' and save.

* Use AWS service 'IAM' to connect to the bucket
- Go to IAM
- Click Access Management -> Groups
- Create New Group 'manage-race-hub'
- Click next twice (no policy to attach yet)
- Create Group
- Policies -> Create Policy
- Create Policy
- json tab -> Import managed policy
- Search for s3 and import the s3 Full Access Policy.
- From Bucket Policy in s3, get the arn and edit the json accordingly.
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::race-hub",
                "arn:aws:s3:::race-hub/*"
                ]
        }
    ]
}
```
- Review Policy
- Add name and description. 
- Create
- Go to Groups -> Select the group -> Permissions tab -> Attach policy -> search and attach.

* users
- Add user
- Include static files access.
- Next: Permisssions
- Add user to group.
- Create user
- ESSENTIAL: Download .csv file.

* Connecting django to Amazon s3.

- `pip3 install boto3`
- `pip3 install django-storages`
- `pip3 freeze > requirements.txt`
- Add 'storages' to installed apps in settings.py

- in settings.py:

```
if 'USE_AWS' in os.environ:
    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'race-hub'
    AWS_S3_REGION_NAME = 'EU (London)'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```

- Add these config vars in Heroku: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, USE_AWS.
- Delete Config Var for DISABLE_COLLECTSTATIC

- create custom_storages.py in main project folder. NB CHECK this location carefully. It should be at the same level as README.md
```
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```
- update EU (London) to eu-west-2 in settings.py

* Add cache control:
```
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }
```

- Go to s3 and create a new folder called media. Upload all product images.
- Grant public permissions.

* Tidying up

- attempt to log in as admin (causes allauth to attempt to verify)
- in django admin panel, verify email address and make primary for the super user account.

* Stripe
- Add Stripe Keys to heroku config vars.
- Add new Stripe Webhook Endpoint. (Remember to tick viewing test data)
- Configure endpoint as follows:
- https://race-hub.herokuapp.com/checkout/wh/
- Select Receive all events.
- Add Endpoint.
- Add signing secret to Heroku Config Vars.
- Should now have: STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY, STRIPE_WH_SECRET - all matched to what exists in settings.py
- send test webhook from Stripe to check.

### Email setup.

* In Gmail:
- Settings (cog)
- Accounts and import
- Other Google Account Settings
- Security
- 2 Step Verification
- Verify
- Turn On
- Under Signing in to Google heading, choose app passwords.
- Create app passwords: Type Mail / Other / enter django in the box.
- Copy the key and enter it in the Heroku app as a config var as EMAIL_HOST_PASS
- Create EMAIL_HOST_USER as the gmail account.

* In settings.py:
```
if 'DEVELOPMENT' in os.environ:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = 'hello@racehub.com'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
    DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')
```



## [Local Development](#local-development)
[Developer Aims](#developer-aims) | [UX](#ux) | [User Stories and Corresponding Features](#user-stories-and-features) | [UI Structure](#ui-structure) | [Visual Layout](#visual-layout) | [Technologies Used](#technologies-used) | [Information Architecture](#information-architecture) | [Deployment](#deployment) | [Local Development](#local-development) | [Testing](#testing) | [Acknowledgements](#acknowledgements)

## [Testing](#testing)
[Developer Aims](#developer-aims) | [UX](#ux) | [User Stories and Corresponding Features](#user-stories-and-features) | [UI Structure](#ui-structure) | [Visual Layout](#visual-layout) | [Technologies Used](#technologies-used) | [Information Architecture](#information-architecture) | [Deployment](#deployment) | [Local Development](#local-development) | [Testing](#testing) | [Acknowledgements](#acknowledgements)

## [Acknowledgements](#acknowledgements)
[Developer Aims](#developer-aims) | [UX](#ux) | [User Stories and Corresponding Features](#user-stories-and-features) | [UI Structure](#ui-structure) | [Visual Layout](#visual-layout) | [Technologies Used](#technologies-used) | [Information Architecture](#information-architecture) | [Deployment](#deployment) | [Local Development](#local-development) | [Testing](#testing) | [Acknowledgements](#acknowledgements)


### Nice to have
- dropdowns open on hover (desktop)



## Navigation
Used advice from https://stackoverflow.com/questions/29752882/cant-scroll-within-mobile-drop-down-nav/29753214 to make mobile mega dropdowns scroll on mobile devices
Refactored code, based on: https://codepen.io/JakubHonisek/pen/xXaYqg
Code for mobile view buttons refacroted from Code Institute tutorial



## Home Page App

- Pillow installed to handle image field


## Events App
- Inspiration for Bootstrap cards taken from: https://codepen.io/aminulhchy/pen/RVeJMZ

## Known Issues
- Remove item from cart removes all entries for this event, not the single athlete.

### Testing

Navigation elements from https://codepen.io/skywalkapps/pen/VeNzwG were found to be incompatible with Bootstrap 4.

### References and Acknowledgements:
Responsive Bootstrap Mega Menu: https://codepen.io/JakubHonisek/pen/xXaYqg

#### Stripe

Card number for testing with authentication (triggers popup with overlay)
4000 0025 0000 3155

## Deployment

### NB need bulk data import using fixtures for news sets of results, clubs etc:
NB: Fixtures have not been used to upload bulk product data so import of results data etc.

NB: Heroku login ipaddress mismatch error: Use `heroku login -i` to login from terminal rather than opening browser

NB: eu-west-2 for London in django settings.

During Deployment an error was found in the requirements.txt file due to a typo. This was fixed and the deployment process was then successful.

During Deployment a typo was found in Procfile. NB race_hub is the name of the application. race-hub is used in AWS and also as the project name in Heroku.

NB When logging in to deployed app for the first time, to verify email address... this may not appear. Try logging in to front end. This will cause allauth to create the email address in the back end. It can then be verified.

Bug found during deployment. Image urls were incorrectly coded and did not include {{ MEDIA_URL }} path.


### Credits:

- icons licensed and used from https://uxwing.com/
- logos created by the author using Boxy SVG for macos