async function predict() {
  const data = {
    gender: document.getElementById('gender').value,
    age: document.getElementById('age').value,
    bmi: document.getElementById('bmi').value,
    sleepTime: document.getElementById('sleepTime').value,
    bloodPressure: document.getElementById('bloodPressure').value,
    heartRate: document.getElementById('heartRate').value,
    stepsWalked: document.getElementById('stepsWalked').value
  };

  try {
    const response = await fetch('/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });

    if (response.ok) {
      const result = await response.json();
      document.getElementById('mood').innerText = `Mood: ${result.mood}`;
      document.getElementById('depressionRisk').innerText = `Depression Risk: ${result.depressionRisk}`;
    } else {
      alert(`Error occurred while fetching data: ${response.status}`);
    }
  } catch (error) {
    alert(`There was a problem with the fetch operation: ${error}`);
  }
}