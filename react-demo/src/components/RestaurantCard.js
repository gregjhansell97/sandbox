import React from "react";
import PropTypes from "prop-types";
import {withStyles} from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import Typography from "@material-ui/core/Typography"; 

const styles = {
  card: {
    width: "50%"
  },
  title: {
    fontSize: 20,
    fontWeight: 500
  }
}


class RestaurantCard extends React.Component {
  render() {
    const {classes, name, description} = this.props;
    return (
      <Card className={classes.card}>
        <CardContent>
          <Typography className={classes.title} color="textSeceondary">
            {name}
          </Typography>
          <br />
          <Typography component="p"> 
            {description}
          </Typography>
        </CardContent> 
      </Card>
    );
  }
}

RestaurantCard.propTypes = {
  /**
   * styling information for the class
   */
  classes: PropTypes.object.isRequired,

  /**
   * name of the restaurant
   */
  name: PropTypes.string.isRequired,

  /**
   * description of restaurant
   */
  description: PropTypes.string.isRequired
}

export default withStyles(styles)(RestaurantCard);
