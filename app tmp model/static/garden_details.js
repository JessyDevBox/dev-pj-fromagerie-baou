
window.gardenDetailsRunning = false;

function getGardenDetails(init=true) {
    const gardenId = document.getElementById("gardenId").value;
    if (!gardenId || !window.gardenDetailsRunning) return;
    const textTemperature = document.querySelector("#sensorTemperature .data-value");
    const textHumidity = document.querySelector("#sensorHumidity .data-value");

    const showGardenDetails = (data={}) => {
        textTemperature.innerHTML = (data.temperature || '...') + ' °C';
        textHumidity.innerHTML = (data.humidity || '...') + ' %';
    }
    showGardenDetails();

    const fetchHumidityTemperature = async() => {
        fetch('/sensor/humidity-temperature/' + gardenId)
        .then(response => response.json())
        .then(data => showGardenDetails(data))
        .catch(error => {
            console.error('Erreur:', error)
            showGardenDetails();
        });
    }
    if (init) {
        fetchHumidityTemperature();
    }
    setInterval(fetchHumidityTemperature, 5000);  // Rafraîchit toutes les 2 secondes
}

function setGardenDetailsRunning(run=false) {
    window.gardenDetailsRunning = run;
}


document.addEventListener("DOMContentLoaded", function() {
    // Void multiple doc loaded event;
    if (window.DocLoaded) return;
    window.DocLoaded = true;

    setGardenDetailsRunning(true);
    getGardenDetails();
});

