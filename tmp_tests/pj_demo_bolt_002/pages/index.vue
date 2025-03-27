<template>
  <div>
    <h1 class="text-4xl font-bold mb-6">{{ $t('home.title') }}</h1>
    <ContentDoc :path="contentPath" />
  </div>
</template>

<script setup>
const { locale } = useI18n()
const contentPath = computed(() => {
  return locale.value === 'fr' ? 'content/fr/index' : 'content/index'
})
</script>