# QYay! App

## Tech Stack

This web app uses Flask for backend, Vue.js for frontend, and mysql for database.

## Running the app

First set up Vue.js [here](https://github.com/cs421sp24-homework/homework-elainexia19/tree/main/frontend)

The database is stored on google cloud, should be able to access directly.

To run the web app locally, sun
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

Visualizations of the web app are in the imgs directory.

## Features implemented
* Sign up for an account as an organizer
* Login to the app with your account
* Create an event on the app and generate a unique invitation code, generated with MD5 hash
* View the events that you created
* Use code to join event without signing in as a participant
* Post questions in the event and view questions submitted by others

## Features added but not complete
* Participant can upvote questions submitted by others
* Organizer can mark questions as answered

## Testing the app
### Testing the organizer
* Has events, username: john, password: qq1111
* Has events, account username: amy, password: ww2222
* Doesn't have events, account username: hello, password: hello333

### Testing the participant
* Has questions, event code: 101010
* Doesn't have questions, event code: 809100

## Challenges
Encountered problems when implementing the "use code to join event" feature, especially in passing the event code from frontend to backend. At first tried to pass the code via query, but the backend server couldn't receive the query because of cross domain issues. Solved the problem by using axois.post.

## References
* [https://codeburst.io/full-stack-single-page-application-with-vue-js-and-flask-b1e036315532](https://codeburst.io/full-stack-single-page-application-with-vue-js-and-flask-b1e036315532)
* [https://cn.vuejs.org/guide/quick-start](https://cn.vuejs.org/guide/quick-start)
* [https://github.com/casreenath/vue-flask-login-app](https://github.com/casreenath/vue-flask-login-app)

Link to repository: [https://github.com/cs421sp24-homework/homework-elainexia19](https://github.com/cs421sp24-homework/homework-elainexia19)