<template>
  <div class = 'home_container'>
    <div class = 'home_title'>
      <input 
        v-model = 'title'
        placeholder = 'Enter your title'
        class = 'home_title_input'
        type = "text"
        @keyup.enter = "createTask"
      />
      <button class = 'home_title_button' @click = "createTask">
        Create
      </button>
    </div>

    <div class = 'home_tasks'>
      <div 
        v-for = 'task in tasks'
        :key = 'task.id'
        class = 'home_task'
      >
        <div class = 'home_task_title'>
          {{ task.title }}
        </div>
        <button class="complete-button" @click = "completeTask(task.id)">Выполнено</button>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'HomeView',
    data() {
      return {
        tasks: [],
        newTask: ''
      }
    },
    async mounted() {
      await this.fetchTasks()
    },
    methods: {
      async fetchTasks() {
        try {
          const tg_user = window.Telegram.WebApp.initDataUnsafe?.user
          const response = await fetch('https://shiny-halibut-wq6w7p7rw66hgr46-8000.app.github.dev/api/tasks/{$tg_user.id}')
          const data = await response.json()
          this.tasks = data

        } catch (error) {
          console.log(error)
        }
      },
      async completeTask(taskId) {
        try {
          const response = await fetch('https://shiny-halibut-wq6w7p7rw66hgr46-8000.app.github.dev/api/completed', {
            method: 'PATCH',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              id: taskId
            })
          })
          if (response.ok) {
            this.newTask = ''
            await this.fetchTasks()
          } else {
            console.log(response)
          }
        } catch (error) {
          console.log(error)
        }
      }
    }
  }
</script>
