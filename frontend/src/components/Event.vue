<!-- html部分 -->
<template>
<div class="content">
    <div class="header">
    <span class="left"><b>QYay!</b>, get connected through your live Q&A platform</span>
    <button class="back" @click="goback">&laquo; Exit Event</button>
    </div>
    <div class="welcome"><h1>Welcome to QYay!</h1></div>
    <div>
    <div class="info">
        Event: {{ event.name }}
        &nbsp;&nbsp;&nbsp;>>>&nbsp;&nbsp;&nbsp;
        Hosted by {{ organizer }}
        <br>
        <div v-if="event.description">Description: {{ event.description }}<br></div>
        {{ event.date }} {{ event.start_time }}-{{ event.end_time }}
        <h3>Post questions here for the organizer</h3>
    </div>
    </div>
    <div class="login">
    <table class="questions">
        <div class="scroll-area">
        <div v-if="questions.length == 0" style="font-size: 0.9em; color: rgb(77, 77, 77);">
            No questions posted yet, submit a question to get started.
        </div>
        <tr class="elements" v-for="q in questions" :key="q[3]">
            <td class="vote">
                <i class='far fa-thumbs-up upvote'/>
                <span class="num">{{ q[3] }}</span>
                <span class="check" v-if="q[4]"><i class='far fa-check-circle'/></span>
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
    <!-- <ul class="events">
        <li v-for="(event, index) in events" :key="event.id">
        {{ index+1 }} {{ event.name }} {{ event.description }} {{ event.date }} 
        {{ event.start_time }} {{ event.end_time }} {{ event.code }}
        </li>
    </ul> -->
    </div>
    <div class="typebox">
        <form @submit.prevent="postQuestion">
            <input 
                type="text"
                name="question"
                v-model="Form.question"
                placeholder="Send questions ..."
                required
                oninvalid="this.setCustomValidity('Question can\'t be empty')"
                oninput="this.setCustomValidity('')"
            >
            <input type="submit" name="submit" value="Send">
        </form>
        <!-- <button class="create" @click="createEvent"><b>Post</b></button> -->
    </div>
</div>
</template>

<!-- js部分 -->
<script>
import axios from 'axios'
// import vueCustomScrollbar from 'vue-custom-scrollbar'
// import "vue-custom-scrollbar/dist/vueScrollbar.css"
export default {
// components: {
//     vueCustomScrollbar
// },
data () {
    return {
        organizer: null,
        questions: null,
        event: null,
        // code: null,
        // question: null
        Form: {
            code: null,
            question: null
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
    this.Form.code = this.$route.query.code
    axios.post(path, this.Form).then(res => {
        console.log(res)
        this.questions = res.data.questions
        this.organizer = res.data.organizer
        this.event = res.data.event
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
    goback () {
        this.$router.replace({ path: "/join" })
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
    background-color: #3498db;
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
    border: 5px solid #3498db;
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
top: 5px;
left: 5px;
color: rgb(19, 170, 19);
}

.vote .check {
position: absolute;
top: 0;
right: 0;
color: rgb(19, 170, 19);
font-size: 20px;
}

/* .vote .vote-icons {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
} */

/* .vote .num {
    margin: auto;
} */

/* .question {
    padding-left: 10px;
} */

.scroll-area {
    /* margin-top: 20px; */
    overflow-y: scroll;
    height: 350px;
}

.link-text {
color: #86A8FA;
text-decoration: underline;
cursor: pointer;
margin-top: 10px;
}

.link-text:hover {
color: #2340CF;
}

.text-warning {
color: #EE3D34;
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
    border: 3px solid #405BE0;
}

.typebox input[type="submit"] {
  background: none;
  text-align: center;
  width: 8.4%;
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
