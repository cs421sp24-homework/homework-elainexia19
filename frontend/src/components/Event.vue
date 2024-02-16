<!-- html部分 -->
<template>
<div class="content">
    <div class="header">
    <span class="left"><b>QYay!</b>, get connected through your live Q&A platform</span>
    <button class="back" @click="goback">&laquo; Exit Event</button>
    </div>
    <div class="welcome"><h1>Welcome to QYay!</h1></div>
    <div v-if="isUser == 'false'">
    <div><div class="info">
        Event: {{ event.name }}
        &nbsp;&nbsp;&nbsp;>>>&nbsp;&nbsp;&nbsp;
        Hosted by {{ organizer }}
        <br>
        <div v-if="event.description">Description: {{ event.description }}<br></div>
        {{ event.date }} {{ event.start_time }}-{{ event.end_time }}
        <h3>Post questions here for the organizer</h3>
    </div></div>
    <div class="login">
    <table class="questions">
        <div class="scroll-area">
        <div v-if="questions.length == 0" style="font-size: 0.9em; color: rgb(77, 77, 77);">
            No questions posted yet, submit a question to get started.
        </div>
        <tr class="elements" v-for="(q, index) in questions">
            <!-- <td>{{ index }}</td> -->
            <td class="vote">
                <span class="check" v-if="q[4]">
                    <i class='far fa-check-circle'/>
                    <span class="tooltip">Question has been answered</span>
                </span>
                <span class="num">{{ q[3] }}</span>
                <i @click="upvoteQuestion(q[0])" :id="q[0]" class='far fa-thumbs-up upvote'/>
            </td>
            <td class="question">{{ q[1] }}</td>  
        </tr>
        </div>
    </table>
    </div>
    <div class="typebox">
        <form @submit.prevent="postQuestion">
            <input 
                type="text"
                name="question"
                v-model="Form.question"
                placeholder="Post questions ..."
                required
                oninvalid="this.setCustomValidity('Question can\'t be empty')"
                oninput="this.setCustomValidity('')"
            >
            <input type="submit" name="submit" value="Post">
        </form>
        <!-- <button class="create" @click="createEvent"><b>Post</b></button> -->
    </div></div>
    <div v-if="isUser == 'true'">
    <div><div class="info">
        Event: {{ event.name }}
        &nbsp;&nbsp;&nbsp;>>>&nbsp;&nbsp;&nbsp;
        Hosted by {{ organizer }}
        <br>
        <div v-if="event.description">Description: {{ event.description }}<br></div>
        {{ event.date }} {{ event.start_time }}-{{ event.end_time }}
        <h3>Questions posted by participants</h3>
    </div></div>
    <div class="login">
    <table class="questions">
        <div class="scroll-area">
        <div v-if="questions.length == 0" style="font-size: 0.9em; color: rgb(77, 77, 77);">
            Participants have not posted any quesitons yet.
        </div>
        <tr class="elements" v-for="q in questions" :key="q[3]">
            <td class="vote">
                <!-- <i class='far fa-thumbs-up upvote'/> -->
                <span class="check" v-if="q[4]"><i @click="markQuestion(q[0], q[4])" class='far fa-check-circle'/></span>
                <span class="no-check" v-if="!q[4]"><i @click="markQuestion(q[0], q[4])" class='far fa-check-circle'/></span>
                <span class="num">{{ q[3] }}</span>
                <!-- <i class='far fa-thumbs-down downvote'/> -->
                <!-- <span class="vote-icons">
                    <i class='far fa-thumbs-up upvote'/>
                    <i class='far fa-thumbs-down downvote'/>
                </span> -->
            </td>
            <td class="question">{{ q[1] }}</td>
        </tr>
        </div>
    </table>
    </div></div>
</div>
</template>

<!-- js部分 -->
<script>
import axios from 'axios'
export default {
data () {
    return {
        organizer: null,
        questions: null,
        event: null,
        isUser: this.$route.query.organizer,
        // code: null,
        // question: null
        Form: {
            type: "question",
            code: this.$route.query.code,
            question: null
        },
        voteForm: {
            type: "vote",
            code: this.$route.query.code,
            question_id: null,
            isUpvote: true
        },
        markForm: {
            type: "mark",
            code: this.$route.query.code,
            question_id: null,
            isMarked: false
        }
        // settings: {
        //     suppressScrollY: false,
        //     suppressScrollX: true,
        //     wheelPropagation: false
        // }
    }
},
created () {
    const path = 'http://127.0.0.1:5000/event'
    axios.post(path, this.Form).then(res => {
        console.log(res)
        this.questions = res.data.questions
        this.organizer = res.data.organizer
        this.event = res.data.event
        // this.isUser = res.data.isUser
    }).catch(error => {
    console.error(error)
    })
},
methods: {
    postQuestion () {
      const path = 'http://127.0.0.1:5000/event'
      axios.post(path, this.Form).then(res => {
        console.log(res)
        this.Form.question = ''
        this.questions = res.data.questions
      }).catch(error => {
        console.error(error)
      })
    },
    upvoteQuestion (question_id) {
      const path = 'http://127.0.0.1:5000/event'
    //   console.log("question id:", question_id)
      const isActive = document.getElementById(question_id).classList.contains('far')
      this.voteForm.question_id = question_id
      this.voteForm.isUpvote = isActive
      if (isActive) {
        document.getElementById(question_id).classList.remove('far')
        document.getElementById(question_id).classList.add('fa-solid')
      } else {
        document.getElementById(question_id).classList.remove('fa-solid')
        document.getElementById(question_id).classList.add('far')
      }
      axios.post(path, this.voteForm).then(res => {
        console.log(res)
        this.questions = res.data.questions
      }).catch(error => {
        console.error(error)
      })
    },
    markQuestion (question_id, question_marked) {
      const path = 'http://127.0.0.1:5000/event'
      this.markForm.question_id = question_id
      this.markForm.isMarked = question_marked
      axios.post(path, this.markForm).then(res => {
        console.log(res)
        this.questions = res.data.questions
      }).catch(error => {
        console.error(error)
      })
    },
    goback () {
        if (this.isUser == 'true') {
            this.$router.replace({ path: "/home" })
        } else {
            this.$router.replace({ path: "/join" })
        }
    },
    // scrollHanle(evt) {
    //     console.log(evt)
    // }
}
}
</script>

