// module for custom directives
var kadiCarApp = angular.module('kadiCarApp', []);

// constroller business logic
kadiCarApp.controller('AppCtrl', ['$scope', '$http', function AppCtrl($scope, $http){

	$scope.getAllExpenses = function(){
		$http.get('/data/all_expenses')
			.success(function(results){
				// assign the result to a scope variable
				$scope.data = results;
			})
	}
	// wrapping this in an if statement to prevent continuous calls to this function
	if(!$scope.data){
		$scope.getAllExpenses();
	}
}]);

kadiCarApp.directive('barVisualisation', function(){

  // constants
  var margin = 50,
    width = 1600,
    height = 1300;

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

      }); // end of scope.$watch('val' ...)
    }
  }
});