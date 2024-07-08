<template>
  <div>
    <h2>Rate Your Experience</h2>
    <div v-if="currentQuestion">
      <p>{{ currentQuestion.text }}</p>
      <div class="rating">
        <span v-for="star in 5" :key="star"
              @click="setRating(star)"
              :class="{ active: star <= ratings[currentIndex] }">
          ★
        </span>
      </div>
      <button v-if="currentIndex > 0" @click="previousQuestion">Back</button>
      <button v-if="currentIndex < questions.length - 1" @click="nextQuestion">Next</button>
      <button v-else @click="submitFeedback">Submit</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      questions: [],
      ratings: [],
      currentIndex: 0
    };
  },
  computed: {
    currentQuestion() {
      return this.questions[this.currentIndex];
    }
  },
  methods: {
    async fetchQuestions() {
      try {
        const response = await fetch('http://localhost:8000/questions');
        const data = await response.json();
        this.questions = data;
        this.ratings = new Array(data.length).fill(0);
      } catch (error) {
        console.error('Error fetching questions:', error);
      }
    },
    setRating(star) {
      console.log("Setting rating for index", this.currentIndex, "to", star);
      this.ratings[this.currentIndex] = star;
    },
    nextQuestion() {
      if (this.currentIndex < this.questions.length - 1) {
        this.currentIndex++;
      }
    },
    previousQuestion() {
      if (this.currentIndex > 0) {
        this.currentIndex--;
      }
    },
    async submitFeedback() {
      if (this.ratings.includes(0)) {
        alert("Please rate all questions before submitting.");
        return;
      }
      try {
        const response = await fetch('http://localhost:8000/feedback/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            ratings: this.ratings.map((rating, index) => ({
              question_id: this.questions[index].id,
              score: rating
            }))
          })
        });

        if (response.ok) {
          alert("Thank you for your feedback!");
          this.$router.push('/view-feedback');
        } else {
          console.log(response);
          alert("Failed to submit feedback.");
        }
      } catch (error) {
        console.error('Error submitting feedback:', error);
        alert("Failed to submit feedback.");
      }
    }
  },
  mounted() {
    this.fetchQuestions();
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
