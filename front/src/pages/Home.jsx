import React from "react";
import { useState,useEffect } from "react";
import './Home.css';


const url_cavaleiros = 'http://127.0.0.1:5000/api/v1/cavaleiros/';
const url_inimigos_cavaleiros = 'http://127.0.0.1:5000/api/v1/inimigos/';


const Home = () =>{
    const [cavaleiros,setCavaleiros] = useState([])
    const getAllCavaleiros = async (url) =>{
    const res = await fetch(url)
    const data = await res.json()
    console.log(res.data)
    setCavaleiros(data.results);   

    };

    useEffect( () => {
        getAllCavaleiros(url_cavaleiros);
    },[])

    return (
        <div className="container">
            <h2 className="title"></h2>
            <div className="cavaleiro-container">
                <h1>Cavaleiros</h1>
                {cavaleiros.length === 0 && <p>Carregando...</p>}
                {cavaleiros.length >0 && cavaleiros && cavaleiros.map((console.log(cavaleiros)))}
            </div>
        </div>
    );

};

export default Home
