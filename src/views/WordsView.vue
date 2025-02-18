<template>
    <div id="webcrumbs">
        <div class="w-[400px] min-h-[600px] bg-[#483D8B] p-6 rounded-lg font-sans"> 
            <header class="mb-12"> 
                <h1 class="text-white text-2xl font-bold tracking-wider">FOCUSY</h1> 
            </header>
            <div class="space-y-4"> 
                <h2 class="text-white text-4xl font-bold mb-2">ЗАДАНИЕ 4</h2> 
                <h3 class="text-white text-2xl mb-8">Куда падает ударение</h3> 
            <div class="space-y-4">    
                <button class="w-full p-6 bg-white rounded-xl transition-all duration-300 hover:bg-gray-100 hover:shadow-lg active:scale-[0.98]"> 
                    <span class="text-2xl font-bold">{{tasks[currentTaskIndex].word}}</span> 
                </button> 
                <button class="w-full p-6 bg-white rounded-xl transition-all duration-300 hover:bg-gray-100 hover:shadow-lg active:scale-[0.98]"> 
                    <span class="text-2xl font-bold">щЕмит</span> 
                </button> 
            </div> 
        </div> 
        <footer class="absolute bottom-6 flex justify-between w-[352px]"> 
            <div class="text-white">Верно: 1</div> 
            <div class="text-white">2/36</div> 
            <div class="text-white">Неверно: 0</div> 
        </footer> 
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
            const theme = '9 – правописание корней'
            const response = await fetch(`https://supreme-halibut-xg6jw7w56rpfpv47-8000.app.github.dev/api/incomplete-tasks/${tg_user.id}/${theme}`);
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
        } else {
            this.tasks = [];
        }
        this.isFlipped = false;
        },
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
  #webcrumbs .absolute {
    position: absolute;
  }
  #webcrumbs .bottom-6 {
    bottom: 24px;
  }
  #webcrumbs .mb-12 {
    margin-bottom: 48px;
  }
  #webcrumbs .mb-2 {
    margin-bottom: 8px;
  }
  #webcrumbs .mb-8 {
    margin-bottom: 32px;
  }
  #webcrumbs .flex {
    display: flex;
  }
  #webcrumbs .min-h-\[600px\] {
    min-height: 600px;
  }
  #webcrumbs .w-\[352px\] {
    width: 352px;
  }
  #webcrumbs .w-\[400px\] {
    width: 400px;
  }
  #webcrumbs .w-full {
    width: 100%;
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
  #webcrumbs :is(.space-y-4 > :not([hidden]) ~ :not([hidden])) {
    --tw-space-y-reverse: 0;
    margin-bottom: calc(16px * var(--tw-space-y-reverse));
    margin-top: calc(16px * (1 - var(--tw-space-y-reverse)));
  }
  #webcrumbs .rounded-lg {
    border-radius: 24px;
  }
  #webcrumbs .rounded-xl {
    border-radius: 36px;
  }
  #webcrumbs .bg-\[\#483D8B\] {
    --tw-bg-opacity: 1;
    background-color: rgb(72 61 139 / var(--tw-bg-opacity));
  }
  #webcrumbs .bg-white {
    --tw-bg-opacity: 1;
    background-color: rgb(255 255 255 / var(--tw-bg-opacity));
  }
  #webcrumbs .p-6 {
    padding: 24px;
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
  #webcrumbs .text-4xl {
    font-size: 36px;
    line-height: 41.4px;
  }
  #webcrumbs .font-bold {
    font-weight: 700;
  }
  #webcrumbs .tracking-wider {
    letter-spacing: 0.05em;
  }
  #webcrumbs .text-white {
    --tw-text-opacity: 1;
    color: rgb(255 255 255 / var(--tw-text-opacity));
  }
  #webcrumbs .transition-all {
    transition-duration: 0.15s;
    transition-property: all;
    transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  }
  #webcrumbs .duration-300 {
    transition-duration: 0.3s;
  }
  #webcrumbs {
    font-family: Open Sans !important;
    font-size: 16px !important;
  }
  #webcrumbs .hover\:bg-gray-100:hover {
    --tw-bg-opacity: 1;
    background-color: rgb(243 244 246 / var(--tw-bg-opacity));
  }
  #webcrumbs .hover\:shadow-lg:hover {
    --tw-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1),
      0 4px 6px -4px rgba(0, 0, 0, 0.1);
    --tw-shadow-colored: 0 10px 15px -3px var(--tw-shadow-color),
      0 4px 6px -4px var(--tw-shadow-color);
    box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000),
      var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
  }
  #webcrumbs .active\:scale-\[0\.98\]:active {
    --tw-scale-x: 0.98;
    --tw-scale-y: 0.98;
    transform: translate(var(--tw-translate-x), var(--tw-translate-y))
      rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y))
      scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
  }
  
</style>