function populationAtLocation(data, day, time) {

	var populations = {}
	var curr_building;
    var curr_pop;
    var curr_location;
	for(var crn in data) {
	
        // Check if the day is the same
        // Check if time is after begin time
        // Check if time is before end time
		if(data[crn].Day.indexOf(day) > -1 && data[crn]["Start time"] <= time && time <= data[crn]["End time"]) { 
				curr_building = data[crn].Building;
				curr_pop = data[crn].Population;
				curr_location = data[crn].Location;
				if(curr_building in populations)  {
					populations[curr_building]["population"] += curr_pop;
				} else {
					populations[curr_building] = {}
					populations[curr_building]["population"] = curr_pop;
					populations[curr_building]["center"] = curr_location; 
				}
		}
	}	

	return populations
}