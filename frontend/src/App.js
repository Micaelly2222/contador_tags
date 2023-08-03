import React, { useState } from 'react';
import axiosInstance from './axiosInstance';
import MonacoEditor from 'react-monaco-editor';
import './App.css';

const App = () => {
  // Armazenar o código HTML inserido no editor
  const [htmlCode, setHtmlCode] = useState('');

  // Armazenar a contagem de tags após a pesquisa
  const [tagsCount, setTagsCount] = useState(null);

  // Função para enviar o código HTML para o backend e realizar a pesquisa de tags
  const handleSearchTags = async () => {
    try {
      // Faz a chamada POST para a rota /upload_html do backend
      // Envia o código HTML como parâmetro da requisição
      const response = await axiosInstance.post('/upload_html', { html_code: htmlCode });

      // Atualiza o estado com a contagem de tags obtida do backend
      setTagsCount(response.data.tags_count);
    } catch (error) {
      // Exibe mensagem de erro no console em caso de falha na requisição
      console.error('Erro ao pesquisar tags:', error);
    }
  };

  // Função para obter as informações da página pelo nome
  const handleGetPageInfo = async (pageName) => {
    try {
      // Faz a chamada GET para a rota /get_page_info/{page_name} do backend
      const response = await axiosInstance.get(`/get_page_info/${pageName}`);

      // Atualiza o estado com as informações da página obtidas do backend
      setTagsCount(response.data.page_info);
    } catch (error) {
      // Exibe mensagem de erro no console em caso de falha na requisição
      console.error('Erro ao obter informações da página:', error);
    }
  };

  return (
    <div className="container">
      <h1 className="title">Contador de Tags</h1>
      {/* Editor do Mônaco para inserir o código HTML */}
      <MonacoEditor
        language="html"
        theme="vs-dark"
        value={htmlCode}
        onChange={(value) => setHtmlCode(value)}
        options={{
          minimap: { enabled: false },
        }}
        className="editor"
      />
      {/* Botões para executar as ações */}
      <div className="button-container">
        <button onClick={handleSearchTags}>Enviar HTML e Contar Tags</button>
        <button onClick={() => handleGetPageInfo('nome_da_pagina')}>Obter Informações da Página</button>
      </div>
      {/* Exibe a contagem de tags após a pesquisa */}
      {tagsCount && (
        <div className="tags-count-container">
          <h2>Contagem de Tags:</h2>
          {/* Exibe o resultado da contagem de tags em formato JSON */}
          <pre>{JSON.stringify(tagsCount, null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

export default App;
