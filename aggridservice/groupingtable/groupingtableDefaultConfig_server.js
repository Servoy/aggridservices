/**
 * Creates an empty toolpanel configuration object
 * @return {toolPanelConfig}
 */
$scope.api.createToolPanelConfig = function() {
	return {};
}

/**
 * Creates an empty icon configuration object
 * @return {iconConfig}
 */
$scope.api.createIconConfig = function() {
	return {
		iconGroupExpanded: "glyphicon glyphicon-minus ag-icon",
		iconGroupContracted: "glyphicon glyphicon-plus ag-icon",
		iconRefreshData: "glyphicon glyphicon-refresh"
	};
}

/**
 * Creates an empty mainMenuItems configuration object
 * @return {mainMenuItemsConfig}
 */
 $scope.api.createMainMenuItemsConfig = function() {
	return {};
}
