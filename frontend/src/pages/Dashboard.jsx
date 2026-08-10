import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import Card from "../components/Card";
import LeetCodeProfile from "../components/LeetCodeProfile";
import { api } from "../api";

export default function Dashboard() {
  const navigate = useNavigate(); const [user, setUser] = useState(null); const [github, setGithub] = useState(null); const [error, setError] = useState("");
  useEffect(() => {
    Promise.all([api("/me"), api("/github/profile").catch(() => null)])
      .then(([me, gh]) => { setUser(me); setGithub(gh) })
      .catch(err => { localStorage.removeItem("token"); setError(err.message); navigate("/login") });
  }, [navigate]);

  if (error) return <main className="page"><div className="alert">{error}</div></main>;
  if (!user) return <main className="page"><div className="card">Loading dashboard...</div></main>;

  return <main className="page">
    <div className="hero-row"><div><p className="eyebrow">PERSONAL DASHBOARD</p><h1>Welcome, {user.name} 👋</h1><p className="muted">Your coding progress, analytics and AI coaching in one place.</p></div>
      <div className="card compact"><div className="muted">LinkedIn</div>{user.linkedin_url ? <a href={user.linkedin_url} target="_blank" rel="noreferrer">View profile</a> : <span className="muted">Not connected</span>}</div>
    </div>
    <div className="stats-grid">
      <Card title="Account" value="Active" subtitle={user.email} /><Card title="LeetCode" value={user.leetcode_username || "—"} /><Card title="GitHub" value={user.github_username || "—"} /><Card title="Coach" value="Ready" subtitle="AI coaching tools" />
    </div>
    <LeetCodeProfile />
    {github && <section className="section"><div className="section-heading"><div><h2>GitHub</h2><p className="muted">Public profile synchronization</p></div><a className="button ghost" href={github.html_url} target="_blank" rel="noreferrer">Open GitHub</a></div>
      <div className="stats-grid"><Card title="Repositories" value={github.public_repos} /><Card title="Followers" value={github.followers} /><Card title="Following" value={github.following} /></div>
      <div className="repo-grid">{github.repositories?.map(r => <a className="card repo" key={r.name} href={r.url} target="_blank" rel="noreferrer"><h3>{r.name}</h3><p className="muted">{r.language || "No language"} · ⭐ {r.stars}</p></a>)}</div>
    </section>}
  </main>;
}
