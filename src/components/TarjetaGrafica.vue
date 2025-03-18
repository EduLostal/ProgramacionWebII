<script setup>
defineProps(['tarjeta', 'index', 'reducirStock', 'aumentarStock']);
</script>

<template>
  <li class="tarjeta">
    <strong>{{ tarjeta.nombre }}</strong> - Precio: ${{ tarjeta.precio }} - Stock: {{ tarjeta.stock }} - 
    <span :style="{ color: tarjeta.disponible ? 'green' : 'red' }">
      {{ tarjeta.disponible ? 'Disponible' : 'No disponible' }}
    </span>
    <br>
    <button @click="reducirStock(index)">Vender 1</button>
    <button @click="aumentarStock(index)">Añadir 1</button>
  </li>
</template>

<style scoped>
.tarjeta {
  background: #fff;
  padding: 15px;
  margin: 10px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
button {
  background: #007bff;
  color: white;
  border: none;
  padding: 5px 10px;
  cursor: pointer;
  border-radius: 5px;
  margin-right: 5px;
}
button:hover {
  background: #0056b3;
}
</style>
