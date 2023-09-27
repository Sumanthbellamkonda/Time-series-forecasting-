<!DOCTYPE html>
<html>
<head>
    <title>Time Series Forecasting</title>
    <script type="text/javascript">
        function forecast() {
            // Get user input
            var Jan = parseFloat(document.getElementById('Jan').value);
            var feb = parseFloat(document.getElementById('feb').value);
            var mar = parseFloat(document.getElementById('mar').value);
            var apr = parseFloat(document.getElementById('apr').value);
            var may = parseFloat(document.getElementById('may').value);
            var jun = parseFloat(document.getElementById('jun').value);
            var jul = parseFloat(document.getElementById('jul').value);
            var aug = parseFloat(document.getElementById('aug').value);
            var sep = parseFloat(document.getElementById('sep').value);
            var oct = parseFloat(document.getElementById('oct').value);
            var nov = parseFloat(document.getElementById('nov').value);
            var dec = parseFloat(document.getElementById('dec').value);
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
    <label for="jan">January : </label>
    <input type="text" id="jan" placeholder="enter"><br><br>
    <label for="feb">February:</label>
    <input type="text" id="feb" placeholder="enter"><br><br>
    <label for="mar">March:</label>
    <input type="text" id="mar" placeholder="enter"><br><br>
    <label for="apr">April:</label>
    <input type="text" id="apr" placeholder="enter"><br><br>
    <label for="may">May:</label>
    <input type="text" id="may" placeholder="enter"><br><br>
    <label for="jun">June:</label>
    <input type="text" id="jun" placeholder="enter"><br><br>
    <label for="jul">July:</label>
    <input type="text" id="jul" placeholder="enter"><br><br>
    <label for="aug">August:</label>
    <input type="text" id="aug" placeholder="enter"><br><br>
    <label for="sep">September:</label>
    <input type="text" id="sep" placeholder="enter"><br><br>
    <label for="oct">Octomber:</label>
    <input type="text" id="oct" placeholder="enter"><br><br>
    <label for="nov">November:</label>
    <input type="text" id="nov" placeholder="enter"><br><br>
    <label for="dec">December:</label>
    <input type="text" id="dec" placeholder="enter"><br><br>
    <label for="data">Time Series Data (Total):</label>
    <input type="text" id="data" placeholder="12-months"><br><br>
    <button onclick="forecast()">Forecast</button><br><br>
    <div id="forecasted"></div>
</body>
</html>
