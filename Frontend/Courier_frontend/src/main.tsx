import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'
import ToggleLoginLogoutButton from './component/Navbar/ToggleLoginLogoutButton';


createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <ToggleLoginLogoutButton>
      <App />
    </ToggleLoginLogoutButton>
    
  </StrictMode>,
)
