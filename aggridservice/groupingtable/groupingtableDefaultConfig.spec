{
    "name": "groupingtableDefaultConfig",
    "displayName": "Grouping Table Default Configurator",
    "version": 1,
    "definition": "aggridservice/groupingtable/groupingtableDefaultConfig.js",
    "libraries": [],
    "model": {"iconConfig": "iconConfig", "toolPanelConfig": "toolPanelConfig"},
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
        	"iconGroupExpanded": { "type": "styleclass" },
			"iconGroupContracted": { "type": "styleclass" },
			"iconSortAscending": { "type": "styleclass" },
			"iconSortDescending": { "type": "styleclass" },		
			"iconSortUnSort": { "type": "styleclass" },
			"iconRefreshData": { "type": "styleclass" }
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
