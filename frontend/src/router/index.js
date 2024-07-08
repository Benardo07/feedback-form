import { createRouter, createWebHistory } from 'vue-router';
import FeedbackForm from '../components/FeedbackForm.vue';
import ViewFeedback from '../components/ViewFeedback.vue';
import SubmittedSuccess from "../components/SubmittedSuccess.vue"

const routes = [
  {
    path: '/',
    name: 'SubmitFeedback',
    component: FeedbackForm
  },
  {
    path: '/view-feedback',
    name: 'ViewFeedback',
    component: ViewFeedback
  },
  {
    path: '/submitted-success',
    name: 'SubmittedSuccess',
    component: SubmittedSuccess
  },
];

const router = createRouter({
  history: createWebHistory("/"),
  routes
});

export default router;
