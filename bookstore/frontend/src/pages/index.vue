<template>
  <v-app>
    <v-main>
      <v-container>
        <v-row>
          <v-col cols="12">
            <div class="d-flex gap-2 mb-4">
              <v-btn color="primary" :loading="loading" @click="fetchBooks">
                Load Books
              </v-btn>
              <v-btn class="ml-4" color="success" @click="goToAddBook">
                Add Books
              </v-btn>
            </div>

            <v-alert v-if="error" class="mb-4" closable type="error" @click:close="clearError">
              {{ error }}
            </v-alert>

            <v-progress-linear v-if="loading" class="mb-4" color="primary" indeterminate></v-progress-linear>

            <!-- Use the BooksList component -->
            <BooksList :books="books" @delete-book="handleDeleteBook" />
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
  import { storeToRefs } from 'pinia'
  import { onMounted } from 'vue'
  import { useRouter } from 'vue-router'
  import BooksList from '@/components/BooksList.vue'
  import { useBooksStore } from '@/stores/books'

  const router = useRouter()
  const booksStore = useBooksStore()
  const { books, loading, error } = storeToRefs(booksStore)
  const { fetchBooks, deleteBook } = booksStore

  const goToAddBook = () => {
    router.push('/add-book')
  }

  const handleDeleteBook = async (bookId) => {
    if (confirm('Are you sure you want to delete this book?')) {
      await deleteBook(bookId)
    }
  }

  onMounted(() => {
    fetchBooks()
  })
</script>
