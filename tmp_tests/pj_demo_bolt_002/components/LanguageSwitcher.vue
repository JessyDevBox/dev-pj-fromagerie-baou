<template>
  <select v-model="locale" @change="switchLocale" class="bg-gray-700 text-white p-1 rounded">
    <option value="fr">Français</option>
    <option value="en">English</option>
  </select>
</template>

<script setup>
const { locale } = useI18n()
const switchLocalePath = useSwitchLocalePath()

const switchLocale = (event) => {
  navigateTo(switchLocalePath(event.target.value))
}
</script>