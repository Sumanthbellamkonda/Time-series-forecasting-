<!DOCTYPE html>
<html>
<head>
    <title>Time Series Forecasting</title>
</head>
<body>
    <h1>Time Series Forecasting</h1>
    <label for="alpha">Alpha:</label>
    <input type="text" id="alpha" placeholder="0.2"><br><br>
    <label for="beta">Beta:</label>
    <input type="text" id="beta" placeholder="0.2"><br><br>
    <label for="gamma">Gamma:</label>
    <input type="text" id="gamma" placeholder="0.2"><br><br>
    <button onclick="forecast()">Forecast</button><br><br>
    <div id="forecasted"></div>

    <script>
        function forecast() {
            var alpha = document.getElementById('alpha').value;
            var beta = document.getElementById('beta').value;
            var gamma = document.getElementById('gamma').value;

            fetch('/forecast', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    alpha: parseFloat(alpha),
                    beta: parseFloat(beta),
                    gamma: parseFloat(gamma)
                })
            })
            .then(response => response.json())
            .then(result => {
                document.getElementById('forecasted').textContent = "Forecasted Values: " + result.forecast.join(', ');
            })
            .catch(error => {
                console.error(error);
            });
        }
    </script>
</body>
</html>
