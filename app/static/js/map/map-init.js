var map;
var markers = [];
var bounds = null;

function initMap() {
  const styledMapType = new google.maps.StyledMapType(map_style, {
    name: "Map"
  });
  const mapElem = document.getElementById("map");
  map = new google.maps.Map(mapElem, {
    center: new google.maps.LatLng(0, 0),
    zoom: 12,
    mapTypeControlOptions: {
      mapTypeIds: ["Map"]
    }
  });
  map.mapTypes.set("Map", styledMapType);
  map.setMapTypeId("Map");
  centerMap(map, currentPos);

  navigator.geolocation.getCurrentPosition(function(position) {
    currentPos = {
      lat: position.coords.latitude,
      lng: position.coords.longitude
    };
    centerMap(map, currentPos);
  });
  bounds = new google.maps.LatLngBounds();
}
