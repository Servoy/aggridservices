{
    "name": "groupingtableDefaultConfig",
    "displayName": "Grouping Table Default Configurator",
    "version": 1,
    "definition": "aggridservice/groupingtable/groupingtableDefaultConfig.js",
    "libraries": [],
    "model": {"iconConfig": "iconConfig", "toolPanelConfig": "toolPanelConfig", "gridOptions": "map", "localeText": "map"},
    "api": {
		"createIconConfig" : {
			"returns": "iconConfig"
		},
        "createToolPanelConfig" : {
			"returns": "toolPanelConfig"
		}
    },
    "types" : {
        "iconConfig" : {
			"iconMenu": { "type": "styleclass" },
			"iconFilter": { "type": "styleclass" },
			"iconColumns": { "type": "styleclass" },
			"iconSortAscending": { "type": "styleclass" },
			"iconSortDescending": { "type": "styleclass" },
			"iconSortUnSort": { "type": "styleclass" },
			
			"iconGroupExpanded": { "type": "styleclass", "default" : "glyphicon glyphicon-minus ag-icon" },
			"iconGroupContracted": { "type": "styleclass", "default" : "glyphicon glyphicon-plus ag-icon" },
			"iconColumnGroupOpened": { "type": "styleclass" },
			"iconColumnGroupClosed": { "type": "styleclass" },
			"iconColumnSelectOpen": { "type": "styleclass" },
			"iconColumnSelectClosed": { "type": "styleclass" },
			
			"iconCheckboxChecked": { "type": "styleclass" },
			"iconCheckboxUnchecked": { "type": "styleclass" },
			"iconCheckboxIndeterminate": { "type": "styleclass" },
			"iconCheckboxCheckedReadOnly": { "type": "styleclass" },
			"iconCheckboxUncheckedReadOnly": { "type": "styleclass" },
			"iconCheckboxIndeterminateReadOnly": { "type": "styleclass" },
			
			"iconColumnMovePin": { "type": "styleclass" },
			"iconColumnMoveAdd": { "type": "styleclass" },
			"iconColumnMoveHide": { "type": "styleclass" },
			"iconColumnMoveMove": { "type": "styleclass" },
			"iconColumnMoveLeft": { "type": "styleclass" },
			"iconColumnMoveRight": { "type": "styleclass" },
			"iconColumnMoveGroup": { "type": "styleclass" },
			"iconColumnMoveValue": { "type": "styleclass" },
			"iconColumnMovePivot": { "type": "styleclass" },
			"iconDropNotAllowed": { "type": "styleclass" },
			
			"iconMenuPin": { "type": "styleclass" },
			"iconMenuValue": { "type": "styleclass" },
			"iconMenuAddRowGroup": { "type": "styleclass" },
			"iconMenuRemoveRowGroup": { "type": "styleclass" },
			"iconClipboardCopy": { "type": "styleclass" },
			"iconClipboardPaste": { "type": "styleclass" },
			
			"iconRowGroupPanel": { "type": "styleclass" },
			"iconPivotPanel": { "type": "styleclass"},
			"iconValuePanel": { "type": "styleclass"},
			
			"iconRefreshData": { "type": "styleclass", "default" : "glyphicon glyphicon-refresh"}
        },
        "toolPanelConfig" : {
            "suppressRowGroups": {"type": "boolean" },
            "suppressSideButtons": {"type": "boolean" },
            "suppressColumnFilter": {"type": "boolean" },
            "suppressColumnSelectAll": {"type": "boolean" },
            "suppressColumnExpandAll": {"type": "boolean" }
        }
    }
}
