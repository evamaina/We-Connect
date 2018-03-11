# We-Connect
[![Build Status](https://travis-ci.org/evamaina/We-Connect.svg?branch=Challenge2)](https://travis-ci.org/evamaina/We-Connect)
[![Coverage Status](https://coveralls.io/repos/github/evamaina/We-Connect/badge.svg?branch=master)](https://coveralls.io/github/evamaina/We-Connect?branch=master)

WeConnect provides a platform that brings businesses and individuals together by creating awareness for businesses and giving the users the ability to write reviews about the businesses they have interacted with.



## Testing
Run command nosetests tests --with-coverage

## Api Endpoints
##Users
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
(Designs)HTML Pages included
The following are the included HTML pages


### Author:

Eva Maina








