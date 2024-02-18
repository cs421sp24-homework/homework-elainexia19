<!-- html部分 -->
<template>
  <div>
    <span>{{ serverResponse }}</span>
    <!--这里使用{{}}来引用JavaScript中赋给this的值-->
    <button @click="getData">get data</button>
  </div>
</template>
<!-- js部分 -->
<script>
import axios from 'axios'
export default {
  data: function () {
    return {
      serverResponse: 'res_test'
    }
  },
  methods: {
    getData () {
      const path = 'http://127.0.0.1:5000/getMsg'
      axios.get(path).then(res => {
        var msg = res.data.msg
        this.serverResponse = msg
        alter('Success' + response.status + ',' + response.data + ',' + msg)
      }).catch(error => {
        console.error(error)
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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
</style>
