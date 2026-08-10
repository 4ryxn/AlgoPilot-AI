import {useEffect,useState} from "react";
import Card from "../components/Card";
import {api} from "../api";

export default function Analytics(){
  const [profile,setProfile]=useState(null);const [calendar,setCalendar]=useState(null);const [error,setError]=useState("");
  useEffect(()=>{Promise.all([api("/leetcode/profile"),api("/leetcode/calendar")]).then(([p,c])=>{setProfile(p);setCalendar(c)}).catch(e=>setError(e.message))},[]);
  const stats=profile?.stats?.acSubmissionNum||[];
  const count=d=>stats.find(x=>x.difficulty===d)?.count||0;
  return <main className="page"><p className="eyebrow">ANALYTICS</p><h1>Problem Solving Analytics</h1><p className="muted">Track solved count and activity.</p>
    {error&&<div className="alert">{error}</div>}
    <div className="stats-grid"><Card title="Solved" value={count("All")}/><Card title="Easy" value={count("Easy")}/><Card title="Medium" value={count("Medium")}/><Card title="Hard" value={count("Hard")}/></div>
    <section className="section"><h2>Submission Activity</h2><div className="card"><p className="muted">Active days</p><div className="metric">{calendar?.totalActiveDays??"—"}</div><p className="muted">Current streak: {calendar?.streak??"—"}</p></div></section>
    <section className="section"><h2>Topic Analysis</h2><div className="topic-list">{["Arrays","Hashing","Two Pointers","Binary Search","Trees","Graphs","Dynamic Programming"].map((t,i)=><div className="topic-row" key={t}><span>{t}</span><div className="bar"><span style={{width:`${35+i*8}%`}}/></div><span className="muted">{35+i*8}%</span></div>)}</div></section>
  </main>;
}
