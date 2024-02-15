<!-- html部分 -->
<template>
  <div class="content">
    <div class="header">
      <span class="left"><b>QYay!</b>, get connected through your live Q&A platform</span>
      <button class="back" @click="login">&laquo; Back</button>
    </div>
    <div class="welcome"><h1>Welcome to Qyay!</h1></div>
    <div class="login">
      <form class="box" @submit.prevent="getUserSignup">
        <h2>Signup</h2>
        <!-- <p>Please enter username and password</p> -->
        <p class="hint">Username</p>
        <input
          type="text"
          name="username"
          placeholder="Please enter username"
          v-model="SignupForm.username"
          required
          oninvalid="this.setCustomValidity('Username is required')"
          oninput="this.setCustomValidity('')"
        />
        <p class="text-warning" v-if="usernameError">{{ usernameError }}</p>
        <!-- <p>Username is {{ LoginForm.username }}</p> -->
        <p class="hint">Password</p>
        <p class="hint-small">Password should be at least 6 characters long, 
          contain at least one digit and one letter.</p>
        <input
          type="password"
          name="password"
          placeholder="Please enter password"
          v-model="SignupForm.password"
          @input="validatePassword"
          required
          oninvalid="this.setCustomValidity('Password is required')"
          oninput="this.setCustomValidity('')"
        />
        <p class="text-warning" v-if="passwordError">{{ passwordError }}</p>
        <!-- <p>Password is {{ LoginForm.password }}</p> -->
        <p class="hint">Re-enter password</p>
        <input
          type="password"
          name="repassword"
          placeholder="Please verify password"
          v-model="SignupForm.repassword"
          @input="validateRePassword"
          required
          oninvalid="this.setCustomValidity('Password is required')"
          oninput="this.setCustomValidity('')"
        />
        <p class="text-warning" v-if="repasswordError">{{ repasswordError }}</p>
        <p class="hint">Email</p>
        <input
          type="email"
          name="email"
          placeholder="Please enter email (not required)"
          v-model="SignupForm.email"
        />
        <input type="submit" name="signup" value="Sign up"/>
        <p class="link-text" @click="login">Already have account? Login here!</p>
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
      SignupForm: {
        username: null,
        password: null,
        repassword: null,
        email: null
      },
      usernameError: '',
      passwordError: '',
      repasswordError: '',
      signedin: false
    }
  },
  mounted() {
    // Wait for 2 seconds using setTimeout
    setTimeout(() => {
      // Check if specific data condition is met
      if (this.signedin) {
        // Redirect to another page using the Vue Router
        this.$router.push('/');
      }
    }, 2000); // 2000 milliseconds = 2 seconds
  },
  methods: {
    getUserSignup () {
      this.error = [];
      const path = 'http://127.0.0.1:5000/signup'
      if (!this.passwordError && !this.repasswordError){
        axios.post(path, this.SignupForm).then(res => {
          this.usernameError = res.data.msg
          // this.signedin = res.data.signedin
          if (res.data.signedup == true) {
            this.$router.replace({ path: "/login" })
          }
        }).catch(error => {
          console.error(error)
        })
      }
    },
    validatePassword () {
      const lengthRegex = /.{4,}/
      const digitRegex = /\d/
      const letterRegex = /[a-zA-Z]/

      if (lengthRegex.test(this.SignupForm.password) && digitRegex.test(this.SignupForm.password) && letterRegex.test(this.SignupForm.password)) {
        this.passwordError = '';
      } else {
        this.passwordError = 'Invalid password'
      }
    },
    validateRePassword () {
      if (this.SignupForm.password == this.SignupForm.repassword) {
        this.repasswordError = '';
      } else {
        this.repasswordError = 'Password does not match'
      }
    },
    login () {
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
.box input[type="password"],
.box input[type="email"] {
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
.box input[type="password"]:focus,
.box input[type="email"]:focus {
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
  