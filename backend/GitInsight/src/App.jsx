import { useState } from "react";
import axios from "axios";

function App() {
  const [url, setUrl] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");

  const analyzeProfile = async () => {
    if (!url.trim()) {
      alert("Please enter a GitHub profile URL");
      return;
    }

    setLoading(true);
    setResult(null);
    setErrorMessage("");

    try {
      const response = await axios.post(
        "http://localhost:8000/api/analyze/",
        { url }
      );

      setResult(response.data);
    } catch (error) {
      if (error.response && error.response.data.error) {
        setErrorMessage(error.response.data.error);
      } else {
        setErrorMessage("Something went wrong. Please try again.");
      }
    }

    setLoading(false);
  };

  return (
    <div
      style={{
        padding: "60px",
        fontFamily: "Arial",
        maxWidth: "900px",
        margin: "auto",
      }}
    >
      <h1 style={{ fontSize: "48px", marginBottom: "10px" }}>
        GitInsight
      </h1>

      <h2 style={{ marginBottom: "20px", fontWeight: "normal" }}>
        GitHub Portfolio Analyzer
      </h2>

      <p style={{ marginBottom: "30px", color: "#555" }}>
        Analyze your GitHub profile from a recruiter’s perspective and
        receive structured portfolio feedback in seconds.
      </p>

      <div style={{ marginBottom: "30px" }}>
        <input
          type="text"
          placeholder="Enter GitHub Profile URL"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          style={{
            width: "500px",
            padding: "12px",
            fontSize: "16px",
          }}
        />

        <button
          onClick={analyzeProfile}
          style={{
            marginLeft: "10px",
            padding: "12px 25px",
            fontSize: "16px",
            cursor: "pointer",
          }}
        >
          Analyze
        </button>
      </div>

      {loading && <p>Analyzing profile...</p>}

      {errorMessage && (
        <p style={{ color: "red", marginTop: "20px" }}>
          {errorMessage}
        </p>
      )}

      {result && (
        <div style={{ marginTop: "40px" }}>
          <h2 style={{ fontSize: "36px", marginBottom: "20px" }}>
            GitHub Portfolio Score: {result.score || 0}/100
          </h2>

          <hr style={{ margin: "30px 0" }} />

          <h3>Profile Overview</h3>
          <p>
            <strong>Total Repositories:</strong>{" "}
            {result.total_repos ?? 0}
          </p>
          <p>
            <strong>Total Stars:</strong>{" "}
            {result.stars ?? 0}
          </p>
          <p>
            <strong>Languages Used:</strong>{" "}
            {result.languages && result.languages.length > 0
              ? result.languages.join(", ")
              : "Not detected"}
          </p>

          <hr style={{ margin: "30px 0" }} />

          <h3>Actionable Recommendations</h3>
          <ul>
            {result.suggestions &&
              result.suggestions.map((s, index) => (
                <li key={index} style={{ marginBottom: "10px" }}>
                  🔹 {s}
                </li>
              ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
