import React from 'react';
import PropTypes from "prop-types";

//inhouse
import RestaurantCard from "./RestaurantCard"

class Root extends React.Component {
  render() {
    return (
      <RestaurantCard name="Moes" description="burrito place"/>
    );
  }
}

export default Root;
