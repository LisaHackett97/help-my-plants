# [Help My Plants](https://help-my-plants.herokuapp.com/)


![site-mockup](README-assets/final-site-image.PNG)


Help My Plants is a site designed to give users a place to find out how to look after their house plants, and helo choosng the best plants for the space/light in their home/office.
User can learn how to better look after their house plants and find out why they should, by reading articles provided on the site. It will give registered users more information on the benefits of plants and some common things to do to care for their house plants, with links back to the services page where they can book a consulation service relating to the issue. 
The site offers consultation services for registered users to book services. These paid services will consist of personalised one to one advice/guide/lessons on caring for and choosing plants, learning the benefits of keeping plants with follow up consultations available

Site is aiming to encourage people to book consulations and get help on how to not kill their plants!. 

[Link to live Site](https://help-my-plants.herokuapp.com/)

## **To open any links in a new tab, please press Ctrl + click**

## Table of Contents

- [UX](#ux)
  - [External User Goals](#external-user-goals)
  - [Site Owner Goals](#site-owner-goals)
  - [Strategy and Scope](#strategy-and-scope)
  - [Structure](#structure-of-the-website)
  - [Wireframes](#wireframes)
  - [Surface](#surface)
    - [Colors](#colors)
    - [Typography](#typography)
    - [Images](#images)
	- [DB Schema](#dbschema)
    - [Features](#features)	
- [Technologies](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
    - [SetUp](#set-up)
    - [Heroku Deployment](#deployment-to-heroku)
    - [Run repo locally](#download-and-run-repo-locally)
    - [Cloning the repo](#cloning-the-repo)
    - [Forking the repo](#forking-the-repo)
- [Credits](#credits)

---



## UX

#### User Stories

| ID    | As as a:        | I want to:                                            | By:                                                                                                                                 |
|-------|-----------------|-------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| US-01 | First time User | Find Out what the site is about                       | Viewing the page and reading information                                                                                            |
| US-02 | First time User | Navigate easily                                       | View accessible parts of the site without to many clicks                                                                            |
| US-03 | First time User | Register, then login to the site                      | Easily enter my registration details, then click to login                                                                           |
| US-04 | Registered User | Login to the site                                     | Easily enter my login details to enter thesite                                                                                      |
| US-05 | Registered User | View Services & Prices                                | Reading the list of available services and being able to view the cost of each                                                      |
| US-06 | Registered User | Choose and book a service                             | Select a service, view the cost, add my details and click to submit                                                           |
| US-07 | Registered User | Make a payment for the service                        | Easily enter my payment info and complete payment quickly                                                                           |
| US-08 | Registered User | Submit the order                                      | clicking to submit and receiving a confirmation                                                                                     |
| US-09 | Registered User | Navigate easily                                       | Moving around the site with as few clicks as possible, and understand easily how to naviagate to different parts of the site        |
| US-10 | Registered User | View More info                                        | Clicking on a more info item and beng able to read the information                                                                  |
| US-11 | Registered User | View my profile                                       | Clicking on a menu item/icon and seeing my registered details                                                                       |
| US-12 | Registered User | Edit my profile                                       | Clicking on my profile page and updating details                                                                                    |
| US-13 | Registered User | See my previous orders                                | Viewing my profile page and seeing my list of previous orders                                                                       |
| US-14 | Registered User | See my Active order                                   | Viewing my profile page and seeing my active order                                                                                  |
| US-15 | Registered User | Log Out                                               | Clicking on a menu item/icon and easily logging out                                                                                 |
| US-16 | Site Owner      | Provide the functionality for users to Register/Login | Providing a login and registration forms, which are easy for the user to update, and easy to find, through menu option or buttons   |
| US-17 | Site Owner      | Showcase available services & Cost                    | Provide a list of available services with descriptions and cost, that will encourage users to book                                  |
| US-18 | Site Owner      | Allow users to choose & book a service                | Providing an option to select a service and a form to book                                                                          |
| US-19 | Site Owner      | Allow users to pay for the service online             | Providing an easy and secure payment section                                                                                        |
| US-20 | Site Owner      | Give users a confirmation email                       | Giving users a confirmation that their booking was successful and sending an email                                                  |
| US-21 | Site Owner      | Provide more info on what the site is about           | Providing an easy to find page, with content interest to the user, links back to the services page to encourage booking of services |
| US-22 | Site Owner      | Delete content                                        | Easily deleting incorrect/expired content, through easy to use delete options                                                       |
| US-23 | Site Owner      | Edit content                                          | Easily editing content, through easy to use edit options                                                                            |
| US-24 | Site Owner      | Provide the functionality for users toLogout          | Providing a logout form,  which the user can find through through menu option or buttons                                            |


### Strategy and scope

The main goal of the site is to provide user with a site where they can find find out how to "not kill their house plants".
To convert a visitor, and draw them in, there will be a short explanation of qhat they can access on the site. Links to the booking/services page will be provided across the site


##### Strategy and scope tables

<details>
  <summary>![Strategy and scope plan] </summary>
  <img src="README-assets/ux-strategy-plan.PNG" alt="strategy-plane-plan-part1" width="80%" height="80%">
  <img src="README-assets/ux-scope-plan.PNG" alt="scope-plane-plan-part2" width="80%" height="80%">
</details>
<br>

### Structure of the website

The basic structure of the site is designed around making it easy for the user to navigate and book services. A user will land on the home page where they can view some high level information and use a simple process to register/login in order to view detailed articles and book services. 

Login, registration, andd logout will also be provided in simple easy to use format. 
Users can read interesting articles about plants, wnd links to booking will be provided on tis page, to encourage booking the services.
Users can view cards with all services which can currently be booked, they will be then taken to a simple checkout page where payment details can be provided.
A profile page will give the user their details. Options will be provided for admin to add new services, and edit or delete currently existing services

#### Structure Plan

 <details>
  <summary>Surface plane plan </summary>
  <img src="README-assets/ux-structure-plan-pt1.PNG" alt="surface-plane-plan-part1" width="80%" height="80%">
  <img src="README-assets/ux-structure-plan-pt2.PNG" alt="surface-plane-plan-part2" width="80%" height="80%">
</details>
<br>

### Wireframes

#### Final Wireframes 

[This is the final mobile wireframe](README-assets/wireframe-mobile-final.pdf)
These were built using balsamiq.

- 
#### These were the original wireframes

[Mobile](README-assets/wireframe-mobile.pdf)

[Tablet](README-assets/wireframe-tablet.pdf)

[Desktop](README-assets/wireframe-desktop.pdf)

### Surface

#### Includes some design decision made during development

- Footer added day before submission. To give better layout on full content pages. However for logout and empty cart pages, footer is floating up the page.
I have the code to fix the footer, but when this is applied to footer in base template results in footer fixing on top of content in some pages such as articles.
For this project and due to time issues, I have just added some margin on logout and empty cart pages so that footer shows in middle of page and doesn't hug the buttons.
If time allows, will come back to this

- Home page link on mobile nav bar, not on desktop version. Link to home through Icon/branch which is hidden on mobile.

- Decisions relating to time/date field:
	-  My plan was to have a calendar app that user could select availability from, which would be added to order. Couldn't quite figure out how to do this. Then decided
to have a user input field on checkout, which would then be added to order. Ran out of time to get this fully in place, was not getting the date to attach/update on the customers order. Date cannot be updated by user at this time but have added a note and if/else stmt to order history. Wanted to then give Admin access on the front end to amend the "confirmed Date". Page is available but unfortunately I ran out of time to get this full in place. Left page in place for admin but disabled buttons and added a message to admin. Adminuser with access to DB can update at that point.

- I originally planned to have a "one-click" type payment for each product. Due to my knowledge at this time, I decided to change this so that users could book mulitple services(though at this time only one of each type), by adding to cart and procedding to the checkout page.

- I hadn't included quantities on the services. This was designed with the user/customer only wanting to book one service type at a time. A future feature would be that the customer could increase the quantity to book for multiple people on the one booking.

 <details>
  <summary>Surface plane plan</summary>
  <img src="README-assets/ux-surface-plan.PNG" alt="surface-plane-plan" width="80%" height="80%">

</details>
<br>



#### Colors

I used the coolors site to generate a pallette related to plants and nature. These were set as root colours in css and used throughout the site. Where there were
contrast colour issues, I used color picker to change, tryin to keep selected colors in line with site theme.
- Root Colours are: 
 	- main-text-color: #3D4A3D;
	- headers: #343434;
    - color1:#138A36;
    - color2:#D4C5C7

#### Typography

There will be two fonts used throughout the website. The titles font will be Hind, and the accompanying body font will be Poppins. Fallback fonts for both are san-serif
I feel these fonts are easy for user to read on screen and are visually appealing.


#### Images

I used one background image on the home page. Each of there services has an accompanying plant image. 
And there is a small image with each article for visual appeal

#### DB Schema

DB has ...

![DB Schema diagram]

[Back to table of contents](#table-of-contents)

## Features

**_Website has the following features_**

### Features which are accessible on all pages with the exception of error pages.

#### Navigation Menu. 

#### Logout 
#### Icon


#### 

### Features on individual pages







## Future Features

- Full ability for Admin to update dates/times on orders (Functionality for this has been started on the site but not finished due to time constraint)
- Ability for user to select an available date/time slot from site owner provided calendar
- Ability for user to book each service for multiple people. ie using a quantity type input field.



[Back to table of contents](#table-of-contents)

## Defensive Design 

The following are defensive design elements identified in planning. Each will be manually tested (See testing docs)

 <details>
  <summary>Click </summary>
  <img src="README-assets/Defensive-Design-Notes.PNG" alt="DefensiveDesign" width="80%" height="80%">
</details>
<br>
		
*** Abuse of Admin privileges, controls on this and info security need to be in place as part of the business process ***


## Technologies Used

- HTML5 - Programming language for structuring the site.
- CSS3- Style sheet programming language
- Python3, Jinja templating language.
- Postgres DB

- [Github](https://github.com/)- software hosting platform to keep project in a remote location
- [Gitpod](https://gitpod.io/) - a development hosting platform
- Git - used for version-control.
- [Google fonts](https://fonts.google.com/) -used to select and provide typography.
- [Balsamiq](https://balsamiq.com/) - used to build wireframes. Downloaded software to use.
- [Markdown table convert](https://tableconvert.com/) - I am using this to turn data on excel into markdown table syntax
- Microsoft word and excel: to assist in organising planning for project
- Amazon Web services for hosting static files
- [Site for creating DB schema diagrams](dbdiagram.io)
- [Site to enable me to edit pdfS](https://www.ilovepdf.com/) - I needed a tool to allow me to edit pdfs of diagrams 
- [Heroku for deployment](https://heroku.com/)
- Stripe for payments
- gmail for sending emails to users
- temp-email.org
- Secret-key generator
- [Favicon generator - website planet](https://favicon.io/)
- Bootstrap4
- Fontawesome & google fonts
- [ami responsive for mock-ups](ami.responsivedesign.i)
- Validators:
  - jshint
  - validator.w3.org
  - jigsaw.w3.org/css-validator
  - pep8online.com
- [techsini for mock-ups](https://techsini.com/multi-mockup/index.php)
- WAVE extension for reviewing accessibility and colour contrasts in testing.
- Chrome Dev Tools - used to view responsiveness and layout as site was being developed. I found this very useful when developing the site, as it aided my learning throughout the project.
- 


[Back to table of contents](#table-of-contents)

## Testing

[Testing Documentation]


- Issues during development and bugs are covered in this document, in addition to the planned testing.

## Deployment

### Set up:

1) Some requirements
- git
- python3
- pip3 to install packages
- for connection with flask, run these--> pip3 install dnspython  pip3 install pymongo  
	- (*ensure these are added to the requirements.txt file)
- Flask:  install Flask-->  pip3 install flask
- ....
- Heroku Account

2) ...
	
3) In Gitpod, create....

4) Add env.py file to .gitignore. 

5) Connecting...
	

6) import os and set config variables in the env.py file, using os.environ.setdefault()

	a. 
	b. 
	c.
	d.
	d. 

7) In the app.py file, set up imports, flask and other required variables:
	- note using an if statment to import the env.py, will create the __pycache__ directory, which must also be added to the .gitignore file.

8) Commit and push appropriate files to Github.

### Deployment to Heroku:

1. A requirements.txt file must be in place
	Use the command-->  pip3 freeze > requirements.txt

2. Add a Procfile, so that Heroku know how to run the app
	Use the command-->  echo web: python app.py > Procfile
Ensure there are no additional blank lines in the Procfile

3. Create a new app in Heroku
	- On the dashboard, click New, and Create New app
	- Give the app a unique name (Use hyphens instead of spaces), select Region and click Create App
4. 
5. 

![New App]


4. Set up environmental variables in Heroku.
	- Select Settings
	- Select Reveal Config Vars
	Add the following and their corresponding key values. Click Add after each
	- 

![Adding config vars](

**Config Variables must be set up before Automatic Deployment is put in place**

5. Set up Automatic Deployment to Github
	- Select Deploy tab
	- Choose deploy using Github. Select your repo and click connect
	- Under automatic deploy, choose master branch 
	- Click Enable automatic deploys. ***nb ensure config variables are set up before you do this)
	- Under manual deploy section, select the branch to deploy
	- Click Deploy branch
	- A message should be displayed once the app is successfully deployed
	- Click view to launch app

![Auto deployment to Github](README-assets/deploy-connect.PNG)

### To download and run locally, follow the below steps:

1. Log into GitHub and lcoate the repository.
2. Select Code
3. Click Download Zip
4. Once files have downloaded, you can extract and use cloned-project locally.

### To Clone, follow the below steps:

1. Log into GitHub and select the repository.
2. Select Code
3. Click https and copy the link
4. Open git bash
5. Change the working directory to where you want the cloned directory
6. Use command git clone and the copied URL
7. Press enter

NB: In order to work with a clone of this project, you will need to create the env.py file using your own variables and create a MongoDB database with collections. See Databas Schema section of this document for more details.
You will also need to install all of the packages listed in the requirements file you can use the following command in the terminal pip install -r requirements.txt which will do it for you.



### Forking the repository:

1. Log into GitHub and select the repository.
2. Select Fork on top right hand corner.
3. A copy should be created in your github profile and pull requests submitted.

GitHub docs link [Forking a repository](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/cloning-and-forking-repositories-from-github-desktop#forking-a-repository/)




## Credits

### Media

#### Images Used


- Favicon generated from (https://favicon.io/)


- pixabay.com
	- Cactus1  
	- Pink-Orchid
	- Green-plant1#
	- cactus-2
	- aloe-vera-2
	- bonsai-pink
	- bonsai-1
	- No camera image
- Unsplash.com
	- Aloe-vera1  unsplash.com/@laurinscheuber

#### Other

- lorem ipsum generators
		- http://www.cupcakeipsum.com/

### Content

##### Home Page and Articles Page Content
https://lifehacker.com/why-you-keep-killing-your-plants-and-what-to-do-about-i-1778545598
https://www.rte.ie/lifestyle/living/2021/1203/1264612-tips-to-keep-your-house-plants-alive-this-winter-and-beyond/
https://www.tinashomedesigns.com/inspiration-solutions/design/benefits-of-houseplants
https://www.gardenersworld.com/plants/25-of-the-best-house-plants-to-grow/
https://www.healthline.com/health/healthy-home-guide/benefits-of-indoor-plant
https://www.prevention.com/health/g27586276/benefits-of-indoor-plants/
https://www.rhs.org.uk/plants/types/houseplants/for-human-health


### Colours

- coolor.co to select colours
- color picker to change as needed

### Code


- I reused the code from my MS3 project for the back to top button/icon. This was originally found on https://www.w3schools.com/howto/howto_js_scroll_to_top.asp */
- I followed the Code Institute Boutique Ado walkthrough to guide me through the structure and help me learn what I needed to do.
- Stripe JS Core logic/payment flow comes from ( https://stripe.com/docs/payments/accept-a-payment)
- And CSS from (https://stripe.com/docs/stripe-js)

### Acknowledgements

I referred to the following to add to my knowledge and for help.

- https://boto3.amazonaws.com/v1/documentation/api/latest/index.html 
- https://lynxbee.com/cloud-technologies/django-and-django-rest-framework/
- https://www.geeksforgeeks.org/django-models/?ref=lbp
- w3docs.com
- https://django-allauth.readthedocs.io/
- stackoverflow
- https://thecodelearners.com/python-django-forms-creating-rendering-validating-and-saving-forms/
- Stripe Docs https://stripe.com/docs/payments/payment-element
- pytutorial.com
- boutique.ado walkthrough projuect
- developer.mozilla.org
- https://lynxbee.com/cloud-technologies/django-and-django-rest-framework/
- https://www.geeksforgeeks.org/django-models/?ref=lbp
- https://www.codacy.com/***
- Code Institute course material, in particular I followed the Boutiqu Ado walkthrough to guide me through the structure
- Slack Community - I searched for a topic and usually someone else had the same question. This has been a great help in developing my understanding.
- And thank you to those on slack who took the time to review my project and give me feedback.
- Thank you to my mentor Adegbenga Adeye, for his help and guidance.

[Back to table of contents](#table-of-contents)

This site was developed for Educational purposes