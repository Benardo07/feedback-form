<template>
  <div class="parent">
    <div class="title-container">
      <h1>Feedback Received</h1>
      <button @click="goToWriteFeedback">Write Feedback</button>
    </div>
    <div v-if="loadingFeedback" class="loader">
    </div>
    <div v-else class="feedback-container">
      <div v-for="(feedback, index) in feedbacks" :key="feedback.id" class="feedback-box">
        <p><strong class="highlight">Submitted on:</strong> {{ formatDate(feedback.created_at) }}</p>
        <div v-for="(rating, ratingIndex) in feedback.ratings" :key="rating.id" class="rating-item">
          <p v-if="rating.question"><strong>{{ ratingIndex + 1 }}. {{ rating.question.text }}</strong></p>
          <p v-else>No question available</p>
          <p>
            Rating: 
            <span v-for="n in 5" :key="n" class="star" :class="{ active: n <= rating.score }">★</span>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      feedbacks: [],
      loadingFeedback: false
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
      this.loadingFeedback = true;
      const response = await fetch('https://feedback-form-api-teal.vercel.app/feedback/');
      if (!response.ok) {
        throw new Error('Failed to fetch');
      }
      const data = await response.json();
      this.feedbacks = data;
    } catch (error) {
      alert('Failed to fetch feedback');
      console.error('Error fetching feedback:', error);
    }finally{
      this.loadingFeedback = false;
    }
  }
};
</script>

<style scoped>
.parent {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;

}

.loader {
  width: 50px;
  padding: 8px;
  aspect-ratio: 1;
  border-radius: 50%;
  background: #25b09b;
  --_m: 
    conic-gradient(#0000 10%,#000),
    linear-gradient(#000 0 0) content-box;
  -webkit-mask: var(--_m);
          mask: var(--_m);
  -webkit-mask-composite: source-out;
          mask-composite: subtract;
  animation: l3 1s infinite linear;
}
@keyframes l3 {to{transform: rotate(1turn)}}

.highlight{
  font-weight: bolder;
  color: #28a745;
  margin-right: 5px;
  font-size: 20px;
}

.title-container {
  display: flex;
  width: 80%;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
}

h1 {
  margin: 0;
  text-align: center;
  flex: 1;
  font-weight: bold;
  font-size: 50px;
}

.feedback-container {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap; /* Allow feedback boxes to wrap to the next line */
  gap: 20px;
  justify-content: center; /* Center the feedback boxes */
  margin-bottom: 20px;
  overflow-y: auto; /* Make the container scrollable if necessary */
  max-height: 80vh; /* Prevent overflow beyond viewport height */
  width: 100%; /* Ensure container takes full width */
}

.feedback-container::-webkit-scrollbar {
  display: none; /* Hide the scrollbar */
}

.feedback-container {
  -ms-overflow-style: none;  /* IE and Edge */
  scrollbar-width: none;  /* Firefox */
}

.feedback-box {
  border: 1px solid #ccc;
  padding: 20px;
  border-radius: 10px;
  background-color: #2c3e50;
  color: white;
  width: 400px; /* Fixed width for feedback box */
  box-sizing: border-box;
  margin: 10px; /* Add margin for spacing */
}

.feedback-box p {
  margin: 5px 0;
}

.rating-item {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.star {
  font-size: 20px;
  color: grey;
}

.star.active {
  color: gold;
}

button {
  padding: 10px 20px;
  background-color: #28a745;
  color: white;
  font-weight: bold;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  align-self: flex-end;
}

button:hover {
  background-color: #218838;
}

button:focus {
  outline: none;
}

@media (max-width: 768px) {
  h1{
    font-size: 32px; /* Smaller font size on smaller screens */
  }

  button{
    padding: 5px 10px;
    margin: 5px;
    font-size: 12px;
  }
  .title-container{
    flex-direction: column;
    gap:10px;
  }

  .feedback-box{
    width: 300px;
    padding: 10px;
    margin: 8px;
    font-size: 14px;
  }

}
</style>
