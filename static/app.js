async function planTrip() {
  const request = document.getElementById("request").value.trim();
  const output = document.getElementById("output");
  if (!request) return;
  output.textContent = "Planning...";
  const res = await fetch("/api/travel", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({message: request})
  });
  const data = await res.json();
  output.textContent = data.plan || JSON.stringify(data, null, 2);
}
