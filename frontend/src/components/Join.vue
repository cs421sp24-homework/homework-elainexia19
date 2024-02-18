<!-- html部分 -->
<template>
<div class="content">
    <div class="header">
    <span class="left"><b>QYay!</b>, get connected through your live Q&A platform</span>
    <button class="back" @click="goback">&laquo; Back</button>
    </div>
    <div class="welcome"><h1>Welcome to QYay!</h1></div>
    <div class="title">
        <p>Please enter the 6-digit code to join:</p>
        <input
            type="text"
            placeholder="X X X X X X"
            v-model="code"
            required
        />
        <p class="text-warning" v-if="error">{{ error }}</p>
        <button class="join" @click="joinEvent"><b>Join Event</b></button>
        <p><br></p>
        <p class="link-text" @click="login">Already have account? Login here!</p>
    </div>
</div>
</template>

<!-- js部分 -->
<script>
import axios from 'axios'
export default {
    data: function () {
        return {
            code: null,
            error: null
        }
    },
    methods: {
        joinEvent () {
            const path = 'http://127.0.0.1:5000/join'
            axios.post(path, this.code).then(res => {
                console.log(res)
                if (res.data.valid) {
                    console.log("Event is validated")
                    // this.$router.replace({ path: "/event" })
                    this.$router.push({ path: '/event', query: { code: this.code, organizer: 'none' } })
                } else {
                    this.error = res.data.msg
                }
            }).catch(error => {
                console.error(error)
            })
        },
        login () {
            this.$router.replace({ path: "/login" })
        },
        goback () {
            this.$router.replace({ path: "/" })
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

.title input {
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
  width: 200px;
  outline: none;
  /* color: white; */
  border-radius: 15px;
  transition: 0.25s;
  font-size: 1em;
}

.title input:focus {
  width: 210px;
  border-color: #405BE0;
}

.join {
    border: 0;
    background: none;
    margin-top: 10px;
    /* display: block; */
    /* margin: auto; */
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

.join:hover {
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

</style>
    
    