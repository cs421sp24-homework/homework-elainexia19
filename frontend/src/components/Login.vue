<!-- html部分 -->
<template>
  <div class="content">
    <div class="header">
      <span class="left"><b>QYay!</b>, get connected through your live Q&A platform</span>
      <button class="back" @click="goback">&laquo; Back</button>
    </div>
    <div class="welcome"><h1>Welcome to QYay!</h1></div>
    <div class="login">
      <form class="box" @submit.prevent="postUserLogin">
        <h2>Login</h2>
        <input
          type="text"
          name="username"
          placeholder="Username"
          v-model="LoginForm.username"
          required
          oninvalid="this.setCustomValidity('Username is required')"
          oninput="this.setCustomValidity('')"
        />
        <input
          type="password"
          name="password"
          placeholder="Password"
          v-model="LoginForm.password"
          required
          oninvalid="this.setCustomValidity('Password is required')"
          oninput="this.setCustomValidity('')"
        />
        <input type="submit" name="login" value="Login" />
        <p class="text-warning" v-if="error">{{ error }}</p>
        <p class="link-text" @click="signup">No account? Sign up here!</p>
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
      LoginForm: {
        username: null,
        password: null
      },
      // test: null,
      error: null
    }
  },
  methods: {
    postUserLogin () {
      const path = 'http://127.0.0.1:5000/login'
      axios.post(path, this.LoginForm).then(res => {
        console.log(res)
        if (res.data.loggedin) {
          // this.test = "show"
          console.log("Login is validated")
          this.$router.replace({ path: "/home" })
        } else {
          this.error = res.data.msg
        }
      }).catch(error => {
        console.error(error)
      })
      
    },
    signup () {
      this.$router.replace({ path: "/signup" })
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

.alert {
  margin-top: 10px;
  color: red;
}
</style>
