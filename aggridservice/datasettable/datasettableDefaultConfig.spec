{
    "name": "ngPowerGrid",
    "displayName": "NG Power Grid Default Configurator",
    "version": 1,
    "definition": "aggridservice/datasettable/datasettableDefaultConfig.js",
	"serverscript": "aggridservice/datasettable/datasettableDefaultConfig_server.js",
	"doc": "aggridservice/datasettable/datasettableDefaultConfig_doc.js",
    "libraries": [],
    "ng2Config": {
       "packageName": "@servoy/nggrids",
       "serviceName": "PowergridService",
	   	"dependencies": {
    	   "serverscript": "aggridservice/datasettable/datasettableDefaultConfig_server_ng2.js"
    	}
    },
    "model": {
		"iconConfig": "iconConfig",
		"toolPanelConfig": "toolPanelConfig",
		"gridOptions": "map",
		"localeText": "map",
		"columnOptions": "map",
		"mainMenuItemsConfig": "mainMenuItemsConfig",
		"continuousColumnsAutoSizing": "boolean",
		"columnsAutoSizingOn": "columnsAutoSizingOn"
	},
	"api": {
		"createIconConfig" : {
			"returns": "iconConfig"
		},
        "createToolPanelConfig" : {
			"returns": "toolPanelConfig"
		},
		"createMainMenuItemsConfig" : {
			"returns": "mainMenuItemsConfig"
		},
		"createColumnsAutoSizingOn" : {
			"returns": "columnsAutoSizingOn"
		}
    },
    "types" : {
        "iconConfig" : {
			"iconMenu": { "type": "styleclass"},
			"iconFilter": { "type": "styleclass"},
			"iconColumns": { "type": "styleclass"},
			"iconSortAscending": { "type": "styleclass"},
			"iconSortDescending": { "type": "styleclass"},
			"iconSortUnSort": { "type": "styleclass"},
			
			"iconGroupExpanded": { "type": "styleclass"},
			"iconGroupContracted": { "type": "styleclass"},
			"iconColumnGroupOpened": { "type": "styleclass"},
			"iconColumnGroupClosed": { "type": "styleclass"},
			"iconColumnSelectOpen": { "type": "styleclass"},
			"iconColumnSelectClosed": { "type": "styleclass"},
			
			"iconCheckboxChecked": { "type": "styleclass"},
			"iconCheckboxUnchecked": { "type": "styleclass"},
			"iconCheckboxIndeterminate": { "type": "styleclass"},
			"iconCheckboxCheckedReadOnly": { "type": "styleclass"},
			"iconCheckboxUncheckedReadOnly": { "type": "styleclass"},
			"iconCheckboxIndeterminateReadOnly": { "type": "styleclass"},
			
			"iconColumnMovePin": { "type": "styleclass"},
			"iconColumnMoveAdd": { "type": "styleclass"},
			"iconColumnMoveHide": { "type": "styleclass"},
			"iconColumnMoveMove": { "type": "styleclass"},
			"iconColumnMoveLeft": { "type": "styleclass"},
			"iconColumnMoveRight": { "type": "styleclass"},
			"iconColumnMoveGroup": { "type": "styleclass"},
			"iconColumnMoveValue": { "type": "styleclass"},
			"iconColumnMovePivot": { "type": "styleclass"},
			"iconDropNotAllowed": { "type": "styleclass"},
			
			"iconMenuPin": { "type": "styleclass"},
			"iconMenuValue": { "type": "styleclass"},
			"iconMenuAddRowGroup": { "type": "styleclass"},
			"iconMenuRemoveRowGroup": { "type": "styleclass"},
			"iconClipboardCopy": { "type": "styleclass"},
			"iconClipboardPaste": { "type": "styleclass"},
			
			"iconRowGroupPanel": { "type": "styleclass"},
			"iconPivotPanel": { "type": "styleclass"},
			"iconValuePanel": { "type": "styleclass"},
			"iconRefreshData": { "type": "styleclass"},
			
			"iconEditorChecked": { "type": "styleclass"},
			"iconEditorUnchecked": { "type": "styleclass"}
        },
		"toolPanelConfig" : {
			"suppressRowGroups": {"type": "boolean"},
			"suppressValues": {"type": "boolean"},
			"suppressPivots": {"type": "boolean"},
			"suppressPivotMode": {"type": "boolean"},
			"suppressSideButtons": {"type": "boolean"},
			"suppressColumnFilter": {"type": "boolean"},
			"suppressColumnSelectAll": {"type": "boolean"},
			"suppressColumnExpandAll": {"type": "boolean"}
		},
		"mainMenuItemsConfig" : {
			"pinSubMenu": {"type": "boolean" },
			"valueAggSubMenu": {"type": "boolean" },
			"autoSizeThis": {"type": "boolean" },
			"autoSizeAll": {"type": "boolean" },
			"rowGroup": {"type": "boolean" },
			"rowUnGroup": {"type": "boolean" },
			"resetColumns": {"type": "boolean" },
			"expandAll": {"type": "boolean" },
			"contractAll": {"type": "boolean" }
		},
		"columnsAutoSizingOn" : {
			"columnResize" : { "type": "boolean" },
			"columnRowGroupChange" : { "type": "boolean" },
			"displayedColumnsChange" : { "type": "boolean" },
			"gridSizeChange" : { "type": "boolean" },
			"toolPanelVisibleChange" : { "type": "boolean" }
		}		
    }
}
