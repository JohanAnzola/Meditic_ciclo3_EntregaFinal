<template>

    <div class="signUp_user">
        <div class="container_signUp_user">
            <h2>Registrarse</h2>

            <form v-on:submit.prevent="processSignUp" >
                <input type="text" v-model="user.ccMedico" placeholder="Cedula">
                <br>
                
                <input type="password" v-model="user.password" placeholder="Contraseña">
                <br>
                
                <input type="text" v-model="user.nombre" placeholder="Nombre">
                <br>

                <input type="email" v-model="user.email" placeholder="Email">
                <br>

                

                <button type="submit">Registrarse</button>
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
                ccMedico: "",
                password: "",
                nombre: "",
                email: "",
                
                
            }
        }
    },

    methods: {
        processSignUp: function(){
            axios.post(
                "https://meditic-be-2.herokuapp.com/user/", 
                this.user,  
                {headers: {}}
            )
                .then((result) => {
                    let dataSignUp = {
                        ccMedico: this.user.ccMedico,
            token_access: result.data.access,
            token_refresh: result.data.refresh,
                    }
                    
                    this.$emit('completedSignUp', dataSignUp)
                })
                .catch((error) => {
                    console.log(error)
                    alert("Erroe en el resgistro.");
                    
                    
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
        border: 3px solid  #283747;
        border-radius: 10px;
        width: 25%;
        height: 60%;
        
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .signUp_user h2{
        color: #4E93D0;

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

        border: 1px solid #283747;
    }

    .signUp_user button{
        width: 100%;
        height: 40px;

        color: #E5E7E9;
        background: #186cc5;
        border: 1px solid #E5E7E9;

        border-radius: 5px;
        padding: 10px 25px;
        margin: 5px 0 25px 0;
    }

    .signUp_user button:hover{
        color: #E5E7E9;
        background: #4E93D0;
        border: 1px solid #283747;
    }

</style>