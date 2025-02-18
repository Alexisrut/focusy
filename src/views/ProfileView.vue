<template>
  <div class="profile-container">
    <h1>Профиль</h1>
    <div class="profile-info">
      <p>Имя: {{ user.name }}</p>
      <p>Выполнено задач: {{ user.completedTasks }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user: {
        name: '',
        completedTasks: 0
      }
    }
  },
  async mounted() {
    await this.fetchProfile()
  },
  methods: {
    async fetchProfile() {
      try {
        const tg_user = window.Telegram.WebApp.initDataUnsafe?.user
        const response = await fetch('https://shiny-halibut-wq6w7p7rw66hgr46-8000.app.github.dev/api/main/{$tg_user.id}')
        const data = await response.json()
        this.user.name = tg_user.name
        this.user.completedTasks = data.completedTasks
      } catch (error) {
        console.log(error)
      }
    }
    
  }
}

</script>