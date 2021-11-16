<template>
  <div class="logIn_user">
    <div class="container_logIn_user">
      <h2>Nuevo Hotel</h2>
      <form v-on:submit.prevent="createHotel">
        <input
          v-model="hotel.nombreHotel"
          type="text"
          placeholder="Nombre del hotel"
          required
        />
        <br />
        <input
          type="text"
          v-model="hotel.descripcion"
          placeholder="Descripción"
          required
        />
        <br />
        <input
          type="text"
          v-model="hotel.calificacion"
          placeholder="calificación"
          required
        />
        <br />
        <input
          type="text"
          v-model="hotel.precio"
          placeholder="precio"
          required
        />
        <br />
        <button v-on:click="noIsNumber" type="submit">Crear Hotel</button>
      </form>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import swal from "sweetalert";

export default {
  name: "Hotel",

  data: function() {
    return {
      hotel: {
        nombreHotel: "",
        descripcion: "",
        calificacion: "",
        precio: "",
      },
    };
  },
  methods: {
    createHotel: async function() {
      console.log("ENTRAAAA", this.hotel);
      try {
        let url = "https://hotel-despliegue.herokuapp.com/hotels/";
        let body = this.hotel;
        let config = { Headers: {} };

        let result = await axios.post(url, body, config);
        swal("OK", "Creado exitosamente", "success");

        this.$router.push("home");
        this.$emit("creationCompleted", result);
      } catch (error) {
        if (!this.noIsNumber) {
          console.log(error);
          swal("Error", "Intente nuevamente", "error");
        }
      }
    },

    noIsNumber: function() {
      if (isNaN(this.hotel.precio && this.hotel.calificacion)) {
        // si no es un numero
        swal("Error", "No es un número valido (escribir sin comas)", "error");
      }
    },
  },
  created: function() {},
};
</script>
<style>

.container_logIn_user {
  border: 1px solid #bdb8bc;
  width: 30%;
}

</style>
