/* global angular */

/*
    This sets up the main app module and also tells Angular
    what this module depends on to work correctly.
 */
angular.module('angular_apis', [
    'ui.router',
    'ngMaterial',
    'ngMessages',
  ]
)
.config([
  '$urlRouterProvider', '$stateProvider', '$httpProvider',
  function($urlRouterProvider, $stateProvider, $httpProvider) {
    "use strict";

    $stateProvider
      .state('home', {
        url: '/',
        templateUrl: 'js/homeView.tpl.html',
        controller: 'HomeViewCtrl'
      });

    $urlRouterProvider.otherwise('/');
  }
]);

// Runs initialization during load to load backend apis
function init() {
  window.initGapi();
};

// Controller is being used for initialization of APIs
angular.module('angular_apis')
.controller('InitAPIController', function($scope, $window) {

  // Init command to load APIs
  $window.initGapi = function() {
     $scope.$apply($scope.load_apis);
  };

  // Load SignupUserApi
  $scope.load_apis = function() {
    var ready = 0;
    gapi.client.load('comment', 'v1', function() {
      ready++;
    }, '/_ah/api');

    gapi.client.load('get_comments', 'v1', function() {
      ready++;
    }, '/_ah/api');

    if (ready == 2)
      $scope.backend_is_ready = true;
  };
});
