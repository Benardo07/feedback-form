<template>
    <div>
      <h1>Submit Feedback</h1>
      <input type="number" v-model="rating" placeholder="Rate from 1 to 5" min="1" max="5" />
      <button @click="submitFeedback">Submit Feedback</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        rating: 1
      };
    },
    methods: {
      async submitFeedback() {
        try {
          await axios.post('http://localhost:8000/feedback/', { rating: this.rating });
          alert('Feedback submitted successfully');
          this.$router.push('/view-feedback');
        } catch (error) {
          alert('Failed to submit feedback');
          console.error(error);
        }
      }
    }
  };
  </script>
  