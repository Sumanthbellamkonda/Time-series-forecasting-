<!DOCTYPE html>
<html>
<head>
    <title>Time Series Forecasting</title>
    <script type="text/javascript">
        function forecast() {
            // Get user input
            var alpha = parseFloat(document.getElementById('alpha').value);
            var beta = parseFloat(document.getElementById('beta').value);
            var gamma = parseFloat(document.getElementById('gamma').value);
            var data = document.getElementById('data').value.split(',').map(parseFloat);

            // Send input to the server for forecasting
            fetch('/forecast', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    alpha: alpha,
                    beta: beta,
                    gamma: gamma,
                    data: data
                })
            })
            .then(response => response.json())
            .then(result => {
                // Display the forecasted values
                document.getElementById('forecasted').textContent = "Forecasted Values: " + result.forecast.join(', ');
            });
        }
    </script>
</head>
<body>
    <h1>Time Series Forecasting</h1>
    <label for="alpha">January : </label>
    <input type="text" id="alpha" placeholder="0.2"><br><br>
    <label for="beta">February:</label>
    <input type="text" id="beta" placeholder="0.2"><br><br>
    <label for="gamma">March:</label>
    <input type="text" id="gamma" placeholder="0.2"><br><br>
    <label for="alpha">April:</label>
    <input type="text" id="alpha" placeholder="0.2"><br><br>
    <label for="beta">May:</label>
    <input type="text" id="beta" placeholder="0.2"><br><br>
    <label for="gamma">June:</label>
    <input type="text" id="gamma" placeholder="0.2"><br><br>
    <label for="alpha">July:</label>
    <input type="text" id="alpha" placeholder="0.2"><br><br>
    <label for="beta">August:</label>
    <input type="text" id="beta" placeholder="0.2"><br><br>
    <label for="gamma">September:</label>
    <input type="text" id="gamma" placeholder="0.2"><br><br>
    <label for="alpha">Octomber:</label>
    <input type="text" id="alpha" placeholder="0.2"><br><br>
    <label for="beta">November:</label>
    <input type="text" id="beta" placeholder="0.2"><br><br>
    <label for="gamma">December:</label>
    <input type="text" id="gamma" placeholder="0.2"><br><br>
    <label for="data">Time Series Data (comma-separated):</label>
    <input type="text" id="data" placeholder="1,2,3,4,5"><br><br>
    <button onclick="forecast()">Forecast</button><br><br>
    <div id="forecasted"></div>
</body>
</html>
