import {useState} from "react";
import {Link,useNavigate} from "react-router-dom";
import {api} from "../api";

export default function Register(){
  const navigate=useNavigate();
  const [form,setForm]=useState({name:"",email:"",password:"",leetcode_username:"",linkedin_url:"",github_username:""});
  const [error,setError]=useState(""); const [loading,setLoading]=useState(false);
  const update=(k,v)=>setForm(x=>({...x,[k]:v}));

  async function submit(e){
    e.preventDefault();setError("");setLoading(true);
    try{await api("/register",{method:"POST",body:JSON.stringify(form)});navigate("/login")}
    catch(err){setError(err.message)}finally{setLoading(false)}
  }

  return <div className="auth-page"><form className="auth-card wide" onSubmit={submit}>
    <h1>Create Account</h1><p className="muted">Connect your coding profiles to AlgoPilot-AI.</p>
    <label>Name</label><input required value={form.name} onChange={e=>update("name",e.target.value)}/>
    <label>Email</label><input type="email" required value={form.email} onChange={e=>update("email",e.target.value)}/>
    <label>Password</label><input type="password" minLength="6" required value={form.password} onChange={e=>update("password",e.target.value)}/>
    <label>LeetCode Username</label><input placeholder="4ryxn" value={form.leetcode_username} onChange={e=>update("leetcode_username",e.target.value)}/>
    <label>LinkedIn URL</label><input placeholder="https://www.linkedin.com/in/aryan-singhal-ba1231332/" value={form.linkedin_url} onChange={e=>update("linkedin_url",e.target.value)}/>
    <label>GitHub Username</label><input placeholder="4ryxn" value={form.github_username} onChange={e=>update("github_username",e.target.value)}/>
    {error && <div className="alert">{error}</div>}
    <button className="button primary full" disabled={loading}>{loading?"Creating...":"Create Account"}</button>
    <p className="center muted">Already registered? <Link to="/login">Login</Link></p>
  </form></div>;
}
