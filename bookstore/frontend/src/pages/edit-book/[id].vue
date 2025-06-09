<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" lg="6" md="8">
        <!-- Loading state -->
        <v-card v-if="fetchBookLoading">
          <v-card-text class="text-center py-8">
            <v-progress-circular color="primary" indeterminate size="64"></v-progress-circular>
            <div class="mt-4">Loading book data...</div>
          </v-card-text>
        </v-card>

        <!-- Main form card -->
        <v-card v-else-if="!fetchBookError">
          <v-card-title class="d-flex align-center">
            <v-icon class="me-2" icon="mdi-book-edit"></v-icon>
            Edit Book
          </v-card-title>

          <v-divider></v-divider>

          <v-card-text>
            <BookForm v-model="bookData" v-model:valid="valid" :loading="updateBookLoading" @submit="handleUpdateBook" />
          </v-card-text>

          <v-card-actions class="px-6 pb-6">
            <v-btn
              color="grey"
              variant="outlined"
              @click="goBack"
            >
              Cancel
            </v-btn>
            <v-spacer></v-spacer>
            <v-btn color="primary" :disabled="!valid || !hasChanges" :loading="updateBookLoading" @click="handleUpdateBook">
              Update Book
            </v-btn>
          </v-card-actions>
        </v-card>

        <!-- Error state -->
        <v-card v-else>
          <v-card-text class="text-center py-8">
            <v-icon class="mb-4" color="error" icon="mdi-alert-circle" size="64"></v-icon>
            <h3 class="text-h6 mb-2">Book Not Found</h3>
            <p class="text-body-2 mb-4">{{ fetchBookError }}</p>
            <v-btn color="primary" @click="goBack">
              Go Back
            </v-btn>
          </v-card-text>
        </v-card>

        <!-- Success/Error Messages -->
        <v-alert v-if="updateBookError" class="mt-4" closable @click:close="clearUpdateError" type="error">
          {{ updateBookError }}
        </v-alert>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
  import { storeToRefs } from 'pinia'
  import { computed, onMounted, ref, watch } from 'vue'
  import { useRoute, useRouter } from 'vue-router'
  import BookForm from '@/components/BookForm.vue'
  import { useBooksStore } from '@/stores/books'

  const router = useRouter()
  const route = useRoute()
  const booksStore = useBooksStore()

  // Get reactive state from store
  const {
    updateBookLoading,
    updateBookError,
    fetchBookLoading,
    fetchBookError,
    bookLoaded,
  } = storeToRefs(booksStore)

  const { updateBook, fetchBookById, clearUpdateError } = booksStore

  // Get book ID from route params
  const bookId = computed(() => route.params.id)

  // Form data
  const bookData = ref({
    title: '',
    author: '',
    price: 0,
    qty: 0,
  })

  // Store original data to detect changes
  const originalData = ref({})

  // Form validation
  const valid = ref(false)

  // Computed property to check if there are changes
  const hasChanges = computed(() => {
    return JSON.stringify(bookData.value) !== JSON.stringify(originalData.value)
  })

  // Watch for changes in currentBook from store
  watch(bookLoaded, (newBook) => {
    if (newBook) {
      const bookInfo = {
        title: newBook.title,
        author: newBook.author,
        price: newBook.price,
        qty: newBook.qty,
      }
      bookData.value = { ...bookInfo }
      originalData.value = { ...bookInfo }
    }
  }, { immediate: true })

  // Methods
  const handleUpdateBook = async () => {
    if (!valid.value || !hasChanges.value) return

    try {
      await updateBook(bookId.value, bookData.value)
      router.push('/')
    } catch (error) {
      console.error('Failed to update book:', error)
    }
  }

  const goBack = () => {
    router.push('/')
  }

  // Fetch book data on component mount
  onMounted(async () => {
    if (bookId.value) {
      try {
        await fetchBookById(bookId.value)
      } catch (error) {
        console.error('Failed to fetch book:', error)
      }
    } else {
      router.push('/')
    }
  })
</script>
