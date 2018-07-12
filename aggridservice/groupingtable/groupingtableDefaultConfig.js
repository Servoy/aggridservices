angular.module('groupingtableDefaultConfig',['servoy'])
.factory("groupingtableDefaultConfig",function() 
{
	return {
		/**
		 * Creates an empty icon configuration object
		 * @return {iconConfig}
		 */
		createIconConfig: function() {
			return {};
		},
		/**
		 * Creates an empty toolpanel configuration object
		 * @return {toolPanelConfig}
		 */
		createToolPanelConfig: function() {
			return {};
		}
	}
})