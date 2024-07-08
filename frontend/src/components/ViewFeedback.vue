<template>
  <div>
    <h1>Feedback Received</h1>
    <div v-for="feedback in feedbacks" :key="feedback.id" class="feedback-box">
      <p><strong>Submitted on:</strong> {{ formatDate(feedback.created_at) }}</p>
      <div v-for="rating in feedback.ratings" :key="rating.id">
        <p  v-if="rating.question"><strong>{{ rating.question.text }}</strong></p>
        <p v-else>No question available</p>
        <p>Rating: <span v-for="n in rating.score" :key="n">★</span></p>
      </div>
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
      const utcDate = new Date(date + (date.endsWith('Z') ? '' : 'Z'));
      return utcDate.toLocaleString('en-US', {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
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

<style scoped>
.feedback-box {
  border: 1px solid #ddd;
  padding: 20px;
  color: black;
  margin: 20px 0;
  border-radius: 10px;
  background-color: #f9f9f9;
}

.feedback-box p {
  margin: 5px 0;
}

.rating span {
  color: gold;
  font-size: 20px;
}

button {
  margin-top: 20px;
  padding: 10px 20px;
  background-color: #007BFF;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>
