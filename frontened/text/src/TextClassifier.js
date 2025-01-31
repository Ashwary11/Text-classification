import React, { useState } from "react";
import axios from "axios";

const TextClassifier = () => {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);

  const handleSubmit = async () => {
    if (!text) return;

    try {
      const response = await axios.post("http://127.0.0.1:5000/predict", { text });
      setResult(response.data.prediction);
    } catch (error) {
      console.error("Error fetching prediction", error);
    }
  };

  return (
    <div className="container">
      <h2> Movie Review Classifier </h2>
      <textarea
        rows="4"
        placeholder="Enter text here..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <button onClick={handleSubmit}>Predict</button>
      {result && <h3>Prediction: {result}</h3>}
    </div>
  );
};

export default TextClassifier;
