(function(){

	'use strict'

	angular.module('kadiCarApp.directives', [])
		.directive('barVisualisation', function(){
	  // constants
	  var margin = 50,
	    width = 1500,
	    height = 450;

	  return {
	    restrict: 'E',
	    scope: {
	      val: '=',
	      grouped: '='
	    },
	    link: function (scope, element, attrs) {

	      // set up initial svg object
	      var vis = d3.select(element[0])
	        .append("svg")
	          .attr("width", width)
	          .attr("height", height + margin + 100);

	      scope.$watch('val', function (newVal, oldVal) {

	        vis.selectAll('*').remove();

	        // val is the data for the visualisation
	        // if 'val' is falsy (undefined, false, NaN, null, 0, ""), exit
	        if (!newVal) {
	          return;
	        }

	        var data = newVal;
	        var svg = d3.select("svg");
	        var format = d3.time.format("%Y-%m-%d");
			
			var myChart = new dimple.chart(svg, data);
			myChart.setBounds(70, 30, 1000, 500)
			var x = myChart.addTimeAxis("x", "expense_date", "%Y-%m-%d", "%m-%Y");
			x.showGridlines = true;
			x.addOrderRule("expense_date");
			var y = myChart.addMeasureAxis("y", "amount");
			var s = myChart.addSeries(["expense_type"], dimple.plot.line);
			s.lineWeight = 4;
			s.lineMarkers = true;
			var myLegend = myChart.addLegend(1200, 100, 60, 300, "Right");
			myChart.draw();

			// This is a critical step.  By doing this we orphan the legend. This
	        // means it will not respond to graph updates.  Without this the legend
	        // will redraw when the chart refreshes removing the unchecked item and
	        // also dropping the events we define below.
	        myChart.legends = [];

	        // This block simply adds the legend title. I put it into a d3 data
	        // object to split it onto 2 lines.  This technique works with any
	        // number of lines, it isn't dimple specific.
	        svg.selectAll("title_text")
	          .data(["Click legend to","show/hide types of expense:"])
	          .enter()
	          .append("text")
	            .attr("x", 1150)
	            .attr("y", function (d, i) { return 90 + i * 14; })
	            .style("font-family", "sans-serif")
	            .style("font-size", "10px")
	            .style("color", "Black")
	            .text(function (d) { return d; });

	        // Get a unique list of Owner values to use when filtering
	        var filterValues = dimple.getUniqueValues(data, "expense_type");
	        // Get all the rectangles from our now orphaned legend
	        myLegend.shapes.selectAll("rect")
	          // Add a click event to each rectangle
	          .on("click", function (e) {
	            // This indicates whether the item is already visible or not
	            var hide = false;
	            var newFilters = [];
	            // If the filters contain the clicked shape hide it
	            filterValues.forEach(function (f) {
	              if (f === e.aggField.slice(-1)[0]) {
	                hide = true;
	              } else {
	                newFilters.push(f);
	              }
	            });
	            // Hide the shape or show it
	            if (hide) {
	              d3.select(this).style("opacity", 0.2);
	            } else {
	              newFilters.push(e.aggField.slice(-1)[0]);
	              d3.select(this).style("opacity", 0.8);
	            }
	            // Update the filters
	            filterValues = newFilters;
	            // Filter the data
	            myChart.data = dimple.filterData(data, "expense_type", filterValues);
	            // Passing a duration parameter makes the chart animate. Without
	            // it there is no transition
	            myChart.draw(800);
	        });
	      }); // end of scope.$watch('val' ...)
	    }
	  }
	});

})();