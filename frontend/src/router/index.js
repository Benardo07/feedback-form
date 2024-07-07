import { createRouter, createWebHistory } from 'vue-router';
import FeedbackForm from '../components/FeedbackForm.vue';
import ViewFeedback from '../components/ViewFeedback.vue';

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
  }
];

const router = createRouter({
  history: createWebHistory("/"),
  routes
});

export default router;
