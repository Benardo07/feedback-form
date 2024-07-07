<template>
    <div>
      <h2>Rate Your Experience</h2>
      <div class="rating">
        <span v-for="star in 5" :key="star" @click="setRating(star)" :class="{ active: star <= rating }">
          ★
        </span>
      </div>
      <button @click="submitFeedback">Submit</button>
      <!-- Navigation Button -->
      <button @click="goToViewFeedback">View Feedback</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        rating: 0,
      };
    },
    methods: {
      setRating(star) {
        this.rating = star;
      },
      async submitFeedback() {
        if (this.rating === 0) {
          alert("Please select a rating before submitting.");
          return;
        }
        try {
          const response = await fetch('http://localhost:8000/feedback/', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              rating: this.rating
            })
          });
  
          if (response.ok) {
            alert("Thank you for your feedback!");
            this.rating = 0; // Reset rating after submission
            this.goToViewFeedback(); // Optionally navigate automatically after submission
          } else {
            console.log(response)
            alert("Failed to submit feedback.");
          }
        } catch (error) {
          console.error('Error submitting feedback:', error);
          alert("Failed to submit feedback.");
        }
      },
      goToViewFeedback() {
        this.$router.push('/view-feedback');
      }
    }
  };
  </script>
  
  <style scoped>
  .rating span {
    cursor: pointer;
    font-size: 25px;
  }
  
  .rating span.active {
    color: gold;
  }
  </style>