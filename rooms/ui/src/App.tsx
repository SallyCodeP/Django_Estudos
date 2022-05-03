import React from 'react';
import logo from './logo.svg';
import './App.css';
import styled from 'styled-components';
import InputSeiLa from './Components/InputSeiLa';

type AppProps = {
  className?: string;

}
  

const App = ({className}:AppProps) => {
  return (
    <div 
    className={className}>
    <div className='patostyle'>Pato</div>
    <InputSeiLa
    name='pato'
    placeHolder='eu sou um pato?'
    type='text'
    />
    
    </div>
  );
}
  

export default styled(App)`
  background-color: red;
  width: 20em;
  height: 20em;
  display: flex;
  aling-items: center;
  justify-content: center;

  .patostyle {
    background-color: blue;
    width: 50px;
    height: 50px;
      
  }

  `;
