'use strict';

var controllers = angular.module('openPSEApp.controllers', []);

controllers.controller('QuoteDownloadsController', function ($scope, $http, $window, downloadsService) {
    $scope.objs = [];
    $scope.total = 0;
    $scope.objsPerPage = 50;
    $scope.urlParams = {}
    getUrlParams();
    $scope.pageNum = typeof $scope.urlParams.page != 'undefined' ? $scope.urlParams.page : 1;
    console.log($scope.pageNum);
    downloadsService.getPage($scope.pageNum);
    
    $scope.pagination = {
        current: $scope.pageNum
    };
    
    $scope.pageChanged = function(newPage) {
        downloadsService.getPage(newPage).then(function(result) {
            $scope.objs = result.data.results;
            $scope.total = result.data.count;
        });
    };
    
    function getUrlParams(){
        if($window.location.search){
            var parts = $window.location.search.substring(1).split('&');
            for (var i = 0; i < parts.length; i++) {
                var nv = parts[i].split('=');
                if (!nv[0]) continue;
                $scope.urlParams[nv[0]] = nv[1] || true;
            }
        }
    }
});
