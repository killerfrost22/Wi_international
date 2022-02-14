# Wi_international
 Willhelm International Care 

## Description

An appointment website designed for Willhelm International. 

# Tech stack 
Flask, Django, Sql, Bootstrap, jQuery.

<!-- **Webiste:** [Deployed on Pythonanywhere](http://jasonchan.pythonanywhere.com) -->

## Admin view:

Administrator can be created only through terminal of server by using "./manage.py createsuperuser" command. An [administrator](username: test, password: test) has been created, please feel free to test the data intergrity and consistency.

1. Administrator has Create, Read, Update, and Delete control of the user.
2. Administrator has Create, Read, Update, and Delete control of the appointment.
3. Administrator has Create, Read, Update, and Delete control of the prescription.
 
## Doctor view
 
1. Prescribe medication (type of medication/dosage/duration). (Doctor can only prescribe to those who have appointment in the future.)
2. View scheduled appointments
3. See patient appointment and medication history


## Patient View

1. book appointments with specific doctors - view only current medication and dosage.
2. Book appointment by types(primary care, flu, mental care, and etc)