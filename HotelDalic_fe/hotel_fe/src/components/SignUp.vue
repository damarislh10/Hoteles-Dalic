<template>
    <div class="signUp_user">
        <div class="container_signUp_user">
            <h2>Registrarse</h2>
        <form v-on:submit.prevent="processSignUp" >
            <input type="text" v-model="user.username" placeholder="Usuario" required>
            <br>
            <input type="password" v-model="user.password" placeholder="Contraseña" required>
            <br>
 
            <input type="text" v-model="user.name" placeholder="Nombre" required>
            <br>
            <input type="email" v-model="user.email" placeholder="Email" required>
            <br>
            <button type="submit">Continúa</button>
        </form>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
    export default {
        name: "SignUp",
        data: function(){
            return {
                user: {
                    username: "",
                    password: "",
                    name: "",
                    email: "",

                    }
                }
        },
        methods: {
            processSignUp: function(){
            axios.post(
                    "https://hotel-despliegue.herokuapp.com/user/",
                    this.user, 
                    {headers: {}}
                 )
                    .then((result) => {
                        let dataSignUp = {
                            username: this.user.username,
                            token_access: result.data.access,
                            token_refresh: result.data.refresh,
                            }
                            this.$emit('completedSignUp', dataSignUp)
                        })
                    .catch((error) => {
                        console.log(error)
                        swal("Error","Fallo en el registro o usuario ya existente ","error");

                    });
            }
        }
}
</script>
<style>
 .signUp_user{
        margin: 0;
        padding: 0%;
        height: 100%;
        width: 100%;
        
        display: flex;
        justify-content: center;
        align-items: center;
        }
 .container_signUp_user {
        border-top: 1px solid #e1e4e7;
        border-radius: 10px;
        width: 35%;
        height: 80%;
        margin-top: 100px;


        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background: rgba(255, 255, 255,.7);

 
    }
 .signUp_user h2{
        color: #222222;
        font-size: 24px;
        line-height: 70px;
 
    }
 .signUp_user form{
        width: 70%;
 
}
 .signUp_user input{
        height: 40px;
        width: 100%;
        box-sizing: border-box;
        padding: 10px 20px;
        margin: 5px 0;
        border: 1px solid #9c9fa3;
}
 .signUp_user button{
        width: 100%;
        height: 40px;
        color: #E5E7E9;
        font-weight: bold;
        background-image: radial-gradient(circle at center center, rgb(255, 56, 92) 0%, rgb(230, 30, 77) 27.5%, rgb(227, 28, 95) 40%, rgb(215, 4, 102) 57.5%, rgb(189, 30, 89) 75%, rgb(189, 30, 89) 100%);
        border: none;
        border-radius: 5px;
        padding: 10px 25px;
        margin: 5px 0 25px 0;
 
}
 .signUp_user button:hover{
        color: #E5E7E9;
        background-image: radial-gradient(circle at center center, rgb(255, 56, 92) 0%, rgb(230, 30, 77) 27.5%, rgb(227, 28, 95) 40%, rgb(215, 4, 102) 57.5%, rgb(189, 30, 89) 75%, rgb(189, 30, 89) 100%);
        border: none;
}

</style>