<template>
    <div class="success-container">
      <h1>Feedback Submitted Successfully!</h1>
      <div class="button-container">
        <button @click="writeAnotherFeedback">Write Another Feedback</button>
         <button @click="viewAllFeedback">View All Feedback</button>
      </div>
      
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      writeAnotherFeedback() {
        this.$router.push('/');
      },
      viewAllFeedback() {
        this.$router.push('/view-feedback');
      }
    }
  };
  </script>
  
  <style scoped>
  .success-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    text-align: center;
  }

  .button-container{
    display: flex;
    align-items: center;
    justify-items: center;
    flex-direction: row;
    gap: 30px;
  }
  
  h1 {
    margin-bottom: 20px;
    font-weight: bold;
    font-size: 50px;
  }
  
  button {
    padding: 10px 20px;
    margin: 10px;
    background-color: green;
    color: white;
    border: none;
    border-radius: 10px;
    align-self: center;
    font-weight: bold;
    cursor: pointer;
    font-size: 16px;
  }
  
  button:hover {
    background-color: darkgreen;
  }
  </style>
  