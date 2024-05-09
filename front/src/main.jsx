import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter,Routes,Route } from 'react-router-dom';
import App from './App.jsx';
import './index.css';
import Home from './pages/Home.jsx';


ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
    <Routes>
      <Route element = {<App/>}>
        <Route path="/" element={<Home/>}/>
      </Route>
    </Routes>
    </BrowserRouter>
   
  </React.StrictMode>,
)
