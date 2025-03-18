<script setup>
import './assets/styles.css';
import { reactive } from 'vue';
import TarjetaGrafica from './components/TarjetaGrafica.vue';

const tarjetasGraficas = reactive([
  { nombre: "NVIDIA RTX 4090", precio: 1800, stock: 5, disponible: true },
  { nombre: "AMD Radeon RX 7900 XTX", precio: 999, stock: 0, disponible: false },
  { nombre: "NVIDIA RTX 4070 Ti", precio: 799, stock: 10, disponible: true },
  { nombre: "AMD Radeon RX 7800 XT", precio: 500, stock: 2, disponible: true },
  { nombre: "NVIDIA RTX 3060", precio: 299, stock: 0, disponible: false }
]);

const reducirStock = (index) => {
  if (tarjetasGraficas[index].stock > 0) {
    tarjetasGraficas[index].stock--;
    tarjetasGraficas[index].disponible = tarjetasGraficas[index].stock > 0;
  }
};

const aumentarStock = (index) => {
  tarjetasGraficas[index].stock++;
  tarjetasGraficas[index].disponible = true;
};
</script>

<template>
  <div>
    <h1>Inventario de Tarjetas Gráficas</h1>
    <ul>
      <TarjetaGrafica 
        v-for="(tarjeta, index) in tarjetasGraficas" 
        :key="index" 
        :tarjeta="tarjeta" 
        :index="index"
        :reducirStock="reducirStock"
        :aumentarStock="aumentarStock"
      />
    </ul>
  </div>
</template>

<style scoped>
h1 {
  text-align: center;
}
ul {
  list-style: none;
  padding: 0;
}
</style>
