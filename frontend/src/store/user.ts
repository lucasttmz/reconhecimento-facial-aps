import { jwtDecode } from 'jwt-decode';
import { create } from 'zustand'

interface User {
  user_id: string
  name: string
  sub: string
  permissions: number
}

interface stateProps {
  user: User | null
}

interface actionsProps {
  addUser: (token: string) => void

  removeUser: () => void
}

interface storeProps {
  actions: actionsProps

  states: stateProps
}

const jwtDecodeToken =  (token: string) => {
    try {
        const tokenDecoded: User = jwtDecode(token)

        console.log(tokenDecoded)

        if (tokenDecoded && typeof tokenDecoded !== 'string') {
            return tokenDecoded as User;
        }

        return null;
  } catch (error) {
    console.log(error)
  }
}

export const useUserStore = create<storeProps>((set) => ({
  actions: {
    addUser: (user) =>
      set(() => ({
        states: {
          user: jwtDecodeToken(user)
        },
      })),
    removeUser: () => set(() => ({ states: { user: null } })), 
  },
  states: {
    user: null,
  },
}))