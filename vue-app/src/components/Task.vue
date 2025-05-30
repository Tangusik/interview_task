<template>
  <div
    class="flex items-center w-full md:w-96 px-4 py-3 mx-auto bg-white rounded-lg shadow hover:shadow-md transition-shadow"
  >
    <input
      type="checkbox"
      v-model="task.completed"
      @change="patchTask"
      class="h-5 w-5 text-blue-500 rounded focus:ring-blue-400 mr-4"
    />
    <div class="flex-grow">
      <span class="text-gray-800 text-gray-400">{{ task.title }}</span>
    </div>
    <button
      @click="deleteTask"
      class="text-gray-400 hover:text-red-500 transition"
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="h-5 w-5"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"
        />
      </svg>
    </button>
  </div>
</template>

<script>
import api from "../api/index.js";

export default {
  props: {
    task: {
      type: Object,
      required: true,
    },
  },

  data() {
    return {
      localTask: { ...this.task }, // Локальная копия задачи
      loading: false,
    };
  },

  methods: {
    async deleteTask() {
      this.$emit("delete", this.task.id);
      await api.delete(`tasks/${this.task.id}`);
    },
    async patchTask() {
      this.loading = true;
      try {
        let task = this.task;
        task = await api.patch(`tasks/${this.task.id}`, {
          completed: this.task.completed,
        });
        this.$emit("patch", this.task);
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<style scoped></style>
