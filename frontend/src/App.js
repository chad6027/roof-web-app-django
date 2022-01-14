import './App.css';
import {BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Room from './routes/room'

function App() {
  return (
          <Router>
              <Routes>
                <Route path="/room" element={<Room />} />
              </Routes>
          </Router>
  )
  ;
}

export default App;





