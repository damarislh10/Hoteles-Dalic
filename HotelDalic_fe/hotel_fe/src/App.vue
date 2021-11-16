<template>
  <div id="app" class="app">
    <div class="header">
      <img src="../src/assets/logodalic.jpg" />
      <h2>Dalic</h2>
      <nav>
        <button v-if="is_auth" v-on:click="loadHome">Inicio</button>
        <button v-if="is_auth">Perfil</button>
        <button v-if="is_auth" v-on:click="logOut">Cerrar Sesión</button>
        <button v-if="!is_auth" v-on:click="loadLogIn">Iniciar Sesión</button>
        <button v-if="!is_auth" v-on:click="loadSignUp">Registrarse</button>
      </nav>
    </div>

    <div class="main-component">
      <router-view
        v-on:completedLogIn="completedLogIn"
        v-on:completedSignUp="completedSignUp"
        v-on:logOut="logOut"
      >
      </router-view>
    </div>

    <div class="footer">
      <ul>
        <h6>ACERCA DE</h6>
        <li><a href="#">Cómo funciona Dalic</a></li>
        <li><a href="#">Contáctenos</a></li>
        <li><a href="#">Centro de la comunidad</a></li>
      </ul>
      <ul>
        <h6>ASISTENCIA</h6>
        <li><a href="#">Centro de ayuda</a></li>
        <li><a href="#">Privacidad</a></li>
        <li><a href="#">Confianza y seguridad</a></li>
      </ul>
    </div>
    <div class="derechos_reservados">
      <div>
        © 2021 Dalic, Inc.
        <a href="#"> · Privacidad</a>
        <a href="#"> · Términos</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "App",

  data: function() {
    return {
      is_auth: false,
    };
  },
  components: {},

  methods: {
    verifyAuth: function() {
      this.is_auth = localStorage.getItem("isAuth") || false;

      if (this.is_auth == false) 
        this.$router.push({ name: "logIn" });

      else
       this.$router.push({ name: "home" });
    },

    loadLogIn: function() {
      this.$router.push({ name: "logIn" });
    },

    loadSignUp: function() {
      this.$router.push({ name: "signUp" });
    },

    completedLogIn: function(data) {
      localStorage.setItem("isAuth", true);
      localStorage.setItem("username", data.username);
      localStorage.setItem("token_access", data.token_access);
      localStorage.setItem("token_refresh", data.token_refresh);
      this.verifyAuth();
    },

    completedSignUp: function(data) {
      alert("Registro Exitoso");
      this.completedLogIn(data);

    },


    loadHome: function() {
      this.$router.push({ name: "home" });
    },
    logOut: function() {
      localStorage.clear();
      console.log("Sesión Cerrada");
      this.verifyAuth();
    },
  },

  created: function() {
    this.verifyAuth();

  },
};
</script>
<style>

body {
  margin: 0 0 0 0;
}
/* Background Image */
body {
  background-image: url(https://i.pinimg.com/originals/50/98/d4/5098d4f2f18ee7903bd8d6e4010e5c55.jpg);
  background-position: left;
  background-size: auto;
  background-size: contain;
  background-size: cover;
  background-attachment: fixed;
  background-repeat: no-repeat;
}
.app {
  font-family: Circular, -apple-system, BlinkMacSystemFont, Roboto,
    Helvetica Neue, sans-serif;
}


.header {
  margin: 0%;
  padding: 0;
  width: 100%;
  height: 14vh;
  min-height: 100%;

  background-color: rgb(255, 255, 255);
  box-shadow: 1px 0 4px rgb(0, 0, 0, 0.2);
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.header h2 {
  width: 5%;
  margin-left: -800px;
  color: #ff385c;
  font-family: "Alata", sans-serif;
}
.header h2,.header img:hover {
  cursor: pointer;
}
.header nav {
  height: 100%;
  width: 20%;

  display: flex;
  justify-content: space-around;
  align-items: center;
  font-size: 20px;
  margin-right: 85px;
}
.header nav button {
  border: none;
  background: #fff;

  font-size: 16px;
  color: #222222;
  font-family: inherit;
}
.header nav button:hover {
  cursor: pointer;
}
.header nav button:hover {
  padding: 10px;
  border-radius: 22px;
  background: #f7f7f7;
}
.header img {
  width: 60px;
  margin-left: 70px;
}
.main-component {
  margin: 0%;
  padding: 0%;
}

.footer {
  margin-top: 100px;
  padding: 0;
  width: 100%;
  height: 10vh;
  min-height: 170px;

  background-color: #f7f7f7;
  color: #222222;
  border-top: 1px solid rgb(207, 205, 205);
  border-bottom: 1px solid rgb(207, 205, 205);
}
.footer h6 {
  width: 100%;
  height: 100%;

  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 14px;
}

.footer ul{
  display:inline-block;
  padding-top:40px;
  padding-bottom: 50px;
  margin-left: 30px;
}

/* Content list */
.footer li{
  list-style: none;
}

.footer li a{
  text-decoration: none;
  font-size: 14px;
  line-height: 18px;
  color: rgb(34, 34, 34);
}

.derechos_reservados {
  display: flex;
  background-color: #f7f7f7;
  padding: 20px;
  font-size: 14px;
  color: #222222;
  width: 100%;
  text-align: left;
}
.derechos_reservados a {
  text-decoration: none;
  line-height: 18px;
  color: #222222;
}


</style>
