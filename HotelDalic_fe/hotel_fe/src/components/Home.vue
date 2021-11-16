<template>
  <div class="container">
    <div class="description_main">
      <h1>Hoteles en el valle del cauca</h1>

      <div id="description_text">
        <p>
          Encuentra los mejores Hoteles en el Valle del Cauca en un solo lugar,
          tendrás las mejores opciones para un alojamiento increible, cómodo y
          placentero para disfrutar en familia de un estadía espectacular.
          Algunos con su estilo arquitectónico colonial, corredores amplios,
          habitaciones grandes, otros más contemporáneos y modernistas hacen de
          estos Hoteles la mejor alternativa para su paseo o vacaciones.
        </p>
      </div>
      <div id="principalHotel">
        <img
          class="shadow p-3 mb-5 bg-white rounded"
          src="../assets/principalhotel.jpg"
        />
      </div>
      <ul v-if="!is_superuser" class="benefits">
        <li>Hoteles exclusivos</li>
        <li>Precios comodos</li>
        <li>Reservación inmediata</li>
        <li>Cancelación gratuita</li>
      </ul>
    </div>

    <button
      v-if="is_superuser"
      v-on:click="loadhotel"
      class="button_custom btn btn-success"
    >
      <span class="icon_add">+</span>Crear Hotel
    </button>
    <router-view v-on:creationCompleted="creationCompleted"></router-view>
    <br />

    <div v-for="hotel in hotels" v-bind:key="hotel.id">
      <div class="crudHotel">
        <br />
        <br />
        <form v-if="is_superuser" v-on:submit.prevent="UpdateHotel">
          <input
            type="text"
            name="nombreHotel"
            @change="onChange($event)"
            v-model="hotel.nombreHotel"
            placeholder="Nombre del hotel"
          />
          <input
            type="text"
            name="descripcion"
            @change="onChange($event)"
            v-model="hotel.descripcion"
            placeholder="Descripción"
          />
          <input
            type="text"
            name="calificacion"
            @change="onChange($event)"
            v-model="hotel.calificacion"
            placeholder="calificación"
          />
          <input
            type="text"
            name="precio"
            @change="onChange($event)"
            v-model="hotel.precio"
            placeholder="precio"
          />
          <br />
          <br />
          <button
            v-if="is_superuser"
            v-on:click="updateHotel(hotel.id)"
            type="submit"
            class="btn btn-warning"
          >
            Actualizar Hotel
          </button>
          <button
            v-if="is_superuser"
            v-on:click="deleteHotel(hotel.id)"
            type="submit"
            class="btn btn-danger"
            id="button_delete"
          >
            Eliminar Hotel
          </button>
        </form>
      </div>
      <br />
      <div class="container_hotel">
        <div class="contain_imagen">
          <img
            class="imagen_hotel"
            src="../assets/Imagen_hotel.jpg"
            alt="Hotel"
          />
        </div>
        <div class="information">
          <div class="imagen_hearth">
            <img
              class="destacado"
              src="../assets/hearth.png"
              alt="hearth_destacado"
            />
          </div>

          <h4>
            <span class="title_hotel"> {{ hotel.nombreHotel }}</span>
          </h4>

          <p>
            <span class="description_hotel">{{ hotel.descripcion }}</span>
          </p>

          <div class="inline">
            <h6>
              <span class="star">
                <img src="../assets/star_calificationDalic.jpg" alt="Star"
              /></span>
              <span class="calification_hotel">{{ hotel.calificacion }}</span>
            </h6>
            <h5>
              <span class="price_hotel">${{ hotel.precio }}</span>
              <span class="day">/ noche</span>
            </h5>
          </div>
        </div>
      </div>
    </div>
    <div class="mapaHotel">
      <iframe
        id="map"
        src="https://www.google.com/maps/d/u/0/embed?mid=1VEahdsBpKBdTUq_9qtx0l_ybvMQEBOnb"
        width="800"
        height="480"
      ></iframe>
    </div>
  </div>
</template>

<script>
import jwt_decode from "jwt-decode";
import axios from "axios";

