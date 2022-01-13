import logo from './logo.svg';
import './App.css';
import { Routes, Route, Link } from 'react-router-dom';

function App() {
  return (
    <Routes>
      <Route exact path="/" element={<main />}> </Route>
      <Route path="/login" element={<login />}> </Route>
      <Route path="/join" element={<join />}> </Route>
      <Route path="/room" element={<room />}> </Route>
      <Route path="/chat" element={<chat />}> </Route>
      <Route path="/photo" element={<photo />}> </Route>
      <Route path="/schedule" element={<schedule />}> </Route>
    </Routes>
  );
}

export default App;