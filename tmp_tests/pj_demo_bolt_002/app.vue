<template>
  <div>
    <header class="bg-gray-800 text-white p-4">
      <nav class="container mx-auto flex justify-between items-center">
        <NuxtLink to="/" class="text-xl font-bold">{{ $t('site.name') }}</NuxtLink>
        <div class="space-x-4">
          <NuxtLink to="/" class="hover:text-gray-300">{{ $t('nav.home') }}</NuxtLink>
          <NuxtLink to="/contact" class="hover:text-gray-300">{{ $t('nav.contact') }}</NuxtLink>
          <NuxtLink to="/register" class="hover:text-gray-300">{{ $t('nav.register') }}</NuxtLink>
          <NuxtLink to="/admin" class="hover:text-gray-300">{{ $t('nav.admin') }}</NuxtLink>
          <LanguageSwitcher />
        </div>
      </nav>
    </header>

    <main class="container mx-auto p-4">
      <NuxtPage />
    </main>

    <footer class="bg-gray-800 text-white p-4 mt-8">
      <div class="container mx-auto text-center">
        <p>&copy; 2024 {{ $t('site.name') }}</p>
      </div>
    </footer>
  </div>
</template>