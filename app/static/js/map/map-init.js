var map;
var markers = [];

function initMap() {
    const styledMapType = new google.maps.StyledMapType(
        map_style,
        {name: 'Map'}
    );
    const mapElem = document.getElementById('map');
    map = new google.maps.Map(
        mapElem,
        {
            center: new google.maps.LatLng(0, 0),
            zoom: 12,
            mapTypeControlOptions: {
                mapTypeIds: ['Map']
            }
        }
    );
    map.mapTypes.set('Map', styledMapType);
    map.setMapTypeId('Map');
    centerMap(map, currentPos);

    navigator.geolocation.getCurrentPosition(function (position) {
        centerMap(map, position);
    });
}