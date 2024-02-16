<!-- html部分 -->
<template>
  <div class="content">
    <div class="header">
      <span class="left"><b>QYay!</b>, get connected through your live Q&A platform</span>
      <button class="back" @click="goback">&laquo; Sign Out</button>
    </div>
    <div class="welcome"><h1>Welcome, {{ username }}!</h1></div>
    <div>
      <div class="title">
        Create an event to get started &rarr;
        <button class="create" @click="createEvent"><b>Create Event</b></button>
        <h2>My Events</h2>
      </div>
    </div>
    <div class="login">
      <table class="events">
        <tr>
          <th>No.</th>
          <th>Event</th>
          <th>Date</th>
          <th>Start Time</th>
          <th>End Time</th>
          <th>Code</th>
          <th>Action</th>
        </tr>
        <tr class="elements" v-for="(event, index) in events" :key="event.id">
          <td>{{ index + 1 }}</td>
          <td class="event-name">{{ event.name }}<span class="dscrp" v-if="event.description"><br>{{ event.description }}</span></td>
          <td>{{ event.date }}</td>
          <td>{{ event.start_time }}</td>
          <td>{{ event.end_time }}</td>
          <td>{{ event.code }}</td>
          <td><button class="open-event" @click="openEvent(event.event_id)" :id="event.event_id">Open</button></td>
        </tr>
      </table>
      <!-- <ul class="events">
        <li v-for="(event, index) in events" :key="event.id">
          {{ index+1 }} {{ event.name }} {{ event.description }} {{ event.date }} 
          {{ event.start_time }} {{ event.end_time }} {{ event.code }}
        </li>
      </ul> -->
    </div>
  </div>
</template>

<!-- js部分 -->
<script>
import axios from 'axios'
export default {
  data () {
    return {
      username: null,
      events: null
    }
  },
  mounted() {
    this.fetchUsername()
    this.fetchEvents()
  },
  methods: {
    async fetchUsername () {
      try{
        const path = 'http://127.0.0.1:5000/home'
        const res = await axios.get(path)
        this.username = res.data.username
        if (!this.username) {
          this.$router.replace({ path: "/" })
        }
      } catch(error) {
        console.error(error)
      }
    },
    async fetchEvents () {
      try{
          const path = 'http://127.0.0.1:5000/home'
          const res = await axios.get(path)
          this.events = res.data.events
      } catch(error) {
          console.error(error)
      }
    },
    createEvent () {
      this.$router.replace({ path: "/create_event" })
    },
    openEvent (event_id) {
      const path = 'http://127.0.0.1:5000/home'
      axios.post(path, event_id).then(res => {
        console.log(res)
        if (res.data.valid) {
            // this.test = "show"
            console.log("Event is validated")
            // this.$router.replace({ path: "/event" })
            this.$router.push({ path: '/event', query: { code: res.data.code, organizer: true } })
        } else {
            this.error = res.data.msg
        }
      }).catch(error => {
        console.error(error)
      })
    },
    goback () {
      this.$router.replace({ path: "/login" })
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

.title {
  position: relative;
  width: 50%;
  margin: 40px auto;
  text-align: center;
  font-size: 1.2em;
  font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif; 
}

.title h2 {
  margin-top: 60px;
}

.create {
  border: 0;
  background: none;
  /* display: block; */
  /* margin: auto; */
  margin-left: 20px;
  text-align: center;
  border: 2px solid #405BE0;
  padding: 8px 30px;
  outline: none;
  /* color: white; */
  border-radius: 10px;
  transition: 0.25s;
  text-transform: uppercase;
  font-weight: 500;
}

.create:hover {
  background: #405BE0;
  color: white;
}

.events {
  width: 70%;
  padding: 10px 25px;
  /* position: absolute; */
  /* top: 50%; */
  /* left: 50%; */
  /* background: #191919; */
  border: 4px solid rgb(199, 223, 245);
  /* border-radius: 5px; */
  list-style: none;
  font-size: 1.1em;
  border-collapse: collapse;
  line-height: 16px;
}

.events th {
  text-align: left;
  padding-left: 8px;
  height: 40px;
  background-color: rgb(199, 223, 245);
}

.events tr:nth-child(odd) {
  background-color: rgb(244, 247, 249);
}

.events td {
  padding: 12px 8px;
  /* background-color: rgb(236, 244, 250); */
  /* border-top: 3px solid rgb(190, 205, 244); */
}

/* .events .elements:hover {
  background: #3498db;
  color: white;
} */

.dscrp {
  font-size: 0.8em;
  color: #585c6d;
}

.event-name {
  width: 400px;
}

.open-event {
  border: 0;
  background: none;
  display: block;
  /* margin: 20px auto; */
  text-align: center;
  border: 2px solid #405BE0;
  padding: 3px 5px;
  outline: none;
  /* color: white; */
  font-size: 15px;
  border-radius: 5px;
  /* transition: 0.25s; */
  cursor: pointer;
}

.open-event:hover {
  background: #405BE0;
  color: white;
}

.box input[type="text"],
.box input[type="password"] {
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

.box h2 {
  /* color: white; */
  text-transform: uppercase;
  font-weight: 500;
}

.box input[type="text"]:focus,
.box input[type="password"]:focus {
  width: 300px;
  border-color: #405BE0;
}

.box input[type="submit"] {
  border: 0;
  background: none;
  display: block;
  margin: 20px auto;
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
</style>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<!-- <style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style> -->
