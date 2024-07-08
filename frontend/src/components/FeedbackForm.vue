<template>
  <div class="parent">
    <h2 class="title">Rate Your Experience</h2>
    <div class="progress-bar">
      <div class="progress" :style="{ width: progressPercentage + '%' }"></div>
    </div>
    <div v-if="currentQuestion" class="content">
      <p class="questionText">{{ currentQuestion.text }}</p>
      <div class="rating">
        <span v-for="star in 5" :key="star"
              @click="setRating(star)"
              :class="{ active: star <= ratings[currentIndex] }">
          ★
        </span>
      </div>
      <p class="ratingText">
        {{ ratingDescriptions[ratings[currentIndex] - 1] || '' }}
      </p>
      <div class="buttons">
        <button :disabled="currentIndex === 0" @click="previousQuestion">Back</button>
        <button v-if="currentIndex < questions.length - 1" @click="nextQuestion">Next</button>
        <button v-else @click="submitFeedback">Submit</button>
      </div>
    </div>
  </div>
</template>

<script>
import { useToast } from "vue-toastification";

export default {
  data() {
    return {
      questions: [],
      ratings: [],
      currentIndex: 0,
      ratingDescriptions: ["Very dissatisfied", "Dissatisfied", "Neutral", "Satisfied", "Very satisfied"],
    };
  },
  computed: {
    currentQuestion() {
      return this.questions[this.currentIndex];
    },
    progressPercentage() {
      return ((this.currentIndex + 1) / this.questions.length) * 100;
    },
  },
  methods: {
    async fetchQuestions() {
      try {
        const response = await fetch("https://feedback-form-api-teal.vercel.app/questions");
        const data = await response.json();
        this.questions = data;
        this.ratings = new Array(data.length).fill(0);
      } catch (error) {
        console.error("Error fetching questions:", error);
      }
    },
    setRating(star) {
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
      const toast = useToast();
      if (this.ratings.includes(0)) {
        alert("Please rate all questions before submitting.");
        return;
      }
      try {
        const response = await fetch("https://feedback-form-api-teal.vercel.app/feedback/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            ratings: this.ratings.map((rating, index) => ({
              question_id: this.questions[index].id,
              score: rating,
            })),
          }),
        });

        if (response.ok) {
          toast.success("Thank you for your feedback!", {
              timeout: 2000
            });
          this.$router.push("/submitted-success");
        } else {
          console.log(response);
          toast.error("Failed to submit feedback.");
        }
      } catch (error) {
        console.error("Error submitting feedback:", error);
        toast.error("Failed to submit feedback.", {
          timeout: 2000
        });
      }
    },
  },
  mounted() {
    this.fetchQuestions();
  },
};
</script>

<style scoped>
.parent {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 600px;
  margin: 0 auto;
  height: 100vh;
}

.title {
  font-size: 50px;
  font-weight: bold;
  margin-bottom: 20px;
}

.progress-bar {
  width: 100%;
  background-color: #e0e0e0;
  border-radius: 5px;
  overflow: hidden;
  margin-bottom: 20px;
}

.progress {
  height: 10px;
  background-color: green;
  width: 0%;
  transition: width 0.3s;
}

.content {
  text-align: center;
}

.questionText {
  font-size: 30px;
  margin-bottom: 20px;
}

.rating {
  cursor: pointer;
  font-size: 50px;
  margin-bottom: 10px;
}

.rating span {
  cursor: pointer;
  font-size: 60px;
}

.rating span.active {
  color: gold;
}

.ratingText {
  font-size: 20px;
  margin-bottom: 20px;
}

.buttons {
  display: flex;
  justify-content: space-between;
  gap: 10px;
}

button {
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  background-color: green;
  color: white;
  font-size: 16px;
}

button:disabled {
  background-color: gray;
  cursor: not-allowed;
}

button:hover:enabled {
  background-color: darkgreen;
}
</style>
