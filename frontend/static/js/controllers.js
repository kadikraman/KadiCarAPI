(function(){

	'use strict'

	angular.module('kadiCarApp.controllers', [])
	.controller('LineChartCtrl', ['$scope', '$http', function LineChartCtrl($scope, $http){

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
		}])
	.controller('RawViewCtrl', ['$scope', function RawViewCtrl($scope){
		$scope.expense =  {
			id: 0,
			expense_type: "initial_purchase",
			amount: 1380,
			expense_date: "2013-11-06",
			mileage: 12345,
			litres: 35,
			comment: "this is a sample expense", 
		};
	}])
	.controller('TabsCtrl', ['$scope', function ($scope) {

		$scope.currentTab = 'about.tpl.html';

		$scope.onClickTab = function (tab) {
			$scope.currentTab = tab;
		}

		$scope.isActiveTab = function(tab) {
			return tab == $scope.currentTab;
		}
	}]);	

})();