import './assets/main.css'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router' // Import the router
import Toast from "vue-toastification";
import "vue-toastification/dist/index.css";

// Create and configure the Vue Toastification options
const options= {
  // You can set your default options here
  position: "top-right",
  timeout: 2000,
  closeOnClick: true,
  pauseOnHover: true,
  draggable: true,
  draggablePercent: 0.6,
  showCloseButtonOnHover: false,
  hideProgressBar: false,
  closeButton: "button",
  icon: true,
  rtl: false
};

const app = createApp(App);

// Use the router and the toast notification library
app.use(router);
app.use(Toast, options);

app.mount('#app');
