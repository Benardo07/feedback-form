<template>
  <div class="parent">
    <h2 class="title">Rate Your Experience</h2>
    <!-- Loading indicator for fetching questions -->
    <div v-if="loadingQuestions" class="loader"></div>
    <div v-else>
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
    <!-- Loading indicator for submitting feedback -->
    <div v-if="loadingFeedback" class="overlay" >
      <div class="loader"></div>
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
      loadingQuestions: false,
      loadingFeedback: false
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
      this.loadingQuestions = true;
      try {
        const response = await fetch("https://feedback-form-api-teal.vercel.app/questions");
        const data = await response.json();
        this.questions = data;
        this.ratings = new Array(data.length).fill(0);
      } catch (error) {
        console.error("Error fetching questions:", error);
      }finally {
        this.loadingQuestions = false;
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
      this.loadingFeedback = true;
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
      }finally {
        this.loadingFeedback = false;
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

.overlay {
  position: fixed;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 50; /* Ensure it's above other content */
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

@media (max-width: 768px) {
  .title {
    font-size: 32px; /* Smaller font size on smaller screens */
  }

  .questionText {
    font-size: 24px; /* Smaller font size on smaller screens */
  }

  .rating {
    font-size: 35px; /* Smaller star rating on smaller screens */
  }

  .rating span {
    font-size: 35px; /* Keep consistent with .rating size */
  }

  .ratingText {
    font-size: 16px; /* Smaller description font size */
  }

  .buttons button {
    padding: 8px 16px; /* Smaller padding for buttons */
    font-size: 14px; /* Smaller font size for buttons */
  }

  .parent {
    width: 95%; /* Make the width responsive */
    padding: 10px; /* Add padding to avoid touching the screen edges */
  }

}
</style>
