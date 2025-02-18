<template>
  
  <div class="card-container">
    <div 
      v-if="currentTask"
      class="card"
      :class="{ 'flipped': isFlipped }"
      @touchstart="startDrag"
      @touchmove="duringDrag"
      @touchend="endDrag"
      @mousedown="startDrag"
      @mousemove="duringDrag"
      @mouseup="endDrag"
      @mouseleave="endDrag"
    >
      <!-- Front Side -->
      <div class="card-face card-front">
        <h2 class="word">{{ currentTask.task_word }}</h2>
        <div class="indicators">
          <div class="circle incorrect-circle">{{ currentTask.task_incorrect }}</div>
          <div class="circle correct-circle">{{ currentTask.task_correct }}</div>
        </div>
      </div>

      <!-- Back Side -->
      <div class="card-face card-back">
        <p class="explanation">{{ currentTask.task_explain }}</p>
      </div>
    </div>
    
    <div v-else class="empty-state">
      Все карточки пройдены! 🎉
    </div>
    
    <div class="controls">
      <button @click="undo" :disabled="index <= 0">↩ Undo</button>
      <button @click="redo" :disabled="index >= history.length - 1">Redo ↪</button>
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
          const theme = '9'
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

      startDrag(event) {
        this.isDragging = true;
        const clientX = event.touches?.[0]?.clientX || event.clientX;
        const clientY = event.touches?.[0]?.clientY || event.clientY;
        this.dragStart = { x: clientX, y: clientY };
        this.dragDelta = { x: 0, y: 0 };
      },

      duringDrag(event) {
        if (!this.isDragging) return;
        event.preventDefault();
        
        const clientX = event.touches?.[0]?.clientX || event.clientX;
        const clientY = event.touches?.[0]?.clientY || event.clientY;
        
        this.dragDelta = {
          x: clientX - this.dragStart.x,
          y: clientY - this.dragStart.y
        };
      },

      endDrag() {
        if (!this.isDragging) return;
        this.isDragging = false;

        // Horizontal swipe takes priority
        if (Math.abs(this.dragDelta.x) > Math.abs(this.dragDelta.y)) {
          if (this.dragDelta.x > 50) { // Swipe right
            this.handleSwipeRight();
          } else if (this.dragDelta.x < -50) { // Swipe left
            this.handleSwipeLeft();
          }
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

      handleSwipeLeft() {
        this.isFlipped = !this.isFlipped;
      }
    }
  };
</script>


<style scoped>
/* General Styling */
.card-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 15px;
  padding: 20px;
  min-height: 100vh;
  background: #fcfae6;
  color: #1a1a1a;
  font-family: "Arial", sans-serif;
}

/* Card */
.card {
  width: 320px;
  height: 200px;
  position: relative;
  border-radius: 20px;
  perspective: 1000px;
  cursor: pointer;
  transition: transform 0.5s ease;
}

.card.flipped {
  transform: rotateY(180deg);
}

/* Card Faces */
.card-face {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  border-radius: 20px;
  box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
  font-size: 20px;
  font-weight: bold;
}

/* Front Side */
.card-front {
  background: linear-gradient(45deg, #7242a5, #8c55c7);
  color: white;
}

/* Back Side */
.card-back {
  background: white;
  color: #1a1a1a;
  transform: rotateY(180deg);
  padding: 20px;
  font-size: 16px;
  font-weight: normal;
}

/* Indicators */
.indicators {
  display: flex;
  gap: 20px;
  margin-top: 10px;
}

.circle {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  font-weight: bold;
  border: 2px solid white;
}

.incorrect-circle {
  background: #ff6b6b;
}

.correct-circle {
  background: #4caf50;
}

/* Empty State */
.empty-state {
  font-size: 20px;
  font-weight: bold;
  color: #7242a5;
  text-align: center;
  margin-top: 20px;
}

/* Buttons */
.controls {
  display: flex;
  gap: 10px;
}

button {
  background: transparent;
  border: 2px solid #7242a5;
  color: #7242a5;
  font-size: 16px;
  padding: 10px 20px;
  border-radius: 15px;
  cursor: pointer;
  transition: all 0.3s ease;
}

button:hover {
  background: #7242a5;
  color: white;
}

button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
</style>
