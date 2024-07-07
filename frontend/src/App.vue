<template>
  <div id="app">
    <router-view></router-view> <!-- This element will display routed components -->
  </div>
</template>
<script>
import FeedbackForm from './components/FeedbackForm.vue';

export default {
  components: {
    FeedbackForm
  }
};
</script>
