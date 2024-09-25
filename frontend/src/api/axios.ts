import axios, { AxiosInstance } from "axios";

export interface makeRequestProps {
  path: string;
  subpath?: string;
  method: 'GET' | 'POST' | 'PUT' | 'DELETE';
  params?: object | string;
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
    urlParams,
    params,
  }: makeRequestProps) {
    if (method === 'GET') {
      console.log(urlParams);

      const splitPath = subpath!.split('-'); //materias-aluno = ['materias', 'aluno'] [1, 10]
      if (splitPath.length > 1) {
        const pathFormatted = splitPath.map((item, index) => {
          return `${item}/${urlParams![index]}`;
        });

        const pathWithSubpath = pathFormatted.join('/');

        const { data } = await this.api.get(`${path}/${pathWithSubpath}`, { params });

        return data;
      }

      const { data } = await this.api.get(`${path}/${subpath}/${urlParams![0]}`, { params });

      return data;
    }
    if (method === 'POST') {

      const { data } = await this.api.post(path, params)
      return data
    }
  }
}