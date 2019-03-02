import React from 'react';
import PropTypes from "prop-types";

//inhouse
import RestaurantCard from "./RestaurantCard"
import AppBar from './AppBar';

class Root extends React.Component {

    render() {
        
        let restaurants = [
            {name:'kekes', description:'tacos'}, 
            {name:'chipotle', description: 'burritos'}, 
            {name:'Qdoba', description: 'ripoff chipotle'}, 
            {name:'Moes', description: 'more burritos and shit'}, 
            {name:'Taco Bell', description: 'shit'}
        ];

        return (
            <div>
                <div>
                    <AppBar name="Restaurants"></AppBar>
                </div>
                <div>
                    {restaurants.map((r) =>
                        <RestaurantCard name={r.name} description={r.description}></RestaurantCard>
                    )
                    }
                </div>
            </div>
        );
    }
}

export default Root;
