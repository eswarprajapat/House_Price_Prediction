function getBathValue(){
   var uiBathrooms = document.getElementsByName("uiBathrooms");
   for(let i=0; i<uiBathrooms.length; i++){
      if(uiBathrooms[i].checked){
             return parseInt(uiBathrooms[i].value);
      }
 }
return -1;
}
function getBHKValue(){
  var uiBHK = document.getElementsByName("uiBHK");
  for(let i=0; i<uiBHK.length; i++){
     if(uiBHK[i].checked){
        return parseInt(uiBHK[i].value);
   }
}
return -1;

}
  
function onClickedEstimateprice(){
    console.log("Estimate price button clicked");
    var sqft = document.getElementById("uiSqft");
    var bhk = getBHKValue();
    var bathrooms = getBathValue();
    var location = document.getElementById("uiLocations");
    var estprice = document.getElementById("uiEstimatedPrice");
    var url = "http://127.0.0.1:5000/home_price";
    $.post(url,{
       sqft:parseFloat(sqft.value),
       bhk:bhk,
       bath:bathrooms,
       location:location.value
    },function(data,status){
       console.log(data.estimated_predict);
       estprice.innerHTML=        "<h2>"+data.estimated_predict.toString()+"lakh</h2>";
       console.log(status);

});
}
function onPageLoad(){
  console.log("document loaded");
  var url="http://127.0.0.1:5000/get_location_names";
  $.get(url,function(data,status){
  console.log("got response for get_location_names request");
  if(data){
    var locations = data.location;
    var uiLocations = document.getElementById("uiLocations");
    $('#uiLocations').empty();
    for(var i in locations){
        var opt = new Option(locations[i]);
        $('#uiLocations').append(opt);
}
}
});
}

window.onload = onPageLoad;
