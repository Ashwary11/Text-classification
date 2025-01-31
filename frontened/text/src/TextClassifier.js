import React, { useState } from "react";
import axios from "axios";

const TextClassifier = () => {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);

  const handleTextChange = (e) => {
    const newText = e.target.value;
    setText(newText);

    // Clear the prediction when input is empty
    if (newText.trim() === "") {
      setResult(null);
    }
  };

  const handleSubmit = async () => {
    if (!text.trim()) {
      setResult(null); // Ensure prediction is cleared when empty
      return;
    }

    try {
      const response = await axios.post("http://127.0.0.1:5000/predict", { text });
      setResult(response.data.prediction);
    } catch (error) {
      console.error("Error fetching prediction", error);
      setResult("Error fetching prediction");
    }
  };

  return (
    <div className="container">
      <h2> Movie Review Classifier </h2>
      <textarea
        rows="4"
        placeholder="Enter text here..."
        value={text}
        onChange={handleTextChange} // Updated function
      />
      <button onClick={handleSubmit}>Predict</button>
      {result && <h3>Prediction: {result}</h3>}
    </div>
  );
};

export default TextClassifier;

