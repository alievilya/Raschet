<template>
  <div id="app">
    <h1>Hello </h1>
    <hr>
    <list
    v-bind:massiv="massiv"
    />
  </div>
</template>

<script>
import list from '@/components/list'
export default {
  name: 'app',
  data() {
    return{
      massiv:[
        {id:1, title: 'perviy', completed: false},
        {id:2, title: 'vtoroy', completed: false},
        {id:3, title: 'tretiy', completed: false}
      ]
    }
  },
  components: {
    list
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
