/* global angular */

angular.module('angular_apis')
.controller('HomeViewCtrl',
  [
    '$scope', '$state', '$stateParams',
    function($scope, $state, $stateParams) {
      "use strict";

      $scope.displayOverflow = false;
      $scope.comment = "";
      $scope.comments = [];

      $scope.submit = function submit(comment) {
        var ROOT = 'https://localhost:8080/_ah/api';
        gapi.client.comment.submit({
          'Comment': $scope.comment
        }).execute();
        $scope.getComments();
      };

      $scope.getComments = function getComments() {
        gapi.client.get_comments.list().execute(function(resp) {
          console.log("here we are");
          $scope.comments = resp.message;
        });
      };

      $scope.clear = function clear() {
        $scope.comment = "";
      };
    }
  ]
);
