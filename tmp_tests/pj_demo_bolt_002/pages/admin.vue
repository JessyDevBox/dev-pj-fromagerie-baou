<template>
  <div>
    <h1 class="text-4xl font-bold mb-6">{{ $t('admin.title') }}</h1>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <div class="bg-white p-6 rounded-lg shadow">
        <h2 class="text-2xl font-bold mb-4">{{ $t('admin.content') }}</h2>
        <ContentList v-slot="{ list }">
          <div v-for="item in list" :key="item._id" class="mb-4">
            <h3 class="font-bold">{{ item.title }}</h3>
            <div class="flex space-x-2 mt-2">
              <button @click="editContent(item)" class="bg-blue-500 text-white px-3 py-1 rounded">
                {{ $t('admin.edit') }}
              </button>
              <button @click="deleteContent(item._id)" class="bg-red-500 text-white px-3 py-1 rounded">
                {{ $t('admin.delete') }}
              </button>
            </div>
          </div>
        </ContentList>
      </div>
    </div>
  </div>
</template>

<script setup>
const editContent = (item) => {
  // Handle content editing
  console.log('Editing content:', item)
}

const deleteContent = (id) => {
  // Handle content deletion
  console.log('Deleting content:', id)
}
</script>