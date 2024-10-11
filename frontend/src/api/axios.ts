import axios, { AxiosInstance } from "axios";

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
      const { data } = await this.api.get(url)

      return data;
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
      const { data } = await this.api.put(path, body)

      return data
    }

    if (method === 'DELETE') {
      const { data } = await this.api.delete(path)

      return data
    }
  }
}