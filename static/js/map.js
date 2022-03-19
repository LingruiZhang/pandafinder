//get the idea from https://developers.google.com/maps/documentation/javascript/adding-a-google-map
// Initialize and add the map
function initMap() {
  const lat = parseFloat(document.getElementById("lat").innerHTML);
  const lng = parseFloat(document.getElementById("lng").innerHTML);
  console.log(lng)
  const center = { lat: lat, lng: lng };
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 20,
    center: center,
  });

const marker = new google.maps.Marker({
  position: center,
  map: map,
});
}