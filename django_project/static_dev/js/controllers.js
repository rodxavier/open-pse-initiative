'use strict';

var controllers = angular.module('openPSEControllers', []);
controllers.controller('QuoteDownloadsController', function ($scope, $http) {
    $scope.objs = [];
    $scope.total = 0;
    $scope.objsPerPage = 15;
    getResultsPage(1);

    $scope.pagination = {
        current: 1
    };
    
    $scope.pageChanged = function(newPage) {
        getResultsPage(newPage);
    };
    
    function getResultsPage(pageNumber) {
        $http.get('/api/downloads/?format=json&page=' + pageNumber)
            .then(function(result) {
                $scope.objs = result.data.results;
                $scope.total = result.data.count;
            });
    }
});
