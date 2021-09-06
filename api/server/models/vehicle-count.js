'use strict';

module.exports = function(Vehiclecount) {

  Vehiclecount.getVehicleCountByRoadId = async function(id) {
    const crossRoad = await Vehiclecount.app.models.cross_road.findOne({
      cross_road_id: id,
    });
    const vehicleCountData = await Vehiclecount.find({
      where: {
        cross_road_id: id,
      },
    });
    console.log(crossRoad);
    console.log(vehicleCountData);
    return {
      type: {
        crossRoadDetails: crossRoad,
        vehicleCountDetails: vehicleCountData,
      }, root: true,
    };
  };

  Vehiclecount.remoteMethod('getVehicleCountByRoadId', {
    accepts: {
      arg: 'id',
      type: 'string',
    },
    returns: {
      arg:'object',
      type: 'object',
      root: true,
    },
    http: {path: '/getVehicleCountByRoadId/:id', verb: 'post'},
    'description': 'Fetch Vehicle Count Data along with crossroad data by using Road Id',
  });

};
