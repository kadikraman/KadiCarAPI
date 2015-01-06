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
	.controller('RawViewCtrl', ['$scope', '$http', function RawViewCtrl($scope, $http){

		$scope.currencySymbol = '£';
		
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
	// keeps track of which tab is currently selected
	// the appropriate .html fragment is served via ng-include in index.html
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