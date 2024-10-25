import { useCallback, useEffect, useRef, useState } from "react";
import Webcam from "react-webcam";
import { apiService } from "../api/api";
import { makeRequestProps } from "../api/axios";

interface CameraHookProps {
    webcamRef: React.RefObject<Webcam>;
    apiCall: makeRequestProps;
    onCaptureImagesR?: boolean;
}

export const CameraHook = ({ webcamRef, apiCall, onCaptureImagesR}: CameraHookProps) => {
  const [arrayImagens, setArrayImagens] = useState<string[]>([]);
  const [authenticating, setAuthenticating] = useState<boolean>(false);
  const [responseData, setResponseData] = useState<unknown>();
  const arrayImagensRef = useRef<string[]>([]);

  const getPhotos = async (codAluno:string) => {
    const timeToGetPhoto = 3000;
    const timeForUs = timeToGetPhoto / 10;
    let data;

    setAuthenticating(true);

    const intervalPhoto = setInterval(() => {
      const novaImagem = webcamRef?.current?.getScreenshot();

      if (novaImagem) {
          setArrayImagens((prev) => {
            const newArray = [...prev, novaImagem];
            arrayImagensRef.current = newArray; // Update the ref
            return newArray;
          });
        }
      }, timeForUs);

    setTimeout(async () => {
      clearInterval(intervalPhoto);

      if(onCaptureImagesR){
        setAuthenticating(false)
      }

      else{
        try {
          data = await apiService().makeRequest({
            ...apiCall,
            body: {
              codigo: codAluno,
              fotos: arrayImagensRef.current,
            },
          });
          
          setResponseData(data);
        } catch (error) {
          setArrayImagens([])
          setResponseData({ error: true });
        }

      }
    }, 3000);

    return data
  };

  const toggleIsAuthenticating = useCallback(() => {
    setAuthenticating(prev => !prev)
  }, [authenticating])

  useEffect(() => {
    console.log(arrayImagens);
  }, [arrayImagens]);


  return {
    getPhotos,
    arrayImagens,
    toggleIsAuthenticating,
    responseData,
    authenticating,
  }
}