export default function Pricing(){
  const plans=[["Free","₹0",["LeetCode profile","Basic dashboard","GitHub sync"]],["Pro","₹299/mo",["Advanced analytics","AI Coach","Planner","Reports"]],["Career","₹599/mo",["Everything in Pro","Interview practice","Company roadmap"]]];
  return <main className="page"><div className="center-head"><p className="eyebrow">PRICING</p><h1>Choose your plan</h1><p className="muted">Start free and upgrade when needed.</p></div>
    <div className="pricing-grid">{plans.map(([n,p,f])=><div className="card price-card" key={n}><h2>{n}</h2><div className="price">{p}</div>{f.map(x=><p key={x}>✓ {x}</p>)}<button className="button primary full">Choose {n}</button></div>)}</div>
  </main>;
}
