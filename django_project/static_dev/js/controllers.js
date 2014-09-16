'use strict';

var controllers = angular.module('openPSEApp.controllers', []);

controllers.controller('QuoteDownloadsController', function ($scope, $http, downloadsService) {
    $scope.objs = [];
    $scope.total = 0;
    $scope.objsPerPage = 50;
    $scope.pagination = {
        current: 1
    };
    
    $scope.pageChanged = function(newPage) {
        downloadsService.getPage(newPage).then(function(result) {
            $scope.objs = result.data.results;
            $scope.total = result.data.count;
        });
    };
    
    // Initialize Data
    $scope.pageChanged(1);
});
