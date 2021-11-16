<template>
  <div class="logIn_user">
    <div class="container_logIn_user">
      <h2>Iniciar sesión</h2>
      <form v-on:submit.prevent="processLogInUser">
        <input
          type="text"
          v-model="user.username"
          placeholder="Usuario"
          required
        />
        <br />
        <input
          type="password"
          v-model="user.password"
          placeholder="Contraseña"
          required
        />
        <br />
        <button type="submit">Continúa</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "LogIn",

  data: function() {
    return {
      user: {
        username: "",
        password: "",
      },
    };
  },

  methods: {
    processLogInUser: function() {
      axios
        .post("https://hotel-despliegue.herokuapp.com/login/", this.user, {
          headers: {},
        })
        .then((result) => {
          let dataLogIn = {
            username: this.user.username,
            token_access: result.data.access,
            token_refresh: result.data.refresh,
          };

          this.$emit("completedLogIn", dataLogIn);
        })
        .catch((error) => {
          if (error.response.status == "401")
            swal("Error", "Credenciales Incorrectas", "error");
        });
    },
  },
};
</script>
<style>
.logIn_user {
  margin: 0;
  padding: 0%;
  height: 100%;
  width: 100%;

  display: flex;
  justify-content: center;
  align-items: center;
}

.container_logIn_user {
  border-radius: 10px;
  border-top: 1px solid #e1e4e7;
  width: 35%;
  height: 370px;
  margin-top: 100px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background: rgba(255, 255, 255, 0.7);
}

.logIn_user h2 {
  color: #222222;
  font-size: 24px;
  line-height: 70px;
}
.logIn_user form {
  width: 70%;
}
.logIn_user input {
  height: 40px;
  width: 100%;
  box-sizing: border-box;
  padding: 10px 20px;
  margin: 5px 0;
  border: 1px solid #9c9fa3;
}

.logIn_user button {
  width: 100%;
  height: 40px;
  color: #e5e7e9;
  font-weight: bold;
  background-image: radial-gradient(
    circle at center center,
    rgb(255, 56, 92) 0%,
    rgb(230, 30, 77) 27.5%,
    rgb(227, 28, 95) 40%,
    rgb(215, 4, 102) 57.5%,
    rgb(189, 30, 89) 75%,
    rgb(189, 30, 89) 100%
  );
  border-radius: 5px;
  border: none;
  padding: 10px 25px;
  margin: 5px 0;
}
.logIn_user button:hover {
  color: #e5e7e9;
  background-image: radial-gradient(
    circle at center center,
    rgb(255, 56, 92) 0%,
    rgb(230, 30, 77) 27.5%,
    rgb(227, 28, 95) 40%,
    rgb(215, 4, 102) 57.5%,
    rgb(189, 30, 89) 75%,
    rgb(189, 30, 89) 100%
  );
}
</style>
