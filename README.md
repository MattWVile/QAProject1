
Objective
The objective provided for this project is as follows:

To create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training.

More specifically, the following is required:

Functioning CRUD application created in Python
Functioning front-end to website using Flask
Trello board or equivalent
Relational database - must contain at least one one-to-many relationship
Clear documentation
Detailed risk assessment
Automated tests
Fully integrated into Github or other VCS

ERD

My idea was to make a website where a user can add reviews to games that have been added by other users so my first ERD looked like this.

<a href="https://ibb.co/mcTBGBt"><img src="https://i.ibb.co/RDbS9SP/ERD-07-07-2021.jpg" alt="ERD-07-07-2021" border="0"></a>

I then realised that the relationship between games and reviews was incorrect for what i was trying to achieve as I wanted each user to be able to add as many reviews they want to as many games as they want so updated my ERD to this.

<a href="https://ibb.co/wg6WyFN"><img src="https://i.ibb.co/02JMqRj/ERD-14-07-2021.jpg" alt="ERD-14-07-2021" border="0"></a><br /><a target='_blank' href='https://imgbb.com/'></a><br />

I then came to the realisation that having a users table was out of scope for this particular project as it would take too long to implement a user login, I also wouldnt be awarded extra marks for a login feature so decided it would be a better idea for me to spend time on other parts of the project and updated the ERD accordingly.

<a href="https://ibb.co/pZmbKZj"><img src="https://i.ibb.co/ftcqNtd/ERD-21-07-2021.jpg" alt="ERD-21-07-2021" border="0"></a><br /><a target='_blank' href='https://imgbb.com/'></a><br />

Each game has a title, a genre and a developer. Each review has a name(of the reviewer), the content of the review, the date the review was posted/updated and a game_id linking to a specific game in the game table. This way each game can have many reviews.

 CI Pipeline
 
 The image below represents what services and tools I have chosen for each stage of development. 
 
 <a href="https://ibb.co/XZRPLPt"><img src="https://i.ibb.co/7JmDCDK/Screenshot-2.png" alt="Screenshot-2" border="0"></a>
 
 Project tracking
 
 I used trello to track my progress of development throughout the development process. The image below is a screenshot of my board and the link to my board is [here](https://trello.com/b/8DT1sc66/qa-project-1)
 
 <a href="https://ibb.co/HFLqfF0"><img src="https://i.ibb.co/r7KHR7g/trello-Screenshot.png" alt="trello-Screenshot" border="0"></a>

Risk assessment

The images below are screenshots of my risk assessment. I came back to it many times to outline more potential risks and how I came around these risks. The updated risk assesment can be found [here](Risk_assessment_23072021.pdf)

<a href="https://ibb.co/3cZr4yg"><img src="https://i.ibb.co/BBMzcV0/Risk-assessment-screenshot-1.png" alt="Risk-assessment-screenshot-1" border="0"></a>
<a href="https://ibb.co/mHJjPL7"><img src="https://i.ibb.co/Jzn1SfP/Risk-assessment-Screenshot-2.png" alt="Risk-assessment-Screenshot-2" border="0"></a><br />

Testing 
I used pytest to run unit tests on almost all of my functions in my application and implemented jenkins to automatically run these tests. I achieved an overall coverage of 98% shown below.

<a href="https://ibb.co/SPgcmM1"><img src="https://i.ibb.co/s24C1ND/Screenshot-7.png" alt="Screenshot-7" border="0"></a><br /><a target='_blank' href='https://imgbb.com/'>image sharing</a><br />



