'use strict';

/* App Module */

var openPSEApp = angular.module('openPSEApp', [
    'ngRoute',

    'angularUtils.directives.dirPagination',

    'openPSEControllers'
]);

openPSEApp.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
            when('/api/downloads?format=json&page=:pageNum', {
                controller: 'QuoteDownloadsController'
            }
        );
    }
]);
