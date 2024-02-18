# QYay! App

## Tech Stack

This web app uses Flask for backend, Vue.js for frontend, and mysql for database.

## Running the app

First set up Vue.js [here](https://github.com/cs421sp24-homework/homework-elainexia19/tree/main/frontend)

The database is stored on google cloud, should be able to access directly. Alternatively, could set up local mysql database using the data.sql file.

To run the web app locally, run
``````
conda create --name qyay python=3.9 -y
conda activate qyay
pip install -r requirements.txt

cd backend
python server.py

``````
In a seperate terminal, run
``````
cd frontend
npm run dev
``````

Open [http://localhost:8080/](http://localhost:8080/) to view it in the browser.

## Features implemented
* Sign up for an account as an organizer, checks that the password satifies requirements, enables re-enter password for validation
* Login to the app with your account
* Create an event on the app with event name, description, and time, checks that the events created are not past-time
* Generate a unique invitation code for the created event with MD5 hash using event id as input
* View the events that the organizer created on user homepage
* Open the event as an organizer and view the questions posted by participants
* Mark the questions as answered as an organizer
* Use code to join event without signing in as a participant
* Post questions in the event as a participant and view questions submitted by others
* Upvote or unvote questions as a participant
* The event page will be displayed for inactive events with event information and questions, but does not support any actions, such as posting questions and upvoting

## Testing the app
### Testing the organizer
* Has events, account username: john, password: qq1111
    * Contains events that are past-time and pre-time
    * Would need to create a new event for testing live events
* Has events, but events have no questions, account username: amy, password: ww2222
* Doesn't have events, account username: hello, password: hello333

### Testing the participant
* Past event that has questions, event code: 101010
* Past event that doesn't have questions, event code: 901192
* Future event that doesn't have questions, event code: 98f137
* Current live event can be tested by creating a new event via user homepage

## Challenges
1. Encountered problems when implementing the "attendees upvote questions submitted by others" feature, took a while to come up with a solution to ensure an audience can only upvote a question once, and could unvote the question if already upvoted. Solved the problem by searching through the class list of the icon, if the class signaling that the question has been upvoted (making the icon solid), then the question can be identified as upvoted, and unvoted questions vice versa. The same logic was applied to the "organizers mark questions as answered" feature.
2. Encountered problems implementing live update for the event. At first I tried to look into WebSocket to create a live event, but it was too time consuming to integrate with my existing code. Eventually I implemented live update with the setInterval function in Vue, it fetches data every 2 seconds, this method solves the problem, but might cause bad connection sometimes, in which case I would need to refresh the page or restart the program.
3. Encountered problems with CSS styling, couldn't get the background color to fit the whole cell width.

## References
* [https://codeburst.io/full-stack-single-page-application-with-vue-js-and-flask-b1e036315532](https://codeburst.io/full-stack-single-page-application-with-vue-js-and-flask-b1e036315532)
* [https://cn.vuejs.org/guide/quick-start](https://cn.vuejs.org/guide/quick-start)
* [https://github.com/casreenath/vue-flask-login-app](https://github.com/casreenath/vue-flask-login-app)

Link to repository: [https://github.com/cs421sp24-homework/homework-elainexia19](https://github.com/cs421sp24-homework/homework-elainexia19)