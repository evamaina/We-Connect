# We-Connect
<<<<<<< HEAD

WeConnect provides a platform that brings businesses and individuals together. This platform creates awareness for businesses and gives the users the ability to write reviews about the businesses they have interacted with.  

## Required Features
1.Users can create an account and log in

2.Authenticated Users can register a business.

3.Only the user that creates the business can update and delete a business

4.Users can view businesses.

5.Users can give reviews about a business.

6.Users can search for businesses based on business location or business category.
### Built with:
Html/css

Bootstrap

#### Prerequisites
The templates make use of HTML and Css and will accomadate future integration of a python SQLAlchemy database and flask. This program can run on any web browser conviniently

##### Contributing
1. Fork this project to your GitHub account.

2. Create a branch for version control.

3. Proceed to make modifications to your fork.

4. Send pull request from your fork's branch to my master branch.

###### Author:

Eva Maina
=======
[![Build Status](https://travis-ci.org/evamaina/We-Connect.svg?branch=Challenge2)](https://travis-ci.org/evamaina/We-Connect)
[![Coverage Status](https://coveralls.io/repos/github/evamaina/We-Connect/badge.svg?branch=master)](https://coveralls.io/github/evamaina/We-Connect?branch=master)

WeConnect provides a platform that brings businesses and individuals together by creating awareness for businesses and giving the users the ability to write reviews about the businesses they have interacted with.



## Testing
Run command nosetests tests --with-coverage

## Api Endpoints
## Users

POST /api/v1/auth/register Creates a user account

POST /api/v1/auth/login Logs in a user

POST /api/v1/auth/logout Logout a user

PUT /api/v1/auth/reset-password Resets user password

## Businesses

POST /api/v1/businesses Register a new business

GET /api/v1/businesses List all registered businesses

PUT /api/v1/businesses/<businessId> Update business

DELETE /api/v1/businesses/<businessId> delets a business

## Reviews

POST /api/v1/businesses/<businessId>/reviews create a new review

GET /api/v1/businesses/<businessId>/reviews Get reviews


### Author:

Eva Maina








>>>>>>> f55cea202124dca029cda1c421e6483357c2cebe
