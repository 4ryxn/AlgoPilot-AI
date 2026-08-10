import {Link, useNavigate} from "react-router-dom";

export default function Navbar() {
  const navigate = useNavigate();
  const loggedIn = !!localStorage.getItem("token");

  function logout() {
    localStorage.removeItem("token");
    navigate("/login");
  }

  return <nav className="navbar">
    <Link to="/dashboard" className="brand">
      <span className="brand-logo">AP</span> AlgoPilot-AI
    </Link>
    <div className="nav-links">
      {loggedIn && <Link to="/dashboard">Dashboard</Link>}
      {loggedIn && <Link to="/analytics">Analytics</Link>}
      {loggedIn && <Link to="/ai-coach">AI Coach</Link>}
      {loggedIn && <Link to="/roadmap">Roadmap</Link>}
      <Link to="/pricing">Pricing</Link>
    </div>
    <div className="nav-actions">
      {loggedIn ? <button className="button ghost" onClick={logout}>Logout</button> :
      <><Link className="button ghost" to="/login">Login</Link><Link className="button primary" to="/register">Get Started</Link></>}
    </div>
  </nav>;
}
