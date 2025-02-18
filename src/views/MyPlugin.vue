<template>
  <div id="webcrumbs">
    <div class="w-[400px] bg-[#4A3B89] p-6 font-sans"> 
      <div class="text-white text-center"> 
        <h1 class="text-xl font-bold mb-2">FOCUSY</h1>
        <h2 class="text-4xl font-bold mb-2">ЗАДАНИЕ {{theme}}</h2> 
        <p class="text-xl mb-8">Выбери верную букву</p> 
      </div> 
      <div class="card-container">
        <div 
        v-if="currentTask"
        class="card"
        :class="{ 'flipped': isFlipped }"
        >
        <div class="card-face card-front">
          <div class="bg-[#F5F2E3] rounded-3xl p-8 min-h-[300px] shadow-lg mb-8 card_front card-face"> 
            <p class="text-center text-3xl font-bold tracking-wide black_text">{{ currentTask.task_word }}</p> 
          </div> 
        </div>
        <div class="card-face card-back">
          <div class="bg-[#F5F2E3] rounded-3xl p-8 min-h-[300px] shadow-lg mb-8 card_back card-face">
            <p class="explanation black_text">{{ currentTask.task_explain }}</p>
          </div>
        </div>
        </div>
      </div>
      <div class="flex justify-between px-12"> 
        <button class="w-16 h-16 bg-[#F5F2E3] rounded-full text-2xl font-bold hover:bg-white transition-colors duration-300 transform hover:scale-110 black_text" @click="handleSwipeLeft();">{{ currentTask.task_incorrect }}</button> 
        <button class="w-16 h-16 bg-[#F5F2E3] rounded-full text-2xl font-bold hover:bg-white transition-colors duration-300 transform hover:scale-110 black_text" @click="handleSwipeRight();">{{ currentTask.task_correct }}</button> 
      </div>
      
      <div class="absolute bottom-6 left-1/2 -translate-x-1/2 text-white text-sm">2/36</div> 
      <div class="flex justify-between mt-8"> 
        <p class="text-white">Верно: {{good}}</p> 
        <p class="text-white">Неверно: {{bad}}</p> 
      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios';
  function undo() {
    circles.value = clone(history[--index.value])
  }

  function redo() {
    circles.value = clone(history[++index.value])
  }
  import { ref, shallowReactive, toRaw } from 'vue'

  const history = shallowReactive([[]])
  export default {
    data() {
      return {
        tasks: [],
        currentTaskIndex: 0,
        good: 0,
        theme: '9 – правописание корней',
        bad: 0,
        isFlipped: false,
        dragStart: { x: 0, y: 0 },
        dragDelta: { x: 0, y: 0 },
        isDragging: false
      };
    },
    computed: {
      currentTask() {
        return this.tasks[this.currentTaskIndex];
      },
      tgId() {
        // Get from your state management (Vuex, composable, or prop)
        return this.$store.state.user.tg_id;
      }
    },
    async mounted() {
      await this.loadTasks();
    },
    methods: {
      async loadTasks() {
        try {
          const tg_user = window.Telegram.WebApp.initDataUnsafe?.user
          const response = await fetch(`https://supreme-halibut-xg6jw7w56rpfpv47-8000.app.github.dev/api/incomplete-tasks/${tg_user.id}/${this.theme}`);
          const data = await response.json()
          this.tasks = data;
        } catch (error) {
          const tg_user = window.Telegram.WebApp.initDataUnsafe?.user
          alert(`Error loading tasks for user ${tg_user.id}: ${error}`);
          console.error('Error loading tasks:', error);
        }
      },

      async markCompleted() {
        try {
          const tg_user = window.Telegram.WebApp.initDataUnsafe?.user
          await axios.post(`https://supreme-halibut-xg6jw7w56rpfpv47-8000.app.github.dev/api/mark_complete/${tg_user.id}/${this.currentTask.id}`);
        } catch (error) {
          console.error('Error marking task complete:', error);
        }
      },

      async handleSwipeRight() {
        await this.markCompleted();
        if (this.currentTaskIndex < this.tasks.length - 1) {
          this.currentTaskIndex++;
          this.good += 1
        } else {
          this.tasks = [];
        }
        this.isFlipped = false;
      },

      handleSwipeLeft() {
        this.bad += 1
        this.good -= 1
        this.isFlipped = !this.isFlipped;
      }
    }
  };
</script>

