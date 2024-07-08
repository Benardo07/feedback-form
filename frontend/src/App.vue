<template>
  <div id="app">
    <router-view></router-view> <!-- This element will display routed components -->
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
html, body {
  height: 100%;
  width: 100%;
  margin: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

#app {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
  padding: 20px; /* Add padding to prevent overflow */
  box-sizing: border-box;
}
</style>
