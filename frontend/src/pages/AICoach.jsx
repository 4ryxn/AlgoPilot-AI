import {useState} from "react";
import ReactMarkdown from "react-markdown";
import {api} from "../api";

export default function AICoach(){
  const [mode,setMode]=useState("coach");const [message,setMessage]=useState("");const [answer,setAnswer]=useState("");const [loading,setLoading]=useState(false);
  const modeLabels={coach:"Coach Mode",review:"Review Mode",hint:"Hint Mode",interview:"Interview Mode"};
  async function ask(e){e.preventDefault();if(!message.trim())return;setLoading(true);try{const d=await api("/dashboard/ai",{method:"POST",body:JSON.stringify({message,mode})});setAnswer(d.answer)}catch(e){setAnswer(e.message)}finally{setLoading(false)}}
  return <main className="page"><p className="eyebrow">AI FEATURES</p><h1>AI Coach</h1><p className="muted">Coach, review code, generate hints and practice interviews.</p>
    <div className="mode-tabs">{[["coach","AI Coach"],["review","Code Review"],["hint","Hint Generator"],["interview","AI Interviewer"]].map(([v,l])=><button key={v} className={mode===v?"tab active":"tab"} onClick={()=>setMode(v)}>{l}</button>)}</div>
    <form className="card" onSubmit={ask}><label>Your question / code / problem</label><textarea rows="10" placeholder="Paste your problem or code here..." value={message} onChange={e=>setMessage(e.target.value)}/><button className="button primary" disabled={loading}>{loading?"Thinking...":"Get AI Help"}</button></form>
    {answer&&<div className="card ai-answer"><div className="ai-answer-head"><h2>Coach Response</h2><span className="badge">{modeLabels[mode]}</span></div><div className="markdown-body markdown-content"><ReactMarkdown skipHtml>{answer}</ReactMarkdown></div></div>}
  </main>;
}
