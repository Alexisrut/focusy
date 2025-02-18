<template>
  <div class="container">
    <!-- Header -->
    <header class="header">
      <img src="../assets/octopus.png" alt="Logo" class="logo" />
      <h1 class="title">FOCUSY</h1>
      <div class="coins">
        <img src="../assets/coin.png" alt="Coins" class="coin-icon" />
        <span class="coin-text">{{coins}}</span>
      </div>
    </header>

    <!-- Tasks -->
    <div class="tasks">
      <div class="xp-circle">
        <span class="xp-text">{{ xp }}</span>
      </div>
      <button class="tasks-btn">ТВОИ ЗАДАЧИ</button>
      <div class="progress-bar">
        <div class="progress"></div>
      </div>
    </div>

    <!-- Subjects -->

      
    <transition name="expand">
      <section v-if="!isExpanded" class="subjects">
        <h2 class="subjects-title">ПРЕДМЕТЫ</h2>
        <div class="subject-card" @click="toggleExpand">
          <div class="subject-info">
            <h3 class="subject-title">РУССКИЙ ЯЗЫК</h3>
            <p class="subject-desc">Решай задания с 9 по 20 и получай очки опыта</p>
          </div>
          <div class="subject-icon"></div>
        </div>
        <p class="coming-soon">Скоро здесь появятся новые предметы</p>
      </section>
    </transition>

      <!-- Tasks List (Visible when expanded) -->
      <transition name="fade">
        <div v-if="isExpanded" class="subject-expanded">
          <button class="back-btn" @click="toggleExpand">⬅ Назад</button>
          <!-- Tasks List -->
          <transition-group name="fade" tag="div" class="tasks-list">
            <div v-for="theme in themes" :key="theme.name" class="task-card">
              <h3 class="task-title">{{ theme.name }}</h3>
            </div>
          </transition-group>
        </div>
      </transition>
  </div>
</template>

<script>
export default {
  name: "HomeView",
  data() {
    return {
      coins: 0,
      xp: 0,
      isExpanded: false,
      themes: [],
      selectedTask: null,
    };
  },
  methods: {
    async toggleExpand() {
      this.isExpanded = !this.isExpanded;
      if (this.isExpanded) {
        await this.fetchTasks();
      }
    },
    async fetchTasks() {
      try {
        const tg_user = window.Telegram.WebApp.initDataUnsafe?.user
        const response = await fetch(`https://supreme-halibut-xg6jw7w56rpfpv47-8000.app.github.dev/api/theme-tasks/${tg_user.id}`); // Change to your API endpoint
        const data = await response.json();
        this.tasks = data;
      } catch (error) {
        console.error("Error fetching tasks:", error);
      }
    },
    async mounted() {
    // Fetch initial data from backend
      try {
        const tg_user = window.Telegram.WebApp.initDataUnsafe?.user
        const response = await fetch(`https://supreme-halibut-xg6jw7w56rpfpv47-8000.app.github.dev/api/incomplete-tasks/${tg_user.id}`);
        const data = await response.json()
        
        this.coins = data.coins
        this.xp = data.xp
        //this.leaderboard = data.leaderboard
      } catch (error) {
        console.error('Error fetching data:', error)
      } finally {
        this.loading = false
      }
    },
    openTask(task) {
      this.selectedTask = task;
    },
    closeTask() {
      this.selectedTask = null;
    },
  },
};
</script>

