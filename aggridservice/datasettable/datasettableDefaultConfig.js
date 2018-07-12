angular.module('datasettableDefaultConfig',['servoy'])
.factory("datasettableDefaultConfig",function() 
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