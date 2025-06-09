<template>
  <div>
    <v-row v-if="books.length === 0 && !loading">
      <v-col cols="12">
        <v-alert type="info">
          No books found. Click "Load Books" to fetch data or "Add Books" to create new ones.
        </v-alert>
      </v-col>
    </v-row>

    <v-row v-else>
      <v-col
        v-for="book in books"
        :key="book.id"
        cols="12"
        sm="6"
        md="4"
        lg="3"
      >
        <v-card class="h-100">
          <v-card-title>{{ book.title }}</v-card-title>
          <v-card-subtitle>by {{ book.author }}</v-card-subtitle>

          <v-card-text>
            <div class="text-h6 text-primary">${{ book.price }}</div>
            <div class="text-body-2">Quantity: {{ book.qty }}</div>
          </v-card-text>

          <v-card-actions>
            <v-btn
              color="primary"
              variant="text"
              size="small"
              @click="editBook(book.id)"
            >
              Edit
            </v-btn>

            <v-btn
              color="error"
              variant="text"
              size="small"
              :loading="loading"
              @click="$emit('delete-book', book.id)"
            >
              Delete
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script setup>
  import { useRouter } from 'vue-router'

  const router = useRouter()

  defineProps({
    books: {
      type: Array,
      default: () => [],
    },
    loading: {
      type: Boolean,
      default: false,
    },
  })

  defineEmits(['delete-book'])

  const editBook = (bookId) => {
    router.push('/edit-book/' + bookId)
  }
</script>
