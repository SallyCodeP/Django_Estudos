import Reac from 'react';
import styled from 'styled-components';


type InputSeiLaProps = {
    className?: string;
    placeHolder?: string;
    name?: string;
    type?: string;

};

const InputSeiLa = ({className, placeHolder, name, type}: InputSeiLaProps) => {
    return (
       <input 
       className={className}
       placeholder={placeHolder}
       name={name}
       type={type}
       />
    );
};

export default styled(InputSeiLa)`
    width: 10em;
    height: 1em;
    background-color: pink;
    border-radius: 15px;
    border: 2px solid green;
`;