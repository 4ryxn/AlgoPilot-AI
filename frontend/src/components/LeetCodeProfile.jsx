import {useEffect,useState} from "react";
import {api} from "../api";
import Card from "./Card";

export default function LeetCodeProfile() {
  const [data,setData] = useState(null);
  const [error,setError] = useState("");

  useEffect(()=>{api("/leetcode/profile").then(setData).catch(e=>setError(e.message));},[]);

  if(error) return <div className="alert">LeetCode: {error}</div>;
  if(!data) return <div className="card">Loading LeetCode profile...</div>;

  const stats = data.stats?.acSubmissionNum || [];
  const total = stats.find(x=>x.difficulty==="All")?.count ?? 0;
  const easy = stats.find(x=>x.difficulty==="Easy")?.count ?? 0;
  const medium = stats.find(x=>x.difficulty==="Medium")?.count ?? 0;
  const hard = stats.find(x=>x.difficulty==="Hard")?.count ?? 0;

  return <section>
    <div className="section-heading">
      <div><h2>LeetCode Profile</h2><p className="muted">@{data.username}</p></div>
      <a className="button primary" href={`https://leetcode.com/u/${data.username}/`} target="_blank" rel="noreferrer">Open Profile</a>
    </div>
    <div className="stats-grid">
      <Card title="Total Solved" value={total}/><Card title="Easy" value={easy}/><Card title="Medium" value={medium}/><Card title="Hard" value={hard}/>
    </div>
    <div className="card profile-card">
      {data.profile?.userAvatar && <img className="avatar" src={data.profile.userAvatar} alt="LeetCode avatar"/>}
      <div><h3>{data.profile?.realName || data.username}</h3><p className="muted">{data.profile?.school || "LeetCode user"}</p><p className="muted">Global ranking: {data.profile?.ranking ?? "N/A"}</p></div>
    </div>
  </section>;
}
