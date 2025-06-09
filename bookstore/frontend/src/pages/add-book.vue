<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" lg="6" md="8">
        <v-card>
          <v-card-title class="d-flex align-center">
            <v-icon class="me-2" icon="mdi-book-plus"></v-icon>
            Add New Book
          </v-card-title>

          <v-divider></v-divider>

          <v-card-text>
            <BookForm
              v-model="bookData"
              v-model:valid="valid"
              @submit="handleAddBook"
            />
          </v-card-text>

          <v-card-actions class="px-6 pb-6">
            <v-btn
              color="grey"
              variant="outlined"
              @click="goBack"
            >
              Back
            </v-btn>
            <v-spacer></v-spacer>
            <v-btn color="primary" :disabled="!valid" :loading="addBookLoading" @click="handleAddBook">
              Add Book
            </v-btn>
          </v-card-actions>
        </v-card>

        <!-- Success/Error Messages -->
        <v-alert v-if="addBookError" class="mt-4" closable type="error">
          {{ addBookError }}
        </v-alert>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
  import { storeToRefs } from 'pinia'
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  import BookForm from '@/components/BookForm.vue'
  import { useBooksStore } from '@/stores/books'

  const router = useRouter()
  const booksStore = useBooksStore()

  // Get reactive state from store
  const { addBookLoading, addBookError } = storeToRefs(booksStore)
  const { addBook } = booksStore

  // Form data
  const bookData = ref({
    title: '',
    author: '',
    price: 0,
    qty: 0,
  })

  // Form validation
  const valid = ref(false)

  // Methods
  const handleAddBook = async () => {
    if (!valid.value) return

    try {
      await addBook(bookData.value)

      // Reset form on success
      bookData.value = {
        title: '',
        author: '',
        price: 0,
        qty: 0,
      }

      router.push('/')
    } catch (error) {
      console.error('Failed to add book:', error)
    }
  }

  const goBack = () => {
    router.push('/')
  }
</script>
