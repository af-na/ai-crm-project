import React, { useState, useEffect } from "react";
import API from "./api";

function App() {
  const [form, setForm] = useState({
    hp_name: "",
    specialty: "",
    notes: "",
  });

  const [interactions, setInteractions] = useState([]);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const submitForm = async (e) => {
    e.preventDefault();
    await API.post("/chat", form);
    fetchInteractions();
    setForm({ hp_name: "", specialty: "", notes: "" });
  };

  const fetchInteractions = async () => {
    const res = await API.get("/interactions");
    setInteractions(res.data);
  };

  useEffect(() => {
    fetchInteractions();
  }, []);

  return (
    <div style={{ padding: "30px", fontFamily: "Arial" }}>
      <h1>AI CRM System</h1>

      <form onSubmit={submitForm}>
        <input
          name="hp_name"
          placeholder="Healthcare Professional Name"
          value={form.hp_name}
          onChange={handleChange}
          required
        />
        <br /><br />

        <input
          name="specialty"
          placeholder="Specialty"
          value={form.specialty}
          onChange={handleChange}
          required
        />
        <br /><br />

        <textarea
          name="notes"
          placeholder="Interaction Notes"
          value={form.notes}
          onChange={handleChange}
          required
        />
        <br /><br />

        <button type="submit">Save Interaction</button>
      </form>

      <h2>Saved Interactions</h2>
      <ul>
        {interactions.map((i) => (
          <li key={i.id}>
            <strong>{i.hp_name}</strong> ({i.specialty}) — {i.notes}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
