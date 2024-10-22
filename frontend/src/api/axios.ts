import axios, { AxiosInstance } from "axios";
import { useUserStore } from '../store/user'


export interface makeRequestProps {
  path: string;
  subpath?: string;
  method: string;
  body?: object | string;
  urlParams?: unknown[];
  urlQuery?: object;
}

export class api {
  private api: AxiosInstance;

  constructor() {
    this.api = axios.create({
      baseURL: 'http://localhost:8000/',
      headers:{'Authorization': `Bearer ${localStorage.getItem('token')}`}
    });
  }

  async makeRequest({
    method,
    path,
    subpath,
    body,
  }: makeRequestProps) {
    
    let url = path;

    if (subpath) url += `/${subpath}`

    if (method === 'GET') {
      
      try {
        const {data} = await this.api.get(url)
        
        return data;
      
      } catch (error) {
        
        return {error: true}
      }
    }

    if (method === 'POST') {
      
      try {

        const data = await this.api.post(path, body)
        return data
      
      } catch (error) {
        
        return {error: true}
      }
      
    }

    if (method === 'PUT') {

      const data  = await this.api.put(url,body)
      
      return data
    
    }

    if (method === 'DELETE') {
      const { data } = await this.api.delete(path)

      return data
    }
  }
}