<style scoped>
  /* General Layout */
  .container {
    padding: 20px;
    background: #f5f5e6;
    min-height: 100vh;
    animation: fadeIn 0.5s ease-in-out;
  }

  /* Header */
  .header {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .logo {
    width: 60px;
  }

  .title {
    font-size: 22px;
    font-weight: bold;
    color: #243a75;
  }

  .task-title {
    font-size: 12px;
    font-weight: bold;
    color: white;
  }

  .coins {
    display: flex;
    align-items: center;
    background: #243a75;
    color: white;
    padding: 5px 15px;
    border-radius: 20px;
  }

  .coin-icon {
    width: 18px;
    margin-right: 5px;
  }

  .coin-text {
    font-size: 18px;
    font-weight: bold;
  }

  /* Tasks Section */
  .tasks {
    background: #4636a3;
    padding: 15px;
    border-radius: 15px;
    text-align: center;
    color: white;
    margin-top: 20px;
    position: relative;
  }

  .tasks-btn {
    background: #8b6df1;
    padding: 12px;
    border: none;
    border-radius: 12px;
    color: white;
    font-weight: bold;
    cursor: pointer;
    width: 80%;
    margin-top: 40px;
    font-size: 16px;
  }

  /* Subjects */
  .subjects {
    background: #1e2c80;
    padding: 20px;
    border-radius: 15px;
    color: white;
    transition: height 0.5s ease-in-out;
    overflow: hidden;
  }

  .subject-card {
    background: white;
    color: #1e2c80;
    padding: 15px;
    border-radius: 15px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    cursor: pointer;
  }

  .subject-expanded {
    background: white;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
  }

  .back-btn {
    background: #4636a3;
    color: white;
    padding: 10px 15px;
    border-radius: 10px;
    cursor: pointer;
    border: none;
  }

  /* Task Cards */
  .task-card {
    background: #4636a3;
    color: #1e2c80;
    padding: 30px;
    margin-top: 10px;
    border-radius: 15px;
    cursor: pointer;
    transition: transform 0.3s;
  }

  .task-card:hover {
    transform: scale(1.05);
  }

  /* Task Modal */
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .modal {
    background: white;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
  }

  .modal-close {
    background: #4636a3;
    color: white;
    padding: 10px;
    border-radius: 10px;
    border: none;
    cursor: pointer;
  }

  /* Animations */
  @keyframes fadeIn {
    from {
      opacity: 0;
      transform: translateY(-10px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  .fade-enter-active,
  .fade-leave-active {
    transition: opacity 0.3s ease-in-out;
  }

  .fade-enter,
  .fade-leave-to {
    opacity: 0;
  }

  .expand-enter-active,
  .expand-leave-active {
    transition: all 0.5s ease-in-out;
  }

  .expand-enter,
  .expand-leave-to {
    opacity: 0;
    transform: scale(0.9);
  }

  .modal-fade-enter-active,
  .modal-fade-leave-active {
    transition: opacity 0.3s ease-in-out;
  }

  .modal-fade-enter,
  .modal-fade-leave-to {
    opacity: 0;
  }
</style>
<!-- <template>
  <div class="container">

    <header class="header">
      <div class="stats-container">
        <div class="coin-badge">
          <span class="value">{{ coins }}</span>
        </div>
        <div class="xp-badge">
          <span class="value">{{ xp }}</span> XP
        </div>
      </div>
      <div class="user-info">
        <span class="user-name">{{ user.name }}</span>
      </div>
    </header>


    <section class="subjects-section">
      <h2 class="section-title">ПРЕДМЕТЫ</h2>
      
      
      <div class="subject-card">
        <div class="subject-header">
          <h3 class="subject-title">Русский язык</h3>
          <span class="progress-text">Решай задания с 9 по 20 <br/> и получай очки опыта</span>
        </div>
        
        <div class="progress-bar">
          <div 
            class="progress-fill"
            :style="{ width: `${Progress}%` }"
          ></div>
        </div>

        <div class="tasks-grid">
          <button 
            v-for="task in russianTasks"
            :key="task.range"
            @click="startTask(task)"
            class="task-button"
          >
            Задания {{ task.range }}
          </button>
        </div>
      </div>

      
      <div class="coming-soon">
        Скоро здесь появятся новые предметы
      </div>
    </section>

    
    <section class="stats-section">
      <div class="leaderboard-card">
        <h3 class="stats-title">Главный рейтинг</h3>
        <div v-if="loading" class="loading">Загрузка...</div>
        <ul v-else class="leaderboard-list">
          <li v-for="(user, index) in leaderboard" :key="user.id" class="leaderboard-item">
            <span>{{ index + 1 }}. {{ user.name }}</span>
            <span>{{ user.xp }} XP</span>
          </li>
        </ul>
      </div>

      <div class="stats-card">
        <h3 class="stats-title">Статистика</h3>
        <div class="stats-details">
          <div>Решено заданий: {{ stats.completedTasks }}</div>
          <div>Правильных ответов: {{ stats.correctAnswers }}%</div>
          <div>Потрачено монет: {{ stats.spentCoins }}</div>
        </div>
      </div>
    </section>
  </div>
</template>
<style>
  .container {
    min-height: 100vh;
    background-color: #111827;
    color: white;
    padding: 1rem;
  }

  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2rem;
  }

  .stats-container {
    display: flex;
    gap: 1rem;
    align-items: center;
  }

  .coin-badge {
    background-color: #2563eb;
    padding: 0.5rem 1rem;
    border-radius: 0.5rem;
    font-weight: 600;
  }

  .xp-badge {
    background-color: #16a34a;
    padding: 0.5rem 1rem;
    border-radius: 0.5rem;
    font-weight: 600;
  }

  .user-info {
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }

  .user-avatar {
    width: 2.5rem;
    height: 2.5rem;
    border-radius: 50%;
  }

  .subjects-section {
    margin-bottom: 2rem;
  }

  .section-title {
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 1rem;
  }

  .subject-card {
    background-color: #1f2937;
    padding: 1rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
  }

  .subject-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
  }

  .subject-title {
    font-size: 1.25rem;
    font-weight: 600;
  }

  .progress-text {
    font-size: 0.875rem;
    color: #9ca3af;
  }

  .progress-bar {
    background-color: #374151;
    height: 0.5rem;
    border-radius: 0.25rem;
    margin-bottom: 1rem;
  }

  .progress-fill {
    background-color: #3b82f6;
    height: 100%;
    border-radius: 0.25rem;
    transition: width 0.3s ease;
  }

  .tasks-grid {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 0.5rem;
  }

  .task-button {
    background-color: #374151;
    padding: 0.5rem;
    border-radius: 0.25rem;
    border: none;
    color: white;
    cursor: pointer;
    transition: background-color 0.2s;
  }

  .task-button:hover {
    background-color: #4b5563;
  }

  .coming-soon {
    background-color: #1f2937;
    padding: 1rem;
    border-radius: 0.5rem;
    text-align: center;
    color: #9ca3af;
  }

  .stats-section {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }

  .leaderboard-card,
  .stats-card {
    background-color: #1f2937;
    padding: 1rem;
    border-radius: 0.5rem;
  }

  .stats-title {
    font-size: 1.25rem;
    font-weight: 600;
    margin-bottom: 1rem;
  }

  .leaderboard-list {
    list-style: none;
    padding: 0;
  }

  .leaderboard-item {
    display: flex;
    justify-content: space-between;
    padding: 0.5rem 0;
    border-bottom: 1px solid #374151;
  }

  .stats-details {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }

  .loading {
    text-align: center;
    color: #9ca3af;
  }

  .value {
    font-size: 1.25rem;
    font-weight: 700;
  }
</style>
-->

<style>
/* Add custom styles if needed */
body {
  background-color: #1f2937;
}
</style>