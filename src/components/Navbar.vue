<!--<template>
    <nav class = "navbar">
        <router-link to="/" class = "nav-link">Home</router-link>
        <router-link to="/profile" class = "nav-link active">Profile</router-link>
        <router-link to="/cards" class = "nav-link">Cards</router-link>
    </nav>
</template>



<style scoped>
    .navbar {
        width: 100%;
        display: flex;
        justify-content: space-around;
        background: #1e2c80;
        padding: 15px;
        bottom: 0;
        align-items: center;
        height: 60px;
        /* Для iOS/macOS-стиля можно добавить полупрозрачный эффект */
        backdrop-filter: blur(10px);
        border-top: 1px solid #ccc;
    }

    .nav-link {
        background: transparent;
        border: none;
        color: white;
        font-size: 16px;
        cursor: pointer;
    }

    .active {
        background: #4d3ca6;
        padding: 10px;
        border-radius: 10px;
    }
</style>-->

<template>
  <div id="webcrumbs">
    <div class="width_100 bg-[#4A3B89] rounded-lg p-4">
      <nav class="flex items-center justify-between relative">
        <!-- Rating Button -->
        <router-link 
          to="/rate" 
          custom
          v-slot="{ navigate, isActive }"
        >
          <button 
            class="relative group px-6 py-3 rounded-full hover:bg-white/10 transition-all duration-300 ease-in-out"
            @click="setActive(0, navigate)"
            :class="{ 'text-white': isActive }"
          >
            <span class="relative z-10 white_text">Рейтинг</span>
            <div class="absolute inset-0 bg-white/0 group-hover:bg-white/5 rounded-full transition-all duration-300"></div>
            <div 
              v-if="isActive"
              class="absolute -bottom-2 left-1/2 transform -translate-x-1/2 w-2 h-2 bg-white rounded-full transition-all duration-300"
            ></div>
          </button>
        </router-link>

        <!-- Home Button -->
        <router-link 
          to="/" 
          custom
          v-slot="{ navigate, isActive }"
        >
          <button 
            class="relative group px-6 py-3 rounded-full hover:bg-white/10 transition-all duration-300 ease-in-out"
            @click="setActive(1, navigate)"
            :class="{ 'text-white': isActive }"
          >
            <span class="relative z-10 white_text">Главная</span>
            <div class="absolute inset-0 bg-white/0 group-hover:bg-white/5 rounded-full transition-all duration-300"></div>
            <div 
              v-if="isActive"
              class="absolute -bottom-2 left-1/2 transform -translate-x-1/2 w-2 h-2 bg-white rounded-full transition-all duration-300"
            ></div>
          </button>
        </router-link>

        <!-- Stats Button -->
        <router-link 
          to="/stats" 
          custom
          v-slot="{ navigate, isActive }"
        >
          <button 
            class="relative group px-6 py-3 rounded-full hover:bg-white/10 transition-all duration-300 ease-in-out"
            @click="setActive(2, navigate)"
            :class="{ 'text-white': isActive }"
          >
            <span class="relative z-10 white_text">Статистика</span>
            <div class="absolute inset-0 bg-white/0 group-hover:bg-white/5 rounded-full transition-all duration-300"></div>
            <div 
              v-if="isActive"
              class="absolute -bottom-2 left-1/2 transform -translate-x-1/2 w-2 h-2 bg-white rounded-full transition-all duration-300"
            ></div>
          </button>
        </router-link>
      </nav>
    </div>
  </div>
</template>

<script>
export default {
    name: "Navbar",
    methods: {
        setActive(index, navigate) {
        navigate()
        this.activeIndex = index
        }
    },
    data() {
        return {
        activeIndex: 1 // Default to Главная
        }
    }
}
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
  .width_100{
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    text-align: center;
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
  .white_text {
    color: white;
    font-size: 23px;
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
  #webcrumbs .relative {
    position: relative;
  }
  #webcrumbs .inset-0 {
    inset: 0;
  }
  #webcrumbs .-bottom-2 {
    bottom: -6px;
  }
  #webcrumbs .left-1\/2 {
    left: 50%;
  }
  #webcrumbs .z-10 {
    z-index: 10;
  }
  #webcrumbs .flex {
    display: flex;
  }
  #webcrumbs .h-2 {
    height: 6px;
  }
  #webcrumbs .w-2 {
    width: 6px;
  }
  #webcrumbs .w-\[600px\] {
    width: 600px;
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
    gap: 12px;
  }
  #webcrumbs .rounded-full {
    border-radius: 9999px;
  }
  #webcrumbs .rounded-lg {
    border-radius: 24px;
  }
  #webcrumbs .bg-\[\#4A3B89\] {
    --tw-bg-opacity: 1;
    background-color: rgb(74 59 137 / var(--tw-bg-opacity));
  }
  #webcrumbs .bg-white {
    --tw-bg-opacity: 1;
    background-color: rgb(255 255 255 / var(--tw-bg-opacity));
  }
  #webcrumbs .bg-white\/0 {
    background-color: hsla(0, 0%, 100%, 0);
  }
  #webcrumbs .p-4 {
    padding: 12px;
  }
  #webcrumbs .px-6 {
    padding-left: 18px;
    padding-right: 18px;
  }
  #webcrumbs .py-3 {
    padding-bottom: 9px;
    padding-top: 9px;
  }
  #webcrumbs .transition-all {
    transition-duration: 0.15s;
    transition-property: all;
    transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  }
  #webcrumbs .duration-300 {
    transition-duration: 0.3s;
  }
  #webcrumbs .ease-in-out {
    transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  }
  #webcrumbs {
    font-family: Open Sans !important;
    font-size: 26px !important;
  }
  #webcrumbs .hover\:bg-white\/10:hover {
    background-color: hsla(0, 0%, 100%, 0.1);
  }
  #webcrumbs :is(.group:hover .group-hover\:bg-white\/5) {
    background-color: hsla(0, 0%, 100%, 0.05);
  }
  
</style>