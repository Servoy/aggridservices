angular.module('ngDataGrid',['servoy'])
.factory("ngDataGrid",function() 
{
	return {
		/**
		 * Creates an empty icon configuration object
		 * @return {iconConfig}
		 */
		createIconConfig: function() {
			return {
				iconGroupExpanded: "glyphicon glyphicon-minus ag-icon",
				iconGroupContracted: "glyphicon glyphicon-plus ag-icon",
				iconRefreshData: "glyphicon glyphicon-refresh"
			};
		},
		/**
		 * Creates an empty toolpanel configuration object
		 * @return {toolPanelConfig}
		 */
		createToolPanelConfig: function() {
			return {};
		},
		/**
		 * Creates an empty mainMenuItems configuration object
		 * @return {mainMenuItemsConfig}
		 */
		createMainMenuItemsConfig: function() {
			return {};
		}
	}
})