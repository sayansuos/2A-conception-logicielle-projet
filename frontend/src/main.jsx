import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import ChampionSearch from './component/ChampionSearch.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    < ChampionSearch/>
  </StrictMode>,
)
