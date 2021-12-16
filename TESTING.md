# [Help my Plants!]

![site-mockup]

## [Link to live site]

This document will cover manual, compatability and validation testing. Issues found during development and bugs are also detailed.
I have included a section on the defensive design elements of the site I planned.

## **To open any links in a new tab, please press Ctrl + click**



## Table of Contents

- [Testing](#testing)
  - [Planning Approach](#testing-plan)
  - [Defensive Design](#Defensive-design)
  - [Functionality testing](#functionality-testing)
  - [Compatibility testing](#compatibility-testing)
  - [User stories testing](#user-stories-testing)
  - [Issues found during site development](#issues-during-development)
  - [Bugs](#bugs)
  - [Performance and Accessibility testing](#performance-and-accessibility-testing)
  - [Code Validation](#code-validation)
  - [Main README File]
    
---

### Testing Plan

Testing Plan:

For each change/bug resolved, test the feature to ensure working as expected. Test other developed features to ensure no changes

Once main development finished, the following testing should be done.

#### Manual testing will cover the following
  
- Run Functionality/feature tests
- Each feature is tested per plan. Feature, expectation, testing and results are noted.
- Negative and positive cases to be tested
- Tests to be run for each feature on the site. Each will be tested for 3 user types. Logged-out/logged-in/admin.
- If a bug is encountered, work is done to resolve. Noted in bugs section. And testing cycle to start at beginning.
- Check responsiveness for screen sizes
- Do the user story testing. Review each goal of users. Note how this is achieved. Issues noted
- Review already resolved bugs and test again.

#### Non-manual testing

Run code through

- validators
- lighthouse
- WAVE extension

Validation of code re-checked each time a change made, after the main development completed. <br>
If issues occur, resolve and re-run validation tests. <br>
Wave tests help identify issues early so that they could be corrected and feature/functions re-tested.

- Validate css, html and javascript.
- Lighthouse reports
- WAVE accessibility reports
- Cross brower testing


[Back to table of contents](#table-of-contents)

### django testing TBC

#### Defensive Design

The following are defensive design elements identified in planning. Each will be manually tested

[Back to table of contents](#table-of-contents)

### Functionality Testing

#### Features accessible across all pages 


[Back to table of contents](#table-of-contents)
### Compatibility Testing

- Site was manually tested on google chrome,microsoft edge, firefox and opera. No issues.

- I have access to IE10. Site has limited functionaility as site uses ES6. Recommended to use Microsoft edge rather than IE for best viewing experience
Recommended do not use IE10 to view site, please use Microsoft edge for best viewing experience

[Back to table of contents](#table-of-contents)
### User stories Testing


[Back to table of contents](#table-of-contents)

### Issues during development


- Issues getting the Post functionaility on the Add Service form to work. The add to cart was working. To resolve I needed to add back in item_id and fix action on the form element.

- Deployed to heroku no issues. Set up AWS bucket, with settings etc.
  - Was having issues with site deploying. Resolved as I needed to reinstall gunicorn and update requirements file (Happened after gitpod update)

- My plan was to have a calendar app that user could select availability from, which would be added to order. Couldn't quite figure out how to do this. Then decided
to have a user input field on checkout, which would then be added to order. Ran out of time to get this fully in place, was not getting the date to attach/update on the customers order.
Date cannot be updated by user at this time but have added a note and if/else stmt to order history. Wanted to then give Admin access on the fron end to amended the "confirmed Date". Page is available but unfortunately I ran out of time to get this full in place. Left page in place for admin but disable button and message to admin. Admin-user with access to DB can update at that point.

-  Main issue I had during development took a number of days to resolve. During building of the checkout, all code updated and linked to stripe, with variables set up. 
No issues on local server, all worked and displayed as expected, but when deployed to Heroku I was getting 500 server errors, both on the site and when I tried to access services/orders in the heroku admin. Below is a summary of the steps I took to try and resolve.
  - Result was that it was an issue with migrations not applied to Heroku site.  Once these are updated all ok. 
  - I also needed to re-create a new Heroku superuser.
I eventually found resolution as I was a looking through slack to see if anyone had any particular issues with Heroku. Was a different issue someone had asked about but gave me the idea to check the migrations on postgress (Apologies I can't find the thread to thank them)
##### Steps taken
  1. Created a copy of main branch
Decided to work backwards to try id issue. 
  - Removed some of the payment intent success code. Still 500
  - Removed order number from checkout success url to see if could just display that page. Still 500
  2. Check the views for adding a new order. Check fields. Something diff local v deployed?
No, all same. tried removing references to webhook, removing just those files etc. Not working in live/deployed
  3. Reverted to the commit where I had finshed setting up stripe payments and got checkout success page working. This works in Heroku app
And order is created in the heroku admin
  4. Next Steps, go through WebHook set up and test on deployed at smaller incremental stages Testing endpoint worked. Pushed code
  Next set the stripe wh secret in heroku, enable end point and test app. All ok here
  5. Next Add cache checkout view and url. Deployed. All ok
Then added JS and update webook handle payment sucess to view meta data in terminal. Can see meta data ok
but IntegrityError at /checkout/ NOT NULL constraint failed: checkout_order.original_cart. migrations needed to be done.
  6. Step by step add webhook code back in.
When updating the payment intent success, starting to show a 500 error in terminal
And Order is not defined. Add import to file. recheck local Push and test. Can see the 500 error in terminal
  7. At this stage I could get nothing to work. Tried tutor support. 
  I tried to create a seperate app for cart, in line with boutique ado. Created a branch with copy of original main data.
  But once the code udpated, still the 500 Server Error
  Tutor support: helped identify some code I was missing and understnad the webhook and what it was looking for as now causing duplicate orders in the DB

This has helped me to understand that I wasn't handling the time slot field correctly. <br>
Have decided to have as a user input field (similar to user selecting quantities in B Ado)
And add that to the order. <br>
1st step, Find and remove all references across the app to time_slot <br>
Local environment, no issue. Still duplicates in DB, But at this point need to go back and fix up form data that webhook is checking for. <br>
Push to live and check<br>
Still get 500 error<br>

  8. Manually compared my data to b ado. Wasn't saving the order correctly, but still 500 issue. Duplicate Issue Resolved.
  9. Tried adding quantities, updating contexts and views. Still 500 Server Error
  10. Reverting to a previous commit and started again. Revert to my original plan where cart and checkout in same app.
  11. Go through steps again.
  12. Still not resolved at this stage, after reverting and rebuilding a number of times. Contacting tutor support, asking on slack, researching through the interenet on differenct sites. Looking over my code many, many times. 
  13. Decided at this stage, so that I oculd move on with the project to revert again to a previous commit and at this stage ignored the wh handler checks, until time allowed and I could contact tutor support again
Order creates in DB OK, need to get checkout success working
Done and working without full WH handler functionality.
  14. When I got to adding in the User Profiles, starting getting the 500 server issue again. So knew at this tage not an issue with the checkout code
  15. Found info on a slack queastion that migrations may need to be posted to postgres seperately to what was done on gitpod.
  16. I also needed to reset my superuser
  17. Once new superuser and migration to postgres in place, 500 issue on profile app resolved.
  18. The went back and re- added all the required code to the checkout app for webhook handlers etc. And checked migrations all ok pn postgres
  19. Issue now resolved with checkout. Working as expected

- Footer added day before submission. To give better layout on full content pages. However for logout and empty cart pages, footer is floating up the page.
I have the code to fix the footer, but when this is applied to footer in base template results in footer fixing on top of content in some pages such as articles.
For this project and due to time issues, I have just added some margin on logout and empty cart pages so that footer shows in middle of page and doesn't hug the buttons.
If time allows, will come back to this

- Code on articles page for links to particular sevices needs to be udpated as it is repeating and not really adhering to DRY principles. Knowledge at time of writing the code didn't allow for me to refactor, and unfortunately time doesn't allow. Decided to link to a few services and then one link to see all services.
Could not use this code in a live site or site with many more services as would not be efficient or practical.



[Back to table of contents](#table-of-contents)

### Bugs

-  Images were causing issues. The no-image file would not display and if admin tried to add a service without an image, or edit the image field on a service,
the site gave a 500 server error. 
I removed the date fields on models, added order form and had to update the admin and was able to update order in admin
But on site itself, this then caused  issue with image when try to select service page. I decided to revert back to last commit and review step by step
  - added default of 0 to item total
  - checked names/fields
  - re added views, urls, forms, templates. Then applied migrations and added a signals file
  - After reverting back, I also removed the sqllite from the GITHUB, But this then cleared all my admin date.
  - I re created superuser, updated user data in admin and site name
  - Then got the image attrib error when try to access page on the site
  - Checkout html page displays ok
  - Bug is caused where there is no image associated with a service. If/else was not solving. Until resolved I ensured there was an image attached to each service.
  - Resolved: This but was eventually resolved in services by adding the image url field to the model, ensuring migrations applied and updating if/else in html pages

- Crispy forms showing as invalid template/no module
  - Checked all version. Then suddenly started working after running cmd python3 =m pip install django-crispy-forms==1.13.0
  - All ok. Checkout form displaying with fields

- Bug: Not adding to cart. 
  - Removed int in view. Made quanity field hidden on form, updated contexts.py then rendered as expected

- Bug: Can't get remove link to remove items from cart
To resolve: - Updated view function:- to get the cart items and pop out the item id
Then Added a form to html for the remove section. Bug resolved

- Bug: Checkout page wouldn't render. 
To resolve I set up a new booking page to use instead. Use to branch to test with same functionality etc as original checkout page
1. render simple page. Ok
2. Copy all of the checkout.html
Getting the same message. NoReverseMatch at /checkout/booking/
Reverse for 'checkout' with arguments '('',)' not found. 1 pattern(s) tried: ['checkout/$']
3. Revert and copy over sections at a time to test
4. Bug is related to crispy form fields. View for the form data in checkout needed to be updated so could be accessed in the template
RESOLVED.

- Bug: Payment error div for stripe not showing message.
	- Checked with a stripe error card number. Refreshed , left for a while. Now ok

- Bug/Error
  - Stripe WH, NOT CREATING PAYMENT SUCCESS Intent. Issue was that i had only one underscore before iexact

- A few times I would get an attribute error. But this was usually that I needed to apply migrations

- Text on the profile link on mobile nav menu dispaying different to others: Resolved, just needed to update the class.

- Bug: After updating css for footer and fixng image rendering/issue with service causing 500 error where no image, now have css not applied to footers and links. Also. Images in service detail npage not rendering. No-image.png renders when I remove and image. Update if statement for image to include id on the detail page.

-  Looking at footer again, it doesn't look well on some pages. Giving it more margin top, pushes it away but again when less content on page it floats in middle.
TRying to position fixed but then main content scrolls behind footer and user cannot see it. Set padding on content container and fix footer. This just give issues on the home parrallax sections. Added another parallax empty div and some margin. Footer not overlapping the buttons





#### Bug/issue not fully resolved

[Back to table of contents](#table-of-contents)

### Performance and accessibility Testing

#### Lighthouse testing

[Reports for Mobile]
[Reports for Desktop]

#### Accessibility


### Code Validation


When all feature, user story testing etc fully completed. Rerun though validators. Any changes would be noted here

[Back to table of contents](#table-of-contents)

[Link to README File]()