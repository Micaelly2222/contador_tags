import React, { useState } from 'react';
import axios from 'axios';
import MonacoEditor from 'react-monaco-editor';
import './App.css';
import API_BASE_URL from './config'; 

const App = () => {
  // armazenar o código HTML inserido no editor
  const [htmlCode, setHtmlCode] = useState('');

  // armazenar a contagem de tags após a pesquisa
  const [tagsCount, setTagsCount] = useState(null);

  // função para enviar o código HTML para o backend e realizar a pesquisa de tags
  const handleSearchTags = async () => {
    try {
      // Faz a chamada GET para a rota /search_tags do backend
      // Utiliza o URL base da API 
      const response = await axios.get(`${API_BASE_URL}/search_tags?html_code=${encodeURIComponent(htmlCode)}`);

      // atualiza o estado com a contagem de tags obtida do backend
      setTagsCount(response.data.tags_count);
    } catch (error) {
      // Exibe mensagem de erro no console em caso de falha na requisição
      console.error('Erro ao pesquisar tags:', error);
    }
  };

  // Função para enviar o código HTML para o backend e fazer o upload da página
  const handleUpload = async () => {
    try {
      // Faz a chamada POST para a rota /upload_html do backend
      // Envia o código HTML como parâmetro da requisição
      const response = await axios.post(`${API_BASE_URL}/upload_html`, { html_code: htmlCode });

      // Exibe a mensagem de sucesso no console em caso de sucesso na requisição
      console.log(response.data.message);
    } catch (error) {
      // Exibe mensagem de erro no console em caso de falha na requisição
      console.error('Erro ao enviar o HTML:', error);
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
        <button onClick={handleSearchTags}>Pesquisar Tags</button>
        <button onClick={handleUpload}>Enviar HTML</button>
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