export default {
  name: "Home",

  data: function() {
    return {
      hotels: [],
      is_superuser: "",
      loaded: false,
      hotel: {
        nombreHotel: "",
        descripcion: "",
        calificacion: 0,
        precio: 0.0,
      },
    };
  },
  methods: {
    loadhotel: function() {
      this.$router.push({ name: "hotel" });
    },
    listHotels: function() {
      let url = "https://hotel-despliegue.herokuapp.com/hotels/";
      let config = { Headers: {} };
      axios
        .get(url, config)
        .then((response) => {
          console.log(response);
          this.hotels = response.data;
        })
        .catch((error) => {
          console.log(error);
          alert("Ocurrió algo inesperado, intente de nuevo más tarde");
        });
    },
    onChange(event) {
      this.hotel[event.target.name] = event.target.value;
    },
    deleteHotel: async function(id) {
      try {
        let url = "https://hotel-despliegue.herokuapp.com/hotel/" + id + "/";
        let config = { Headers: {} };
        await axios.delete(url, config);
        swal("OK", "Eliminado Hotel", "success");
        this.listHotels();
      } catch (error) {
        console.log(error);
        alert("ocurrio un error inesperado");
      }
    },

    updateHotel: async function(id) {
      console.log("Entra al put", this.hotel);
      try {
        let url = "https://hotel-despliegue.herokuapp.com/hotel/" + id + "/";
        let body = this.hotel;
        let config = { Headers: {} };
        let result = await axios.put(url, body, config);
        swal("OK", "Actualizado exitosamente", "success");
      } catch (error) {
        console.log(error);
        alert(
          "ocurrio un error inesperado o no es un número válido (sin comas)"
        );
      }
    },
    getData: async function() {
      if (
        localStorage.getItem("token_access") === null ||
        localStorage.getItem("token_refresh") === null
      ) {
        this.$emit("logOut");
        return;
      }
      await this.verifyToken();
      let token = localStorage.getItem("token_access");
      let userId = jwt_decode(token).user_id.toString();

      axios
        .get(`https://hotel-despliegue.herokuapp.com/user/${userId}/`, {
          headers: { Authorization: `Bearer ${token}` },
        })
        .then((result) => {
          this.is_superuser = result.data.is_superuser;

          this.loaded = true;
        })
        .catch(() => {
          this.$emit("logOut");
        });
    },
    verifyToken: function() {
      return axios
        .post(
          "https://hotel-despliegue.herokuapp.com/refresh/",
          { refresh: localStorage.getItem("token_refresh") },
          { headers: {} }
        )
        .then((result) => {
          localStorage.setItem("token_access", result.data.access);
        })
        .catch(() => {
          this.$emit("logOut");
        });
    },

    creationCompleted: function() {
      this.$router.push({ name: "home" });
      this.listHotels();
    },
  },
  created: function() {
    this.listHotels();
    this.getData();
  },
};
</script>
<style>
body .container {
  background: #ffff;
}

.container {
  height: 100%;
  width: 100%;
  font-family: Circular, -apple-system, BlinkMacSystemFont, Roboto,
    Helvetica Neue, sans-serif;
}

.description_main {
  text-align: center;
}

.description_main h1 {
  font-size: 32px;
  color: #283747;

  margin: 40px 0 0 0;
  padding-top: 30px;
  line-height: 90px;
  font-weight: 800;
}

/* It don't is Administrator*/
.description_main .benefits {
  display: inline-flex;
  display: flex;
  justify-content: center;
  align-items: center;
  justify-content: space-around;

  margin-left: 60px;
  margin-right: 83px;
}
.description_main .benefits li {
  list-style: none;
  border: 1px solid #ff385c;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  border-radius: 10px;
  padding: 5px;
}

/*Description general */
#description_text {
  display: inline-block;
  text-align: justify;
  width: 600px;
  margin: 40px;
}

/* Image main */
#principalHotel {
  margin-bottom: 100px;
}
#principalHotel img {
  border-radius: 10px;
}

/* Button create hotel */
.button_custom {
  float: right;
  margin-top: -80px;
  margin-right: 90px;
}

/* Icon for add hotel */
.icon_add {
  border-radius: 400px;
  border: 1px solid rgba(255, 255, 255, 0.5);
  color: rgba(255, 255, 255, 0.5);
  font-weight: bold;
  font-size: 20px;
  padding: 2px 9px;
  margin-right: 10px;
}

/* Get, update, delete of input */
.crudHotel {
  text-align: center;
}

#button_delete {
  margin-left: 30px;
}

/* container box of the whole hotel  */
.container_hotel {
  border-top: 1px solid rgb(207, 205, 205);
  border-bottom: 1px solid rgb(207, 205, 205);
  padding: 20px;
  height: 250px;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0 85px;
}
.container_hotel:hover {
  cursor: pointer;
}

/* Their information of Hotel */
.container_hotel .information {
  left: 2%;
  width: 67%;
  height: 70%;
}

.container_hotel .information .title_hotel {
  line-height: 20px;
  margin-top: 10px;
  margin-bottom: 15px;
  font-size: 18px;
  overflow: hidden;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  text-transform: uppercase;
}
.container_hotel .information .description_hotel {
  color: rgb(113, 113, 113);
  font-weight: 400;
  font-size: 15px;
  line-height: 18px;
}

/* star, price, day within of container hotel */
.inline img {
  width: 15px;
}
.inline .price_hotel {
  font-size: 18px;
  font-family: sans-serif, Arial, Helvetica;
}
.inline .day {
  font-weight: 300;
}

.container_hotel .information .inline .calification_hotel {
  font-size: 14px;
  margin-left: 5px;
}

.container_hotel .information .inline {
  display: inline-flex;
  display: flex;
  justify-content: space-between;
  margin-top: 30px;
}

/* hotel picture shows   */
.contain_imagen {
  width: 33%;
  margin-left: -18px;
  margin-right: 30px;
}

.imagen_hotel {
  width: 100%;
  border-radius: 10px;
}

/* Hearth Image */
.imagen_hearth {
  text-align: right;
  padding-right: 30px;
}
.destacado {
  z-index: 1;
}

.container_hotel .information .destacado {
  width: 35px;
  position: absolute;
}

.destacado:active {
  border: 1px solid #ff385c;
  border-radius: 10px;
}

/* Google map of hotels */
.mapaHotel {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 60px 0;
  padding-bottom: 100px;
}
</style>
