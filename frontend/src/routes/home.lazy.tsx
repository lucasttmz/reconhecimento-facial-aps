import { createLazyFileRoute } from '@tanstack/react-router'

export const Route = createLazyFileRoute('/home')({
  component: Home,
})

function Home() {
  return <div>Home</div>
}
