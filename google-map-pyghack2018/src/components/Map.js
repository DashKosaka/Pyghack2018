import React, { Component } from 'react';
import { withGoogleMap, GoogleMap } from 'react-google-maps';

class Map extends Component {
    render() {
        const GoogleMapExample = withGoogleMap(props => (
            <GoogleMap
                defaultCenter = { { lat: 40.1164, lng: 88.2434 } }
                defaultZoom = { 13 }
            >
            </GoogleMap>
        ));
        return(
            <div>
                <GoogleMapExample
                    containerElement={ <div style={{ height: `500px`, width: '500px' }} /> }
                    mapElement={ <div style={{ height: `100%` }} /> }
                />
            </div>
        );
    }
};
export default Map;