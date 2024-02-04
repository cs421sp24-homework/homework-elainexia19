import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'

const routerOptions = [
  { path: "/", component: "Login" },
  { path: "/signup", component: "Signup" },
  { path: "/home", component: "Home" },
  { path: "/create_event", component: "CreateEvent" },
  { path: "/code", component: "Code" }
]
const routes = routerOptions.map(route => {
  return {
      ...route,
      component: () =>
          import (`@/components/${route.component}.vue`)
  };
});
Vue.use(Router)

export default new Router({
  routes,
  mode: 'history'
})

// export default new Router({
//   routes: [
//     {
//       path: '/',
//       name: 'HelloWorld',
//       component: HelloWorld
//     }
//   ]
// })