<style>
.header {
    position: relative;
    margin-left: auto;
    margin-right: auto;
    /* width: 80%; */
    height: 55px;
    background-color: #3e92e6;
}

.left {
    position: absolute;
    left: 200px;
    font-size: 20px;
    line-height: 55px;
    color: white;
    text-align: center;
}

.back {
    position: absolute;
    line-height: 45px;
    right: 150px;
    font-size: 17px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    padding: 0px 16px;
    background-color: #f1f1f1;
    color: black;
    border: 5px solid #3e92e6;
}

.back:hover {
    background: #405BE0;
    color: white;
}

.login {
font-family: sans-serif;
display: flex;
justify-content: center;
align-items: center;
/* background-color: black; */
}

.welcome {
padding-top: 25px;
text-align: center;
font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif; 
}

.info {
position: relative;
width: 50%;
margin: auto;
text-align: center;
font-size: 1.3em;
line-height: 30px;
font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif; 
}

/* .title h3 {
margin-top: 60px;
} */

.questions {
width: 70%;
padding: 15px;
/* position: absolute; */
/* top: 50%; */
/* left: 50%; */
/* background: #191919; */
border: 3px solid rgb(219, 231, 239);
/* border-radius: 5px; */
list-style: none;
font-size: 1.1em;
border-collapse: collapse;
}

/* .questions td {
    border-bottom: 1px solid gray;
} */

.questions tr:nth-child(odd) {
  background-color: rgb(244, 247, 249);
}

.questions .question {
    padding: 6px;
}

.vote {
width: 100px;
position: relative;
text-align: center;
/* border-left: 3px solid #86A8FA; */
}

.vote .upvote {
position: absolute;
top: 8px;
right: 10px;
color: rgb(27, 190, 139);
font-size: 20px;
}

.vote .upvote:hover {
    cursor: pointer;
}

.vote .check {
position: absolute;
top: 3px;
left: 6px;
color: rgb(27, 190, 139);
font-size: 20px;
}

.vote .check .tooltip {
visibility: hidden;
width: 200px;
font-size: 14px;
background-color: rgba(29, 28, 28, 0.715);
color: #ffffffe7;
/* text-align: center; */
border-radius: 6px;
margin-top: 7px;
padding: 3px 0;
position: absolute;
z-index: 1;
top: -5px;
left: 110%;
}

.vote .check .tooltip::after {
content: "";
position: absolute;
top: 50%;
right: 100%;
margin-top: -5px;
border-width: 5px;
border-style: solid;
border-color: transparent rgba(29, 28, 28, 0.715) transparent transparent;
}

.vote .check:hover .tooltip {
    visibility: visible;
}

.vote .no-check {
position: absolute;
top: 3px;
left: 6px;
color: rgb(143, 143, 143);
font-size: 20px;
}

.scroll-area {
    /* margin-top: 20px; */
    overflow-y: scroll;
    height: 350px;
}

.typebox {
    width: 70%;
    margin-top: 50px;
    margin-left: auto;
    margin-right: auto;
}

.typebox input[type="text"] {
    border: 2px solid #3498db;
    padding: 5px;
    width: 90%;
    /* color: white; */
    border-radius: 5px;
    /* transition: 0.25s; */
    font-size: 1em;
}

.typebox input[type="text"]:focus {
    border: 2px solid #405BE0;
}

.typebox input[type="submit"] {
  background: none;
  text-align: center;
  width: 8.3%;
  border: 2px solid #405BE0;
  padding: 5px;
  /* margin-left: 15px; */
  font-size: 1em;
  /* color: white; */
  border-radius: 5px;
  transition: 0.2s;
  cursor: pointer;
}

.typebox input[type="submit"]:hover {
  background: #405BE0;
  color: white;
}
</style>
