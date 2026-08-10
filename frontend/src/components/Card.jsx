export default function Card({title,value,subtitle}) {
  return <div className="card"><div className="muted">{title}</div><div className="metric">{value}</div>{subtitle && <div className="muted small">{subtitle}</div>}</div>;
}
