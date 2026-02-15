import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import Home from './Home.tsx'
import { BrowserRouter, Route, Routes, Navigate } from 'react-router'
import Applications from './Applications.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <BrowserRouter>
        <Routes>
            <Route path="/" element={<Navigate to="/home" />} />
            <Route path="/home" element={<Home />} />
            <Route path="/applications" element={<Applications />} />
        </Routes>
    </BrowserRouter>
  </StrictMode>,
)
