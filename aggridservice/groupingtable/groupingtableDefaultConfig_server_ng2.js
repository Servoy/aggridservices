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
	return {};
}

/**
 * Creates an empty mainMenuItems configuration object
 * @return {mainMenuItemsConfig}
 */
 $scope.api.createMainMenuItemsConfig = function() {
	return {};
}

/**
 * Creates an empty columnsAutoSizingOn configuration object
 * @return {columnsAutoSizingOn}
 */
$scope.api.createColumnsAutoSizingOn = function() {
	return {
		columnResize: true,
		columnRowGroupChange: true,
		displayedColumnsChange: true,
		gridReady: true,
		gridSizeChange: true,
		toolPanelVisibleChange: true
	}
}
