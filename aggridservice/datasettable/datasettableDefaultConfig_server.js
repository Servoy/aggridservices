/**
 * Creates an empty icon configuration object
 * @return {iconConfig}
 */
$scope.api.createIconConfig = function() {
	return {
		iconGroupExpanded: "glyphicon glyphicon-minus ag-icon",
		iconGroupContracted: "glyphicon glyphicon-plus ag-icon"
	}
}

/**
 * Creates an empty toolpanel configuration object
 * @return {toolPanelConfig}
 */
$scope.api.createToolPanelConfig = function() {
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
		gridSizeChange: true,
		toolPanelVisibleChange: true
	}
}
