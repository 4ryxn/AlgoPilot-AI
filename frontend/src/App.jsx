import {Navigate, Route, Routes} from "react-router-dom";
import Navbar from "./components/Navbar";
import Dashboard from "./pages/Dashboard";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Analytics from "./pages/Analytics";
import AICoach from "./pages/AICoach";
import Roadmap from "./pages/Roadmap";
import Pricing from "./pages/Pricing";

function Protected({children}) {
  return localStorage.getItem("token") ? children : <Navigate to="/login" replace />;
}

export default function App() {
  return <>
    <Navbar/>
    <Routes>
      <Route path="/" element={<Navigate to="/dashboard" replace/>}/>
      <Route path="/login" element={<Login/>}/>
      <Route path="/register" element={<Register/>}/>
      <Route path="/dashboard" element={<Protected><Dashboard/></Protected>}/>
      <Route path="/analytics" element={<Protected><Analytics/></Protected>}/>
      <Route path="/ai-coach" element={<Protected><AICoach/></Protected>}/>
      <Route path="/roadmap" element={<Protected><Roadmap/></Protected>}/>
      <Route path="/pricing" element={<Pricing/>}/>
      <Route path="*" element={<Navigate to="/dashboard" replace/>}/>
    </Routes>
  </>;
}
