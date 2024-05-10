import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import InimigoCavaleiro from '../components/CavaleiroCard';

const DetalhesInimigo = () => {
  const { idCavaleiro } = useParams();
  const [inimigo, setInimigo] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Construa a URL da API com base no ID do inimigo
    const apiUrl = `http://127.0.0.1:5000/api/v1/inimigos/${idCavaleiro}`;

    // Faça a chamada fetch para obter os detalhes do inimigo
    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error('Erro ao buscar detalhes do inimigo');
        }
        return response.json();
      })
      .then(data => setInimigo(data))
      .catch(error => setError(error.message));
  }, [idCavaleiro]);

  if (error) {
    return <div>Erro: {error}</div>;
  }

  return (
    <div>
      <h1>Detalhes do Inimigo</h1>
      {inimigo ? (
        <div>
          <h2>{inimigo.nome}</h2>
          <p>Descrição: {inimigo.descricao}</p>
          {/* Aqui você pode exibir outros detalhes do inimigo */}
        </div>
      ) : (
        <div>Carregando...</div>
      )}
      {inimigo && (
        <InimigoCavaleiro
          nome={inimigo.nome}
          signo={inimigo.signo}
          armadura={inimigo.armadura}
          poderEspecial={inimigo.poder_especial}
          imagemUrl={inimigo.url}
        />
      )}
    </div>
  );
}

export default DetalhesInimigo;