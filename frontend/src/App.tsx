import './App.css'
import React from 'react';
import Webcam from 'react-webcam';
import { useArrayImages } from './useArrayImage';

function App() {

  const webcamRef = React.useRef<Webcam>(null);
  const videoConstraints = {facingMode: "user"};
  const ArrayImagens = useArrayImages((state)=> state.imagens)
  const adicionarImagem = useArrayImages((state)=> state.adicionarImagem)
  const removerImagem = useArrayImages((state)=> state.removerImagem)

  const capture = React.useCallback(() => {
    if(ArrayImagens.length == 10){
      console.log(10)
    }
    else{
      const novaImagem = webcamRef?.current?.getScreenshot();
      if (novaImagem) {
        adicionarImagem(novaImagem)
      }
      console.log(novaImagem)
    }
  },[ArrayImagens,adicionarImagem, webcamRef]);
  

  return (
    <>
      <nav>
        <h1>Unip</h1>
      </nav>
      <Webcam
        width={512}
        height={512}
        audio={false}
        ref={webcamRef}
        screenshotFormat="image/jpeg"
        videoConstraints = {videoConstraints}
      />
      <button onClick={capture}>Capture photo</button>

      <div>
        {
          ArrayImagens.map((value,index)=>(
            <div key={index}>
              <img src={value} alt={`Imagem captura ${index}`}/>
              <button type="submit" onClick={()=> removerImagem(index)}> Remover Imagem</button>
            </div>
          ))
        }
      </div>
    </>
  )
}

export default App
