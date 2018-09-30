function populationAtLocation(data, day, time) {

	populations = {}
	var curr_location;
	for(var building in data) {
	
		if(data[building].day == day && \ // Check if the day is the same
			data[building].begin <= time && \ // Check if time is after begin time
			time <= data[building].end) { // Check if time is before end time
				curr_location = data[building].center;
				curr_pop = data[building].population;
				if(curr_location in populations)  {
					populations[curr_location] += curr_pop;
				} else {
					populations[curr_location] = curr_pop;
				}
		}
	}	

	return populations
}