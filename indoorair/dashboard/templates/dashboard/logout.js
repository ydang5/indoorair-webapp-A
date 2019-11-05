function onLoginClick(){
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function(){
    if(this.readyState == 4 && this.status == 200){
      window.location.href = "/api/logout"
    }
  }
  xhttp.open("GET","/api/logout", true);
  xhttp.send()
}
