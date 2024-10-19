import { createLazyFileRoute } from '@tanstack/react-router'

export const Route = createLazyFileRoute('/boletim')({
  component: () => <div>Hello /boletim!</div>,
})
