import React, { useState } from 'react';
import axios from 'axios';
import MonacoEditor from 'react-monaco-editor';

// definindo o componente App
const App = () => {
  // armazenar o código HTML inserido no editor
  const [htmlCode, setHtmlCode] = useState('');

  // armazenar a contagem de tags após a pesquisa
  const [tagsCount, setTagsCount] = useState(null);

  // função para enviar o código HTML para o backend e realizar a pesquisa de tags
  const handleSearchTags = async () => {
    try {
      // faz a chamada POST para a rota /search_tags do backend
      // envia o código HTML como parâmetro da requisição
      const response = await axios.post('/search_tags', { html_code: htmlCode });

      // atualiza o estado com a contagem de tags obtida do backend
      setTagsCount(response.data.tags_count);
    } catch (error) {
      // exibe mensagem de erro no console em caso de falha na requisição
      console.error('Erro ao pesquisar tags:', error);
    }
  };

  // função para enviar o código HTML para o backend e fazer o upload da página
  const handleUpload = async () => {
    try {
      // faz a chamada POST para a rota /upload_html do backend
      // envia o código HTML como parâmetro da requisição
      const response = await axios.post('/upload_html', { html_code: htmlCode });

      // exibe a mensagem de sucesso no console em caso de sucesso na requisição
      console.log(response.data.message);
    } catch (error) {
      // exibe mensagem de erro no console em caso de falha na requisição
      console.error('Erro ao enviar o HTML:', error);
    }
  };

  return (
    <div className="App">
      <h1>FastAPI + React</h1>
      {/* Editor do Mônaco para inserir o código HTML */}
      <MonacoEditor
        language="html"
        theme="vs-dark"
        value={htmlCode}
        onChange={(value) => setHtmlCode(value)}
        options={{
          minimap: { enabled: false },
        }}
      />
      {/* Botões para executar as ações */}
      <button onClick={handleSearchTags}>Pesquisar Tags</button>
      <button onClick={handleUpload}>Enviar HTML</button>
      {/* exibe a contagem de tags após a pesquisa */}
      {tagsCount && (
        <div>
          <h2>Contagem de Tags:</h2>
          {/* exibe o resultado da contagem de tags em formato JSON */}
          <pre>{JSON.stringify(tagsCount, null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

// exporta o componente App para ser usado em outros arquivos
export default App;
