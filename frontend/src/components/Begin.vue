<!-- html部分 -->
<template>
<div class="content">
    <div class="header">
    <span class="left"><b>QYay!</b>, get connected through your live Q&A platform</span>
    </div>
    <div class="welcome"><h1>Welcome to QYay!</h1></div>
    <div class="title">
        <p>Please select a service:<br><br></p>
        <button class="buttons" @click="login"><b>Login as event organizer</b></button>
        <button class="buttons" @click="join"><b>Join event as participant</b></button>
    </div>
</div>
</template>

<!-- js部分 -->
<script>
export default {
    methods: {
        login () {
            this.$router.replace({ path: "/login" })
        },
        join () {
            this.$router.replace({ path: "/join" })
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

.buttons {
    border: 0;
    background: none;
    margin: 30px 20px;
    /* display: block; */
    /* margin: auto; */
    text-align: center;
    border: 2px solid #405BE0;
    padding: 8px 30px;
    outline: none;
    /* color: white; */
    border-radius: 10px;
    transition: 0.25s;
    font-size: 1em;
    /* text-transform: uppercase; */
    font-weight: 500;
}

.buttons:hover {
    background: #405BE0;
    color: white;
}

</style>
