import { useState } from "react";
import "./App.css";

function App() {
  const [reportText, setReportText] = useState("");
  const [explanation, setExplanation] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setExplanation("");

    try {
      const res = await fetch("http://localhost:8000/explain_lab_report", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ report_text: reportText }),
      });
      const data = await res.json();
      setExplanation(data.explanation);
    } catch (err) {
      setExplanation("Error: " + err.message);
    }

    setLoading(false);
  };

  return (
    <div className="container">
      <h1>Lab Report Explainer</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          rows={8}
          placeholder="Paste your lab report here..."
          value={reportText}
          onChange={(e) => setReportText(e.target.value)}
          className="textarea"
          required
        />
        <button className="button" disabled={loading}>
          {loading ? "Explaining..." : "Explain Lab Report"}
        </button>
      </form>

      {explanation && (
        <div className="result-box">
          {explanation}
        </div>
      )}
    </div>
  );
}

export default App;
