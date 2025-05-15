<script setup>
import './assets/styles.css';
import { ref, onMounted } from 'vue';
import TarjetaGrafica from './components/TarjetaGrafica.vue';

const url = 'http://localhost:5000/graphql';

const tarjetasGraficas = ref([]);

async function cargarProductos() {
  const respuesta = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      query: `query { productos { id nombre precio stock disponible } }`
    })
  });
  const datos = await respuesta.json();

  if (datos.data && datos.data.productos) {
    tarjetasGraficas.value = datos.data.productos;
  }
}

async function reducirStock(index) {
  const tarjeta = tarjetasGraficas.value[index];
  if (tarjeta.stock > 0) {
    const respuesta = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        query: `mutation { modificarStock(id: ${tarjeta.id}, cantidad: -1) { producto { id nombre precio stock disponible } } }`
      })
    });
    const datos = await respuesta.json();

    if (datos.data && datos.data.modificarStock && datos.data.modificarStock.producto) {
      tarjetasGraficas.value[index] = datos.data.modificarStock.producto;
    }
  }
}

async function aumentarStock(index) {
  const tarjeta = tarjetasGraficas.value[index];
  const respuesta = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      query: `mutation { modificarStock(id: ${tarjeta.id}, cantidad: 1) { producto { id nombre precio stock disponible } } }`
    })
  });
  const datos = await respuesta.json();

  if (datos.data && datos.data.modificarStock && datos.data.modificarStock.producto) {
    tarjetasGraficas.value[index] = datos.data.modificarStock.producto;
  }
}

onMounted(() => {
  cargarProductos();
});
</script>

<template>
  <div>
    <h1>Inventario de Tarjetas Gráficas</h1>
    <ul>
      <TarjetaGrafica 
        v-for="(tarjeta, index) in tarjetasGraficas" 
        :key="tarjeta.id" 
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
