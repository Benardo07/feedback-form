<template>
    <div>
      <h1>Feedback Received</h1>
      <div v-for="feedback in feedbacks" :key="feedback.id">
        <p>Rating: <span v-for="n in feedback.rating" :key="n">★</span></p>
        <!-- Enhanced date formatting -->
        <p>Submitted on: {{ formatDate(feedback.created_at) }}</p>
      </div>

      <button @click="goToWriteFeedback">Write Feedback</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        feedbacks: []
      };
    },
    methods: {
        formatDate(date) {
        // Append 'Z' to indicate UTC if it's not already included
        const utcDate = new Date(date + (date.endsWith('Z') ? '' : 'Z'));
        return utcDate.toLocaleString('en-US', {
            weekday: 'long', // "Monday"
            year: 'numeric', // "2021"
            month: 'long', // "July"
            day: 'numeric', // "20"
            hour: '2-digit', // "02"
            minute: '2-digit', // "00"
            second: '2-digit' // "00"
        });
        },
        goToWriteFeedback() {
            this.$router.push('/');
        }
    },
    async created() {
      try {
        const response = await fetch('http://localhost:8000/feedback/');
        if (!response.ok) {
          throw new Error('Failed to fetch');
        }
        const data = await response.json();
        this.feedbacks = data;
      } catch (error) {
        alert('Failed to fetch feedback');
        console.error('Error fetching feedback:', error);
      }
    }
  };
  </script>
  