const hotelsEl = document.querySelector('.hotels')
const sightsEl = document.querySelector('.sights')
const restaurantsEl = document.querySelector('.restaurants')

const hotels = [{
    name: "Hilton",
    lat: 44.801938,
    lng: 20.466686
},{
    name: "Belgrade Inn",
    lat: 44.817981,
    lng: 20.462739
},{
    name: "Garni Hotel",
    lat: 44.819868,
    lng: 20.4619026
},{
    name: "Cricket 2",
    lat: 44.822494,
    lng: 20.4626116
},{
    name: "Novi Sad",
    lat: 45.23621,
    lng: 19.97314
}]

const sights = [{
    name: "Hilton",
    lat: 44.0,
    lng: 20.0
},{
    name: "Belgrade Inn",
    lat: 42.817981,
    lng: 21.462739
},{
    name: "Garni Hotel",
    lat: 40.819868,
    lng: 20.4619026
},{
    name: "Cricket 2",
    lat: 44.822494,
    lng: 21.4626116
},{
    name: "Novi Sad",
    lat: 45.23621,
    lng: 13.97314
}]

var map
var markerGroup
const showMap = (markers = null) => {
    
    if (!map) {
        map = new L.map('map', {
            center: [44.453, 20.083],
            zoom: 7
        })
    }

    markerGroup = L.layerGroup().addTo(map)

    if (markers) {
        for (let i = 0; i < markers.length; i++) {
            var marker = L.marker(markers[i]).addTo(markerGroup)
            marker.bindPopup(`${markers[i][2]}`)
        }
        var bounds = new L.LatLngBounds(markers)
        map.fitBounds(bounds)
    }
    
    const layer = new L.TileLayer(`http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png`);
    map.addLayer(layer)
    map.addLayer(markerGroup)
}

const showHotels = () => {
    const allHotels = []
    for (let i = 0; i < hotels.length; i++) {
        const hotel = [hotels[i].lat, hotels[i].lng, hotels[i].name]
        allHotels.push(hotel)
    }
    markerGroup.clearLayers()
    showMap(allHotels)
}

const showSights = () => {
    const allSights = []
    for (let i = 0; i < sights.length; i++) {
        const sight = [sights[i].lat, sights[i].lng, sights[i].name]
        allSights.push(sight)
    }
    markerGroup.clearLayers()
    showMap(allSights)
}

hotelsEl.addEventListener('click', () => {
    showHotels()
})

sightsEl.addEventListener('click', () => {
    showSights()
})

showMap()