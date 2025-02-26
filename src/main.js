import './assets/main.css'
import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import * as solidIcons from '@fortawesome/free-solid-svg-icons';
import * as regularIcons from '@fortawesome/free-regular-svg-icons';
import * as brandIcons from '@fortawesome/free-brands-svg-icons';


import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

for (const icon in solidIcons) {
    if (solidIcons[icon]?.iconName) {
      library.add(solidIcons[icon]);
    }
  }

  for (const icon in regularIcons) {
    if (regularIcons[icon]?.iconName) {
      library.add(regularIcons[icon]);
    }
  }

  for (const icon in brandIcons) {
    if (brandIcons[icon]?.iconName) {
      library.add(brandIcons[icon]);
    }
  }

const app = createApp(App)

app.component('font-awesome-icon', FontAwesomeIcon)

app.use(router)

app.mount('#app')

