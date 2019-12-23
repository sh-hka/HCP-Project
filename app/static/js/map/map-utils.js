function centerMap(map, position) {
    map.panTo(position);
}

function placeMarker(map, title, position, content) {
    var marker = new google.maps.Marker({
        position: position,
        map: map,
        title: title,
    });
    markers.push(marker);

    google.maps.event.addListener(marker, 'click', function () {
        var infowindow = new google.maps.InfoWindow({content: content});

        infowindow.open(map, marker);
    })

    bounds.extend(marker.getPosition());
    map.fitBounds(bounds);
}

function clearMarkers() {
    for (var i = 0; i < markers.length; i++) {
        markers[i].setMap(null);
    }
    markers = [];
    bounds = new google.maps.LatLngBounds();
}