const API_BASE = import.meta.env.VITE_API_BASE_URL;

export function fetchData() {
  return fetch(`${API_BASE}/addMeal`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ key: "value" }),
  }).then(response => response.json());
}
