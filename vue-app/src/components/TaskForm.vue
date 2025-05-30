<template>
  <form @submit.prevent="addTask">
  <section class="text-gray-600 body-font">
  <div class="container px-5 py-8 mx-auto">
    <div class="flex flex-col text-center w-full mb-6">
      <h1 class="sm:text-3xl text-2xl font-medium title-font mb-4 text-gray-900">Добавить задачу:</h1>
    </div>
    <div class="flex lg:w-2/3 w-full sm:flex-row flex-col mx-auto px-8 sm:space-x-4 sm:space-y-0 space-y-4 sm:px-0 items-end">
      <div class="relative flex-grow w-full">
        <input type="text" v-model="newTask.title" required class="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-400 focus:border-indigo-500 focus:bg-transparent focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
      </div>
      <button type="submit" :disabled="isLoading" class="text-white bg-indigo-500 border-0 py-2 px-8 focus:outline-none hover:bg-indigo-600 rounded text-lg">Добавить задачу</button>
    </div>
  </div>
  </section>
  </form>

</template>

<script>
import api from "../api/index.js";
export default {
  data() {
    return {
      isLoading: false,
      newTask: {
        title: "",
        completed: false,
      },
    };
  },

  methods: {
    async addTask() {
      this.isLoading = true;
      try {
        let task = this.newTask;
        task = await api.post("tasks", task);

        this.$emit("task-added", task.data);
        this.newTask = {
          title: "",
          description: "",
          completed: false,
        };
      } finally {
        this.isLoading = false;
      }
    },
  },
};
</script>

<style scoped></style>
