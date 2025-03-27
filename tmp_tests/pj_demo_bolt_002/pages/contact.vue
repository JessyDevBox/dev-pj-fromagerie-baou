<template>
  <div>
    <h1 class="text-4xl font-bold mb-6">{{ $t('contact.title') }}</h1>
    <form @submit.prevent="submitForm" class="max-w-lg">
      <div class="mb-4">
        <label class="block mb-2">{{ $t('contact.name') }}</label>
        <input v-model="form.name" type="text" class="w-full p-2 border rounded" required>
      </div>
      <div class="mb-4">
        <label class="block mb-2">{{ $t('contact.email') }}</label>
        <input v-model="form.email" type="email" class="w-full p-2 border rounded" required>
      </div>
      <div class="mb-4">
        <label class="block mb-2">{{ $t('contact.message') }}</label>
        <textarea v-model="form.message" class="w-full p-2 border rounded" rows="4" required></textarea>
      </div>
      <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded">
        {{ $t('contact.submit') }}
      </button>
    </form>
  </div>
</template>

<script setup>
const form = reactive({
  name: '',
  email: '',
  message: ''
})

const submitForm = () => {
  // Handle form submission
  console.log('Form submitted:', form)
}
</script>