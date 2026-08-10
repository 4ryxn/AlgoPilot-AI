import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { api } from "../api";

export default function Login() {
  const navigate = useNavigate();
  const [form, setForm] = useState({ email: "", password: "" });
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  async function submit(e) {
    e.preventDefault(); setError(""); setLoading(true);
    try {
      const data = await api("/login", { method: "POST", body: JSON.stringify(form) });
      localStorage.setItem("token", data.access_token);
      navigate("/dashboard");
    } catch (err) { setError(err.message) } finally { setLoading(false) }
  }

  return <div className="auth-page"><form className="auth-card" onSubmit={submit}>
    <h1>Welcome Back</h1><p className="muted">Login to your AlgoPilot-AI account</p>
    <label>Email</label><input type="email" required value={form.email} onChange={e => setForm({ ...form, email: e.target.value })} />
    <label>Password</label><input type="password" required value={form.password} onChange={e => setForm({ ...form, password: e.target.value })} />
    {error && <div className="alert">{error}</div>}
    <button className="button primary full" disabled={loading}>{loading ? "Logging in..." : "Login"}</button>
    <p className="center muted">No account? <Link to="/register">Create one</Link></p>
  </form></div>;
}
