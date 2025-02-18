<template>
  <div class="app_container">
    <router-view></router-view>
    <Navbar />
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue';
export default {
  name: 'App',
  components: {
    Navbar
  }
}
</script>

<style scoped>
.app_container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  background: linear-gradient(to bottom right, #f0f0f0, #ffffff);
}
</style>

