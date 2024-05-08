import { useState, useEffect } from "react";


const link = "http://127.0.0.1:5000/api/v1/cavaleiros/"

// function getUser(){
//     axios.get(url)
//     .then(response =>{
//         console.log(response)
//         const data = response.data
//         card.textContent= JSON.stringify(data)
//         document.getElementById('card-img').src=data.url;

//     } )
//     .catch(error=>console.log(error))
// }

// getUser()

function Cavaleiro(){
    const [cavaleiros,setCavaleiros]= useState([]);
    useEffect(() => {
        axios.get(link)
        .then((respose)=>setCavaleiros(respose.data,console.log(respose.data)))
        .catch(error=>console.log(error))
    },[])
    return
}
Cavaleiro();