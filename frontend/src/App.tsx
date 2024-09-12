import { useState , useEffect} from 'react'
import Webcam from 'react-webcam';

import './App.css'
import React from 'react';

interface alunos{
  codigo: string,
  nome: string,
  tipo: number
}

function App() {

  const [imagem, setImagem] = useState<string[]>([])
  const webcamRef = React.useRef<Webcam>(null);

  const capture = React.useCallback(
    () => {
      
      if(imagem.length == 10){//manda backend
        

        console.log(10)
      }
      else{
        const novaImagem = webcamRef?.current?.getScreenshot();
        if (novaImagem) {
        // Atualiza o estado adicionando a nova imagem
          setImagem((prevImagens) => [...prevImagens, novaImagem]);
          console.log(imagem)
        }
        console.log(novaImagem)
      }
    },
    [imagem, webcamRef]
  );
  const videoConstraints = {
    facingMode: "user"
  };

  return (

    <>
      <nav>
        <h1>Unip</h1>
      </nav>
      <Webcam
        audio={false}
        height={512}
        ref={webcamRef}
        screenshotFormat="image/jpeg"
        width={512}
        videoConstraints = {videoConstraints}
      />
      <button onClick={capture}>Capture photo</button>

      { 
        imagem.map((imagem,index)=>{
          <img key={index} src={imagem} alt="" width="20px" height="20px"/>
        })
      }
    </>
  )
}

export default App

/*<div>
      {/* Mapeia o array de alunos para criar parágrafos }
      {alunos.length > 0 ? (
        alunos.map((aluno) => (
          <p key={aluno.codigo}>
            Código: {aluno.codigo}, Nome: {aluno.nome}, Tipo: {aluno.tipo}
          </p>
        ))
      ) : (
        <p>Carregando alunos...</p> // Mensagem enquanto os dados estão sendo carregados
      )}
    </div>

    // const [alunos, setAlunos] = useState<alunos[]>([])
  // const getAlunos = async ()=>{

  //   try{
  //     const response = await fetch('http://localhost:8000/alunos')
  //     const data = await response.json();
  //     setAlunos(data)
  //   }
  //   catch (err){
  //     console.log(err)
  //   }

  // }


    
*/