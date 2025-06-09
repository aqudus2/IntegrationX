<template>
  <v-form ref="form" v-model="valid" @submit.prevent="handleSubmit">
    <v-row>
      <v-col cols="12">
        <v-text-field
          v-model="formData.title"
          label="Book Title"
          prepend-icon="mdi-book"
          required
          :rules="titleRules"
          variant="outlined"
        ></v-text-field>
      </v-col>

      <v-col cols="12">
        <v-text-field
          v-model="formData.author"
          label="Author"
          prepend-icon="mdi-account"
          :rules="authorRules"
          required
          variant="outlined"
        ></v-text-field>
      </v-col>

      <v-col cols="12" sm="6">
        <v-text-field
          v-model.number="formData.price"
          label="Price"
          prepend-icon="mdi-currency-usd"
          type="number"
          step="0.01"
          min="0"
          :rules="priceRules"
          required
          variant="outlined"
        ></v-text-field>
      </v-col>

      <v-col cols="12" sm="6">
        <v-text-field
          v-model.number="formData.qty"
          label="Quantity"
          prepend-icon="mdi-package-variant"
          type="number"
          min="0"
          :rules="qtyRules"
          required
          variant="outlined"
        ></v-text-field>
      </v-col>
    </v-row>
  </v-form>
</template>

<script setup>
  import { ref, computed, watch } from 'vue'

  // Props
  const props = defineProps({
    modelValue: {
      type: Object,
      default: () => ({
        title: '',
        author: '',
        price: 0,
        qty: 0,
      })
    },
    loading: {
      type: Boolean,
      default: false
    }
  })

  // Emits
  const emit = defineEmits(['update:modelValue', 'submit', 'update:valid'])

  // Form ref and validation
  const form = ref(null)
  const valid = ref(false)

  // Internal form data
  const formData = computed({
    get: () => props.modelValue,
    set: (value) => emit('update:modelValue', value)
  })

  // Watch valid state and emit to parent
  watch(valid, (newValid) => {
    emit('update:valid', newValid)
  }, { immediate: true })

  // Validation rules
  const titleRules = [
    v => !!v || 'Title is required',
    v => (v && v.length >= 2) || 'Title must be at least 2 characters',
  ]

  const authorRules = [
    v => !!v || 'Author is required',
    v => (v && v.length >= 2) || 'Author must be at least 2 characters',
  ]

  const priceRules = [
    v => (v !== null && v !== undefined && v !== '') || 'Price is required',
    v => v >= 0 || 'Price must be 0 or greater',
  ]

  const qtyRules = [
    v => (v !== null && v !== undefined && v !== '') || 'Quantity is required',
    v => v >= 0 || 'Quantity must be 0 or greater',
    v => Number.isInteger(Number(v)) || 'Quantity must be a whole number',
  ]

  // Methods
  const handleSubmit = () => {
    if (valid.value) {
      emit('submit', formData.value)
    }
  }

  // Expose form methods to parent
  const validate = () => {
    return form.value?.validate()
  }

  const reset = () => {
    form.value?.reset()
  }

  const resetValidation = () => {
    form.value?.resetValidation()
  }

  defineExpose({
    validate,
    reset,
    resetValidation,
    form
  })
</script>
