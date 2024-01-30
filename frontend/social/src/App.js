import { BrowserRouter, Route, Routes } from 'react-router-dom';
import './App.scss';
import Layout from './components/layout/Layout';
import Home from './pages/Home';
import SignIn from './pages/SignIn';
import SignUp from './pages/SignUp';
import Profile from './pages/Profile';
import Post from './pages/Post';


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Layout />}>
          <Route path='/' element={<Home />} />
          <Route path='/signin' element={<SignIn />} />
          <Route path='/signup' element={<SignUp />} />
          <Route path='/profile' element={<Profile />} />
          <Route path='/post' element={<Post />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
