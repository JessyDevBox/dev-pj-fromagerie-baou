<template>
  <div>
    <h1 class="text-4xl font-bold mb-6">{{ $t('register.title') }}</h1>
    <form @submit.prevent="submitForm" class="max-w-lg">
      <div class="mb-4">
        <label class="block mb-2">{{ $t('register.username') }}</label>
        <input v-model="form.username" type="text" class="w-full p-2 border rounded" required>
      </div>
      <div class="mb-4">
        <label class="block mb-2">{{ $t('register.email') }}</label>
        <input v-model="form.email" type="email" class="w-full p-2 border rounded" required>
      </div>
      <div class="mb-4">
        <label class="block mb-2">{{ $t('register.password') }}</label>
        <input v-model="form.password" type="password" class="w-full p-2 border rounded" required>
      </div>
      <button type="submit" class="bg-green-500 text-white px-4 py-2 rounded">
        {{ $t('register.submit') }}
      </button>
    </form>
  </div>
</template>

<script setup>
const form = reactive({
  username: '',
  email: '',
  password: ''
})

const submitForm = () => {
  // Handle registration
  console.log('Registration submitted:', form)
}
</script>