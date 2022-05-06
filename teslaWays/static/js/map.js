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

const showMap = (markers = null) => {
    const mapOptions = {
        center: [44.453, 20.083],
        zoom: 7
    }
    
    const map = new L.map('map', mapOptions)

    if (markers) {
        for (let i = 0; i < markers.length; i++) {
            L.marker(markers[i]).addTo(map)
        }
    }
    
    const layer = new L.TileLayer(`http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png`);
    map.addLayer(layer);   
    
}

const showHotels = () => {
    const allHotels = []
    for (let i = 0; i < hotels.length; i++) {
        const hotel = [hotels[i].lat, hotels[i].lng]
        allHotels.push(hotel)
    }
    showMap(allHotels)
}

hotelsEl.addEventListener('click', () => {
    showHotels()
})

showMap()


// const mapOptions = {
//     center: [44.80446, 20.46578],
//     zoom: 15
// }
    
// const map = new L.map('map', mapOptions);
// const marker = L.marker([44.80446, 20.46578]).addTo(map);
// const layer = new L.TileLayer(`http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png`);

// map.addLayer(layer);