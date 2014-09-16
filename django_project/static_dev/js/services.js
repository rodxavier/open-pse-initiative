'use strict';

var services = angular.module('openPSEApp.services', []);

services.service('downloadsService', ['$http', function ($http){
    var urlBase = '/api/downloads/?format=json&page='

    this.getPage = function(pageNum){
        return $http.get(urlBase + pageNum);
    };    
}]);
