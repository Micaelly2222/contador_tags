import React from 'react';
import { createRoot } from 'react-dom';
import App from './App';


const root = document.getElementById('root');
const appRoot = createRoot(root); 
appRoot.render(<App />);