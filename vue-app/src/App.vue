<template>
  <div class="flex flex-col text-center w-full mt-8">
    <h1 class="sm:text-3xl text-2xl font-medium title-font mb-4 text-gray-900">
      Задачи:
    </h1>
  </div>

  <div class="flex flex-col">
    <div v-if="loading">Загрузка...</div>
    <Task
      v-else
      v-for="task in tasks"
      :task="task"
      @delete="handleDelete"
      @patch="handlePatch"
    />
  </div>
  <TaskForm @task-added="handleTaskAdded" />
</template>

<script>
import api from "./api";
import Task from "./components/Task.vue";
import TaskForm from "./components/TaskForm.vue";

export default {
  components: {
    Task,
    TaskForm,
  },
  data() {
    return {
      tasks: [],
      loading: false,
    };
  },

  async created() {
    await this.loadTasks();
  },

  methods: {
    async loadTasks() {
      this.loading = true;
      try {
        const response = await api.get("tasks");
        this.tasks = response.data;
      } catch (error) {
      } finally {
        this.loading = false;
      }
    },
    handleDelete(taskId) {
      this.tasks = this.tasks.filter((task) => task.id !== taskId);
    },

    handlePatch(updatedTask) {
      const index = this.tasks.findIndex((t) => t.id === updatedTask.id);
      if (index !== -1) {
        this.tasks.splice(index, 1, updatedTask);
      }
    },

    handleTaskAdded(newTask) {
      this.tasks.push(newTask);
    },
  },
};
</script>

<style scoped></style>
