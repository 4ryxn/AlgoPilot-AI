import {useEffect,useState} from "react";
import {api} from "../api";

export default function Roadmap(){
  const [items,setItems]=useState([]);
  useEffect(()=>{api("/dashboard/planner").then(d=>setItems(d.items))},[]);
  return <main className="page"><p className="eyebrow">PLANNER</p><h1>Your Roadmap</h1><p className="muted">Daily practice, revision and company preparation.</p>
    <div className="roadmap-grid">
      <div className="card"><h2>Daily Planner</h2>{items.map((x,i)=><div className="plan-item" key={i}><div><strong>{x.title}</strong><p className="muted">{x.topic} · {x.difficulty}</p></div><span className="badge">Today</span></div>)}</div>
      <div className="card"><h2>Company Roadmap</h2>{["Amazon","Microsoft","Google","Adobe","Flipkart"].map(x=><div className="plan-item" key={x}><div><strong>{x}</strong><p className="muted">DSA + interview preparation</p></div><span className="badge">Target</span></div>)}</div>
      <div className="card"><h2>Revision Planner</h2>{["Arrays","Trees","Graphs","DP"].map(x=><div className="plan-item" key={x}><strong>{x}</strong><span className="muted">Review this week</span></div>)}</div>
    </div>
  </main>;
}