<style scoped>
  @import url(https://fonts.googleapis.com/css2?family=Lato&display=swap);
  
  @import url(https://fonts.googleapis.com/css2?family=Open+Sans&display=swap);
  
  /*! tailwindcss v3.4.11 | MIT License | https://tailwindcss.com*/
  *,
  :after,
  :before {
    border: 0 solid #e5e7eb;
    box-sizing: border-box;
  }
  :after,
  :before {
    --tw-content: "";
  }
  .card-container {
    perspective: 1000px;
    width: 100%;
    min-height: 300px;
    margin-bottom: 20px;
  }

  .card {
    width: 100%;
    height: 300px;
    position: relative;
    transform-style: preserve-3d;
    transition: transform 0.6s;
  }

  .card-face {
    position: absolute;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    width: 100%;
    height: 100%;
    backface-visibility: hidden;
    -webkit-backface-visibility: hidden; /* For Safari */
  }

  .card-front {
    transform: rotateY(0deg);
  }

  .card-back {
    transform: rotateY(180deg);
  }

  .card.flipped {
    transform: rotateY(180deg);
  }
  :host,
  html {
    line-height: 1.5;
    -webkit-text-size-adjust: 100%;
    font-family:
      Open Sans,
      ui-sans-serif,
      system-ui,
      sans-serif,
      Apple Color Emoji,
      Segoe UI Emoji,
      Segoe UI Symbol,
      Noto Color Emoji;
    font-feature-settings: normal;
    font-variation-settings: normal;
    -moz-tab-size: 4;
    tab-size: 4;
    -webkit-tap-highlight-color: transparent;
  }
  body {
    line-height: inherit;
    margin: 0;
  }
  hr {
    border-top-width: 1px;
    color: inherit;
    height: 0;
  }
  abbr:where([title]) {
    text-decoration: underline dotted;
  }
  h1,
  h2,
  h3,
  h4,
  h5,
  h6 {
    font-size: inherit;
    font-weight: inherit;
  }
  .black_text {
    color: black;
  }
  a {
    color: inherit;
    text-decoration: inherit;
  }
  b,
  strong {
    font-weight: bolder;
  }
  code,
  kbd,
  pre,
  samp {
    font-family:
      ui-monospace,
      SFMono-Regular,
      Menlo,
      Monaco,
      Consolas,
      Liberation Mono,
      Courier New,
      monospace;
    font-feature-settings: normal;
    font-size: 1em;
    font-variation-settings: normal;
  }
  small {
    font-size: 80%;
  }
  sub,
  sup {
    font-size: 75%;
    line-height: 0;
    position: relative;
    vertical-align: baseline;
  }
  sub {
    bottom: -0.25em;
  }
  sup {
    top: -0.5em;
  }
  table {
    border-collapse: collapse;
    border-color: inherit;
    text-indent: 0;
  }
  button,
  input,
  optgroup,
  select,
  textarea {
    color: inherit;
    font-family: inherit;
    font-feature-settings: inherit;
    font-size: 100%;
    font-variation-settings: inherit;
    font-weight: inherit;
    letter-spacing: inherit;
    line-height: inherit;
    margin: 0;
    padding: 0;
  }
  button,
  select {
    text-transform: none;
  }
  button,
  input:where([type="button"]),
  input:where([type="reset"]),
  input:where([type="submit"]) {
    -webkit-appearance: button;
    background-color: transparent;
    background-image: none;
  }
  :-moz-focusring {
    outline: auto;
  }
  :-moz-ui-invalid {
    box-shadow: none;
  }
  progress {
    vertical-align: baseline;
  }
  ::-webkit-inner-spin-button,
  ::-webkit-outer-spin-button {
    height: auto;
  }
  [type="search"] {
    -webkit-appearance: textfield;
    outline-offset: -2px;
  }
  ::-webkit-search-decoration {
    -webkit-appearance: none;
  }
  ::-webkit-file-upload-button {
    -webkit-appearance: button;
    font: inherit;
  }
  summary {
    display: list-item;
  }
  blockquote,
  dd,
  dl,
  figure,
  h1,
  h2,
  h3,
  h4,
  h5,
  h6,
  hr,
  p,
  pre {
    margin: 0;
  }
  fieldset {
    margin: 0;
  }
  fieldset,
  legend {
    padding: 0;
  }
  menu,
  ol,
  ul {
    list-style: none;
    margin: 0;
    padding: 0;
  }
  dialog {
    padding: 0;
  }
  textarea {
    resize: vertical;
  }
  input::placeholder,
  textarea::placeholder {
    color: #9ca3af;
    opacity: 1;
  }
  [role="button"],
  button {
    cursor: pointer;
  }
  :disabled {
    cursor: default;
  }
  audio,
  canvas,
  embed,
  iframe,
  img,
  object,
  svg,
  video {
    display: block;
    vertical-align: middle;
  }
  img,
  video {
    height: auto;
    max-width: 100%;
  }
  [hidden] {
    display: none;
  }
  *,
  :after,
  :before {
    --tw-border-spacing-x: 0;
    --tw-border-spacing-y: 0;
    --tw-translate-x: 0;
    --tw-translate-y: 0;
    --tw-rotate: 0;
    --tw-skew-x: 0;
    --tw-skew-y: 0;
    --tw-scale-x: 1;
    --tw-scale-y: 1;
    --tw-pan-x: ;
    --tw-pan-y: ;
    --tw-pinch-zoom: ;
    --tw-scroll-snap-strictness: proximity;
    --tw-gradient-from-position: ;
    --tw-gradient-via-position: ;
    --tw-gradient-to-position: ;
    --tw-ordinal: ;
    --tw-slashed-zero: ;
    --tw-numeric-figure: ;
    --tw-numeric-spacing: ;
    --tw-numeric-fraction: ;
    --tw-ring-inset: ;
    --tw-ring-offset-width: 0px;
    --tw-ring-offset-color: #fff;
    --tw-ring-color: rgba(59, 130, 246, 0.5);
    --tw-ring-offset-shadow: 0 0 #0000;
    --tw-ring-shadow: 0 0 #0000;
    --tw-shadow: 0 0 #0000;
    --tw-shadow-colored: 0 0 #0000;
    --tw-blur: ;
    --tw-brightness: ;
    --tw-contrast: ;
    --tw-grayscale: ;
    --tw-hue-rotate: ;
    --tw-invert: ;
    --tw-saturate: ;
    --tw-sepia: ;
    --tw-drop-shadow: ;
    --tw-backdrop-blur: ;
    --tw-backdrop-brightness: ;
    --tw-backdrop-contrast: ;
    --tw-backdrop-grayscale: ;
    --tw-backdrop-hue-rotate: ;
    --tw-backdrop-invert: ;
    --tw-backdrop-opacity: ;
    --tw-backdrop-saturate: ;
    --tw-backdrop-sepia: ;
    --tw-contain-size: ;
    --tw-contain-layout: ;
    --tw-contain-paint: ;
    --tw-contain-style: ;
  }
  ::backdrop {
    --tw-border-spacing-x: 0;
    --tw-border-spacing-y: 0;
    --tw-translate-x: 0;
    --tw-translate-y: 0;
    --tw-rotate: 0;
    --tw-skew-x: 0;
    --tw-skew-y: 0;
    --tw-scale-x: 1;
    --tw-scale-y: 1;
    --tw-pan-x: ;
    --tw-pan-y: ;
    --tw-pinch-zoom: ;
    --tw-scroll-snap-strictness: proximity;
    --tw-gradient-from-position: ;
    --tw-gradient-via-position: ;
    --tw-gradient-to-position: ;
    --tw-ordinal: ;
    --tw-slashed-zero: ;
    --tw-numeric-figure: ;
    --tw-numeric-spacing: ;
    --tw-numeric-fraction: ;
    --tw-ring-inset: ;
    --tw-ring-offset-width: 0px;
    --tw-ring-offset-color: #fff;
    --tw-ring-color: rgba(59, 130, 246, 0.5);
    --tw-ring-offset-shadow: 0 0 #0000;
    --tw-ring-shadow: 0 0 #0000;
    --tw-shadow: 0 0 #0000;
    --tw-shadow-colored: 0 0 #0000;
    --tw-blur: ;
    --tw-brightness: ;
    --tw-contrast: ;
    --tw-grayscale: ;
    --tw-hue-rotate: ;
    --tw-invert: ;
    --tw-saturate: ;
    --tw-sepia: ;
    --tw-drop-shadow: ;
    --tw-backdrop-blur: ;
    --tw-backdrop-brightness: ;
    --tw-backdrop-contrast: ;
    --tw-backdrop-grayscale: ;
    --tw-backdrop-hue-rotate: ;
    --tw-backdrop-invert: ;
    --tw-backdrop-opacity: ;
    --tw-backdrop-saturate: ;
    --tw-backdrop-sepia: ;
    --tw-contain-size: ;
    --tw-contain-layout: ;
    --tw-contain-paint: ;
    --tw-contain-style: ;
  }
  #webcrumbs {
    background-color: #4A3B89;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  #webcrumbs .absolute {
    position: absolute;
  }
  #webcrumbs .relative {
    position: relative;
  }
  #webcrumbs .bottom-6 {
    bottom: 24px;
  }
  #webcrumbs .left-1\/2 {
    left: 50%;
  }
  #webcrumbs .mb-2 {
    margin-bottom: 8px;
  }
  #webcrumbs .mb-8 {
    margin-bottom: 32px;
  }
  #webcrumbs .mt-8 {
    margin-top: 32px;
  }
  #webcrumbs .flex {
    display: flex;
  }
  #webcrumbs .h-16 {
    height: 80px;
  }
  #webcrumbs .min-h-\[300px\] {
    min-height: 300px;
  }
  #webcrumbs .min-h-\[640px\] {
    min-height: 640px;
  }
  #webcrumbs .w-16 {
    width: 80px;
  }
  #webcrumbs .w-\[400px\] {
    width: 400px;
  }
  #webcrumbs .-translate-x-1\/2 {
    --tw-translate-x: -50%;
  }
  #webcrumbs .-translate-x-1\/2,
  #webcrumbs .transform {
    transform: translate(var(--tw-translate-x), var(--tw-translate-y))
      rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y))
      scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
  }
  #webcrumbs .flex-row {
    flex-direction: row;
  }
  #webcrumbs .items-center {
    align-items: center;
  }
  #webcrumbs .justify-between {
    justify-content: space-between;
  }
  #webcrumbs .gap-4 {
    gap: 16px;
  }
  #webcrumbs .rounded-2xl {
    border-radius: 48px;
  }
  #webcrumbs .rounded-3xl {
    border-radius: 72px;
  }
  #webcrumbs .rounded-full {
    border-radius: 9999px;
  }
  #webcrumbs .bg-\[\#4A3B89\] {
    --tw-bg-opacity: 1;
    background-color: rgb(74 59 137 / var(--tw-bg-opacity));
  }
  #webcrumbs .bg-\[\#F5F2E3\] {
    --tw-bg-opacity: 1;
    background-color: rgb(245 242 227 / var(--tw-bg-opacity));
  }
  #webcrumbs .p-6 {
    padding: 24px;
  }
  #webcrumbs .p-8 {
    padding: 32px;
  }
  #webcrumbs .px-12 {
    padding-left: 48px;
    padding-right: 48px;
  }
  #webcrumbs .text-center {
    text-align: center;
  }
  #webcrumbs .font-sans {
    font-family:
      Open Sans,
      ui-sans-serif,
      system-ui,
      sans-serif,
      Apple Color Emoji,
      Segoe UI Emoji,
      Segoe UI Symbol,
      Noto Color Emoji;
  }
  #webcrumbs .text-2xl {
    font-size: 24px;
    line-height: 31.200000000000003px;
  }
  #webcrumbs .text-3xl {
    font-size: 30px;
    line-height: 36px;
  }
  #webcrumbs .text-4xl {
    font-size: 36px;
    line-height: 41.4px;
  }
  #webcrumbs .text-sm {
    font-size: 14px;
    line-height: 21px;
  }
  #webcrumbs .text-xl {
    font-size: 20px;
    line-height: 28px;
  }
  #webcrumbs .font-bold {
    font-weight: 700;
  }
  #webcrumbs .tracking-wide {
    letter-spacing: 0.025em;
  }
  #webcrumbs .text-white {
    --tw-text-opacity: 1;
    color: rgb(255 255 255 / var(--tw-text-opacity));
  }
  #webcrumbs .shadow-lg {
    --tw-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1),
      0 4px 6px -4px rgba(0, 0, 0, 0.1);
    --tw-shadow-colored: 0 10px 15px -3px var(--tw-shadow-color),
      0 4px 6px -4px var(--tw-shadow-color);
    box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000),
      var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
  }
  #webcrumbs .transition-colors {
    transition-duration: 0.15s;
    transition-property: color, background-color, border-color,
      text-decoration-color, fill, stroke;
    transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  }
  #webcrumbs .duration-300 {
    transition-duration: 0.3s;
  }
  #webcrumbs {
    font-family: Open Sans !important;
    font-size: 16px !important;
  }
  #webcrumbs .hover\:scale-110:hover {
    --tw-scale-x: 1.1;
    --tw-scale-y: 1.1;
    transform: translate(var(--tw-translate-x), var(--tw-translate-y))
      rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y))
      scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
  }
  #webcrumbs .hover\:bg-white:hover {
    --tw-bg-opacity: 1;
    background-color: rgb(255 255 255 / var(--tw-bg-opacity));
  }
  
</style>
