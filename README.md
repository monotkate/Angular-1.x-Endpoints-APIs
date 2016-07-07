# Angular 1.x Endpoints APIs

This shows an example on how to use Endpoint APIs integrating with Angular 1.x

## Installation

* [Node.js](https://nodejs.org/en/)
* [CloudSQL] Database
* [Python]

This example uses a CloudSQL database.  In order for the code to work, you will need to set up your own database and insert the information into the apis.

Start off by doing a `node install` command in the command line in your working directory after cloning the repository.  This should install anything necessary to make the project work.  Once you do this, move `angular`, `angular-animate`, `angular-aria`, `angular-material`, `angular-messages`, `angular-ui-router` to a lib folder within src.  I haven't set up doing this automatically yet.  Sorry.

## Running

In order to run locally, run `dev_appserver.py . ` while in the src directory.  This will initiate a local server on port 8080.  Navigate to http://localhost:8080/ in your favored browser in order to run the code.  Check for console errors.

## NOTE

I legitimately put in comments where the database info goes, so this will not connect to anything unless you update the API definitions.  You can still take a look at the code and how it connects regardless.

Check https://monotkate.wordpress.com for some walkthroughs on what exactly I did in the code and why.  I'll be updating over the next few days (today is 7/7/16)
