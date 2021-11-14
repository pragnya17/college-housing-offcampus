// Adapted from https://developers.google.com/maps/documentation/javascript/overview#maps_map_simple-javascript
// and https://developers.google.com/maps/documentation/javascript/examples/places-searchbox#maps_places_searchbox-html
// and https://www.freecodecamp.org/news/how-to-change-javascript-google-map-marker-color-8a72131d1207/

let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 38.034493639911936, lng: -78.50999182771713 },
    zoom: 15,
  });
    // Create the search box and link it to the UI element.
  const input = document.getElementById("search-bar");
  const searchBox = new google.maps.places.SearchBox(input);

  // Bias the SearchBox results towards current map's viewport.
  map.addListener("bounds_changed", () => {
    searchBox.setBounds(map.getBounds());
  });

  // store all locations that have been entered so far
  let markers = [];

  // Listen for the event fired when the user selects a prediction and retrieve
  // more details for that place.
  searchBox.addListener("places_changed", () => {
    const places = searchBox.getPlaces();

    if (places.length == 0) {
      return;
    }

    // For each place, get the icon, name and location.
    const bounds = new google.maps.LatLngBounds();

    places.forEach((place) => {
      if (!place.geometry || !place.geometry.location) {
        console.log("Returned place contains no geometry");
        return;
      }

      // Create a marker for each place.
      markers.push(
        new google.maps.Marker({
          map,
          icon: {url: "http://maps.google.com/mapfiles/ms/icons/pink-dot.png"},
          title: place.name,
          position: place.geometry.location,
        })
      );
    // get general location
    bounds.union(place.geometry.viewport);
    // get specific location
    bounds.extend(place.geometry.location);
    });
    // resize map bounds based on markers' locations
    map.fitBounds(bounds);
  });
}
