import React from 'react';
import { Link } from 'react-router-dom';

const Card = ({ nome, signo, armadura, poderEspecial, imagemUrl,idCavaleiro }) => {
  return (
    <div className="card">
      <img src={imagemUrl} alt={nome} />
      <h2>{nome}</h2>
      <p>Signo: {signo}</p>
      <p>Armadura: {armadura}</p>
      <p>Poder Especial: {poderEspecial}</p>
      <Link to={`/detalhes/${idCavaleiro}`}>
        <button>Ver Detalhes do Inimigo</button>
      </Link>

      
    </div>
  );
}

export default Card;
