const API_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

export async function api(path, options = {}) {
  const token = localStorage.getItem("token");
  const headers = {"Content-Type": "application/json", ...(options.headers || {})};
  if (token) headers.Authorization = `Bearer ${token}`;

  const response = await fetch(`${API_URL}${path}`, {...options, headers});
  const data = await response.json().catch(() => ({}));
  if (!response.ok) throw new Error(data.detail || "Request failed");
  return data;
}
export { API_URL };
