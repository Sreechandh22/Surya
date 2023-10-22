async function submitData() {
  const data = {
    gender: document.getElementById('gender').value,
    age: document.getElementById('age').value,
    bloodPressure: document.getElementById('bloodPressure').value,
    sleepTime: document.getElementById('sleepTime').value,
    heartRate: document.getElementById('heartRate').value,
    stepsWalked: document.getElementById('stepsWalked').value
  };

  try {
    const response = await fetch('http://127.0.0.1:5000/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });

    if (!document.getElementById('sleepTime').value) {
      alert('Please fill out the sleep time.');
      return;
    }

    if (response.ok) {
      const result = await response.json();
      document.getElementById('result').innerText = `Mood: ${result.mood}, Depression Risk: ${result.depressionRisk}`;
      
    } else {
      document.getElementById('result').innerText = 'Error occurred while fetching data.';
    }
  } catch (error) {
    console.error('There was a problem with the fetch operation:', error);
  }
}
