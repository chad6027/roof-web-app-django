import logo from './logo.svg';
import './App.css';
import {BrowserRouter as Router, Routes, Route, Link, Switch} from 'react-router-dom';
import Room from './routes/room'

function App() {
  return (
          <Router>
              <Routes>
                <Route exact={true} path="/" element={<Room />} />
              </Routes>
          </Router>
  )
  ;
}

export default App;





