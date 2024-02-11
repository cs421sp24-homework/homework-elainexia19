<!-- html部分 -->
<template>
<div class="content">
    <div class="header">
    <span class="left"><b>QYay!</b>, get connected through your live Q&A platform</span>
    </div>
    <div class="welcome"><h1>Event Created!</h1></div>
    <div class="title">
        <p>Here is the code to invite others to join:</p>
        <p class="code">{{ $route.query.code }}</p>
        <button class="save" @click="homepage"><b>Saved Code</b></button>
    </div>
</div>
</template>

<!-- js部分 -->
<script>
export default {
    data () {
        return {
            error: null
        }
    },
    mounted() {
        this.fetchUsername()
    },
    methods: {
        async fetchUsername () {
            try{
                const path = 'http://127.0.0.1:5000/code'
                const res = await axios.get(path)
                this.username = res.data.username
                if (!this.username) {
                    this.$router.replace({ path: "/" })
                }
            } catch(error) {
                console.error(error)
            }
        },
        homepage () {
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

.title .code {
    font-size: 1.5em;
}

.save {
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

.save:hover {
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
