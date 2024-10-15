/* prettier-ignore-start */

/* eslint-disable */

// @ts-nocheck

// noinspection JSUnusedGlobalSymbols

// This file is auto-generated by TanStack Router

import { createFileRoute } from '@tanstack/react-router'

// Import Routes

import { Route as rootRoute } from './routes/__root'

// Create Virtual Routes

const MateriasLazyImport = createFileRoute('/materias')()
const HomeLazyImport = createFileRoute('/home')()
const IndexLazyImport = createFileRoute('/')()

// Create/Update Routes

const MateriasLazyRoute = MateriasLazyImport.update({
  path: '/materias',
  getParentRoute: () => rootRoute,
} as any).lazy(() => import('./routes/materias.lazy').then((d) => d.Route))

const HomeLazyRoute = HomeLazyImport.update({
  path: '/home',
  getParentRoute: () => rootRoute,
} as any).lazy(() => import('./routes/home.lazy').then((d) => d.Route))

const IndexLazyRoute = IndexLazyImport.update({
  path: '/',
  getParentRoute: () => rootRoute,
} as any).lazy(() => import('./routes/index.lazy').then((d) => d.Route))

// Populate the FileRoutesByPath interface

declare module '@tanstack/react-router' {
  interface FileRoutesByPath {
    '/': {
      id: '/'
      path: '/'
      fullPath: '/'
      preLoaderRoute: typeof IndexLazyImport
      parentRoute: typeof rootRoute
    }
    '/home': {
      id: '/home'
      path: '/home'
      fullPath: '/home'
      preLoaderRoute: typeof HomeLazyImport
      parentRoute: typeof rootRoute
    }
    '/materias': {
      id: '/materias'
      path: '/materias'
      fullPath: '/materias'
      preLoaderRoute: typeof MateriasLazyImport
      parentRoute: typeof rootRoute
    }
  }
}

// Create and export the route tree

export interface FileRoutesByFullPath {
  '/': typeof IndexLazyRoute
  '/home': typeof HomeLazyRoute
  '/materias': typeof MateriasLazyRoute
}

export interface FileRoutesByTo {
  '/': typeof IndexLazyRoute
  '/home': typeof HomeLazyRoute
  '/materias': typeof MateriasLazyRoute
}

export interface FileRoutesById {
  __root__: typeof rootRoute
  '/': typeof IndexLazyRoute
  '/home': typeof HomeLazyRoute
  '/materias': typeof MateriasLazyRoute
}

export interface FileRouteTypes {
  fileRoutesByFullPath: FileRoutesByFullPath
  fullPaths: '/' | '/home' | '/materias'
  fileRoutesByTo: FileRoutesByTo
  to: '/' | '/home' | '/materias'
  id: '__root__' | '/' | '/home' | '/materias'
  fileRoutesById: FileRoutesById
}

export interface RootRouteChildren {
  IndexLazyRoute: typeof IndexLazyRoute
  HomeLazyRoute: typeof HomeLazyRoute
  MateriasLazyRoute: typeof MateriasLazyRoute
}

const rootRouteChildren: RootRouteChildren = {
  IndexLazyRoute: IndexLazyRoute,
  HomeLazyRoute: HomeLazyRoute,
  MateriasLazyRoute: MateriasLazyRoute,
}

export const routeTree = rootRoute
  ._addFileChildren(rootRouteChildren)
  ._addFileTypes<FileRouteTypes>()

/* prettier-ignore-end */

/* ROUTE_MANIFEST_START
{
  "routes": {
    "__root__": {
      "filePath": "__root.tsx",
      "children": [
        "/",
        "/home",
        "/materias"
      ]
    },
    "/": {
      "filePath": "index.lazy.tsx"
    },
    "/home": {
      "filePath": "home.lazy.tsx"
    },
    "/materias": {
      "filePath": "materias.lazy.tsx"
    }
  }
}
ROUTE_MANIFEST_END */
