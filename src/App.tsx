import React from 'react';
import { ChakraProvider } from '@chakra-ui/react'
import '@fontsource/raleway/400.css'
import '@fontsource/open-sans/700.css'
import theme from './components/Theme/Theme';
import Router from './Router';
import './App.css';



function App() {
  return (
    <React.StrictMode>
      <ChakraProvider resetCSS theme={theme}>
        <Router/>
      </ChakraProvider>
    </React.StrictMode>

  );

  }
export default App;
