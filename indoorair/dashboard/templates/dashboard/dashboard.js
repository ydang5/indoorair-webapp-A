function getDashboardApi(){
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      const dataString = this.responseText
      const dataObj = JSON.parse(dataString)
      document.getElementById('averageTemperature').innerHTML = dataObj.average_temperature;
      document.getElementById('averagePressure').innerHTML = dataObj.average_pressure;
      document.getElementById('averageCo2').innerHTML = dataObj.average_co2;
      document.getElementById('averageTvoc').innerHTML = dataObj.average_tvoc;
      document.getElementById('averageHumidity').innerHTML = dataObj.average_humidity;
    }
  };
  xhttp.open('GET', "{% url 'dashboard_api' %}", true);
  xhttp.send();
}

getDashboardApi();

function createInsrtument(){
  window.location.href = "/instrument/create";
}


function listInsrtument(){
  window.location.href = "/instrument/list";
}


function retrieveInsrtument(){
  window.location.href = "/instrument/retrieve";
}


function updateInsrtument(){
  window.location.href = "/instrument/update";
}
