<!-- html部分 -->
<template>
<div class="content">
    <div class="header">
    <span class="left"><b>QYay!</b>, get connected through your live Q&A platform</span>
    <button class="back" @click="goback">&laquo; Back</button>
    </div>
    <div class="welcome"><h1>Welcome to Qyay!</h1></div>
    <div class="login">
    <form class="box" @submit.prevent="getUserSignup">
        <h2>Create Event</h2>
        <p class="hint">Event Name</p>
        <input
        type="text"
        name="name"
        placeholder="Please enter name of event"
        v-model="EventForm.name"
        required
        oninvalid="this.setCustomValidity('Event name is required')"
        oninput="this.setCustomValidity('')"
        />
        <p class="hint">Event Description</p>
        <textarea
        name="name"
        placeholder="Please enter description for event"
        v-model="EventForm.description"
        />
        <p class="hint">Event Date</p>
        <input
        type="date"
        name="start_date"
        placeholder="mm-dd-yyyy"
        v-model="EventForm.date"
        :min="minDate"
        required
        oninvalid="this.setCustomValidity('Date is required')"
        oninput="this.setCustomValidity('')"
        />
        <p class="hint">Start Time</p>
        <input
        type="time"
        name="start_time"
        placeholder="Please enter start time"
        v-model="EventForm.start_time"
        :min="minStartTime"
        required
        oninvalid="this.setCustomValidity('Start time is invalid')"
        oninput="this.setCustomValidity('')"
        />
        <p class="hint">End Time</p>
        <input
        type="time"
        name="end_time"
        placeholder="Please enter end time"
        v-model="EventForm.end_time"
        :min="minEndTime"
        required
        oninvalid="this.setCustomValidity('End time is invalid')"
        oninput="this.setCustomValidity('')"
        />
        <p class="text-warning" v-if="timeError">{{ timeError }}</p>
        <input type="submit" name="create" value="Create"/>
    </form>
    </div>
</div>
</template>

<!-- js部分 -->
<script>
import axios from 'axios'
export default {
    data: function () {
        return {
            EventForm: {
                name: null,
                description: null,
                date: null,
                start_time: null,
                end_time: null
            },
            nameError: '',
            dateError: '',
            timeError: '',
            eventcreated: null
        }
    },
    mounted() {
        this.fetchUsername()
    },
    computed: {
        minDate() {
            const today = new Date().toISOString().split('T')[0]
            return today
        },
        minStartTime() {
            const now = new Date()
            const today = now.toISOString().split('T')[0]
            if (this.EventForm.date == today) {
                const hours = now.getHours().toString().padStart(2, '0')
                const minutes = now.getMinutes().toString().padStart(2, '0')
                // console.log(`${hours}:${minutes}`)
                return `${hours}:${minutes}`
            } else {
                return
            }
        },
        minEndTime() {
            return this.EventForm.start_time
        }
    },
    methods: {
        async fetchUsername () {
            try{
                const path = 'http://127.0.0.1:5000/create_event'
                const res = await axios.get(path)
                this.username = res.data.username
                if (!this.username) {
                this.$router.replace({ path: "/" })
                }
            } catch(error) {
                console.error(error)
            }
        },
        getUserSignup () {
            this.error = [];
            const path = 'http://127.0.0.1:5000/create_event'
            if (!this.dateError && !this.timeError){
                axios.post(path, this.EventForm).then(res => {
                    if (!this.timeError) {
                        this.$router.push({ path: '/code', query: { code: res.data.code } })
                    }
                }).catch(error => {
                    console.error(error)
                })
            }
        },
        goback () {
            this.$router.replace({ path: "/home" })
        }
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

.box {
width: 500px;
padding: 40px;
/* position: absolute; */
/* top: 50%; */
/* left: 50%; */
/* background: #191919; */
border: 2px solid #3498db;
border-radius: 10px;
text-align: center;
transition: 0.25s;
margin-top: 40px;
margin-bottom: 100px;
}

.box input[type="text"] {
  border: 0;
  background: none;
  display: block;
  margin-top: 10px;
  margin-bottom: 25px;
  margin-left: auto;
  margin-right: auto;
  text-align: center;
  border: 2px solid #3498db;
  padding: 12px 15px;
  width: 250px;
  outline: none;
  /* color: white; */
  border-radius: 15px;
  transition: 0.25s;
}

.box textarea {
border: 0;
background: none;
display: block;
margin-top: 10px;
margin-bottom: 25px;
margin-left: auto;
margin-right: auto;
/* text-align: center; */
border: 2px solid #3498db;
padding: 12px 15px;
width: 250px;
height: 65px;
outline: none;
/* color: white; */
border-radius: 15px;
transition: 0.25s;
}

.box input[type="date"],
.box input[type="time"] {
border: 0;
background: none;
display: block;
margin-top: 10px;
margin-bottom: 25px;
margin-left: auto;
margin-right: auto;
text-align: center;
border: 2px solid #3498db;
padding: 12px 15px;
width: 140px;
outline: none;
/* color: white; */
border-radius: 15px;
transition: 0.25s;
}

.box h2 {
/* color: white; */
text-transform: uppercase;
font-weight: 500;
}

.box input[type="text"]:focus,
.box textarea:focus {
  width: 270px;
  border-color: #405BE0;
}

.box input[type="date"]:focus,
.box input[type="time"]:focus {
width: 160px;
border-color: #405BE0;
}

.box input[type="submit"] {
border: 0;
background: none;
display: block;
margin: 40px auto;
text-align: center;
border: 2px solid #405BE0;
padding: 8px 30px;
outline: none;
/* color: white; */
border-radius: 15px;
transition: 0.25s;
cursor: pointer;
}

.box input[type="submit"]:hover {
background: #405BE0;
color: white;
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
font-size: 0.9em;
color: #EE3D34;
}

.alert {
margin-top: 10px;
color: red;
}

.hint {
margin: auto;
width: 300px;
font-size: 1em;
color: #888;
}
.hint-small {
margin: auto;
width: 300px;
font-size: 0.8em;
color: #9d9c9c;
}
</style>
