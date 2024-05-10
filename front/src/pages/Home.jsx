import React from "react";
import { useState,useEffect } from "react";
import './Home.css';
import CavaleiroCard from '../components/CavaleiroCard';

const url_cavaleiros = 'http://127.0.0.1:5000/api/v1/cavaleiros/';
const url_inimigos_cavaleiros = 'http://127.0.0.1:5000/api/v1/inimigos/';


// const Home = () =>{
//     const [cavaleiros,setCavaleiros] = useState([])
//     const getAllCavaleiros = async (url) =>{
//     const res = await fetch(url)
//     const data = await res.json()
//     console.log(res.data)
//     setCavaleiros(data.results);   

//     };

//     useEffect( () => {
//         getAllCavaleiros(url_cavaleiros);
//     },[])

//     return (
//         <div className="container">
//             <h2 className="title"></h2>
//             <div className="cavaleiro-container">
//                 <h1>Cavaleiros</h1>
//                 {cavaleiros.length === 0 && <p>Carregando...</p>}
//                 {cavaleiros.length >0 && cavaleiros && cavaleiros.map((console.log(cavaleiros)))}
//             </div>
//         </div>
//     );

// };



const Home = () => {
  const [cardsData, setCardsData] = useState([]);

  useEffect(() => {
    // Aqui você faria a chamada para sua API e atualizaria o estado 'cardsData'
    // Exemplo fictício:
    fetch(url_cavaleiros)
      .then(response => response.json())
      .then(data => {
        console.log('Dados recebidos da API:', data);
        setCardsData(data);
      })

     
      .catch(error => console.error('Erro ao buscar dados da API:', error));
  }, []);

  return (
    
    <div className="home-page">
      <h1>Home Page</h1>
      <div className="cards-container">
        {cardsData.map(card => (
          <CavaleiroCard
            key={card.id} // Certifique-se de usar uma chave única para cada card
            nome={card.nome}
            signo={card.signo}
            armadura={card.armadura}
            poderEspecial={card.poder_especial}
            imagemUrl={card.url}
          />
        ))}
      </div>
    </div>
    
  );
}



export default Home
