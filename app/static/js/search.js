
const search_bar = document.getElementById("search-bar");

// Init the SearchBar actions
function initSearchBar() {
    search_bar.onkeydown = function (event) {
        if (event.keyCode === 13) {
            event.preventDefault();
            search_bar.blur();
            search(search_bar);
        }
    };
}

function search() {
    console.log('search()');
    const query_string = search_bar.querySelector('#query').value;
    const cLatLng = currentPos;
    var range = 30; // Stub
    const range_option = search_bar.querySelector('#search_range');
    if (range_option !== null) {
        const range = range_option.value;
    }
    var query = JSON.stringify({query: query_string, position: cLatLng, range: range});
    // Now construct the query url:
    const url = '/search?data=' + encodeURIComponent(query);
    window.location = url;
}


var map;
function placeMarkerMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 2,
    center: new google.maps.LatLng(2.8,-187.3),
    mapTypeId: 'terrain'
  });

  // Create a <script> tag and set the USGS URL as the source.
  var script = document.createElement('script');
  // This example uses a local copy of the GeoJSON stored at
  // http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.geojsonp
  // script.src = 'https://developers.google.com/maps/documentation/javascript/examples/json/earthquake_GeoJSONP.js';
  document.getElementsByTagName('head')[0].appendChild(script);
}

// Loop through the results array and place a marker for each
// set of coordinates.
  window.eqfeed_callback = function(results) {
    for (var i = 0; i < results.features.length; i++) {
      var coords = results.features[i].geometry.coordinates;
      var latLng = new google.maps.LatLng(coords[1],coords[0]);
      var marker = new google.maps.Marker({
        position: latLng,
        map: map
      });
    }
  }
</script>
<script async defer
src="https://maps.googleapis.com/maps/api/js?key=gmaps_api_key&callback=initMap">
</script>


