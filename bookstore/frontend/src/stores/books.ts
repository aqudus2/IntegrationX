import axios from 'axios'
import { defineStore } from 'pinia'

interface BookCreate {
  title: string
  author: string
  price: number
  qty: number
}

export const useBooksStore = defineStore('books', {
  state: () => ({
    bookLoaded: null,
    books: [],
    loading: false,
    error: '',
    addBookLoading: false,
    addBookError: '',
  }),

  getters: {
    booksCount: (state): number => state.books.length,
  },

  actions: {
    async fetchBooks () {
      this.loading = true
      this.error = ''

      try {
        const response = await axios.get('http://localhost:8000/get-books')
        this.books = response.data
      } catch (error: any) {
        this.error = 'Failed to fetch books'
        console.error('Error fetching books:', error)
      } finally {
        this.loading = false
      }
    },

    async fetchBookById (bookId: number) {
      this.loading = true
      this.error = ''

      try {
        const response = await axios.get('http://localhost:8000/get-book/' + bookId)
        this.bookLoaded = response.data
      } catch (error: any) {
        this.error = 'Failed to fetch books'
        console.error('Error fetching books:', error)
      } finally {
        this.loading = false
      }
    },

    async addBook (bookData: BookCreate) {
      this.addBookLoading = true
      this.addBookError = ''

      try {
        const response = await axios.post('http://127.0.0.1:8000/add_book', {
          title: bookData.title,
          author: bookData.author,
          price: Number(bookData.price),
          qty: Number(bookData.qty),
        })

        return response.data
      } catch (error: any) {
        this.addBookError = 'Failed to add book'
        console.error('Error adding book:', error)
        throw error
      } finally {
        this.addBookLoading = false
      }
    },

    async deleteBook (bookId: number) {
      this.loading = true
      this.error = ''
      try {
        await axios.post('http://127.0.0.1:8000/delete-book/' + bookId)
        this.books = this.books.filter(book => book.id !== bookId)
      } catch (error) {
        this.error = 'Failed to delete book'
        console.error('Error deleting book:', error)
      } finally {
        this.loading = false
      }
    },

    async updateBook (bookId: number, bookData: BookCreate) {
      this.loading = true
      this.error = ''
      try {
        const response = await axios.post('http://127.0.0.1:8000/update-book/' + bookId, bookData)
        // Update the book in the local state
        // const index = this.books.findIndex(book => book.id === bookId)
        // if (index !== -1) {
        //   this.books[index] = response.data
        // }
        // this.currentBook = response.data
        return response.data
      } catch (error) {
        this.error = 'Failed to update book'
        console.error('Error updating book:', error)
        throw error
      } finally {
        this.loading = false
      }
    },

  },
})
