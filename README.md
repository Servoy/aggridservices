# Servoy NG Grid Services

Services to globally set icon, toolPanel, gridOptions and localeText on all NG Grids in a solution.

# Requirements

The Servoy NG Grid Services can be used on NG Grids v2.0.0-rc4 and up.

# Documentation

There are 2 services, one for the NG Power Grid: plugins.ngPowerGrid, and one for
the NG Data Grid: plugins.ngDataGrid. They both have the same config options that
you can set: iconConfig, toolPanelConfig, gridOptions and localeText. Please note
that these must be set before showing the grids, like onSolutionOpen, or onLoad of a form.

Usually a config can be set in 3 places:
 1. on the table component as a design property, if exposed (ex. rowHeight)
 2. as a config option applied on the table component (ex. gridOptions design time property with rowHeight)
 3. as a global config option applied using NG Grid services (ex. plugins.ngDataGrid.gridOptions with rowHeight)
The order they are read is 2 - 3 - 1 : if option is set on component config, that is used, else if global config is set then that
will be used, otherwise, if the option is not set in any config, the design time value of that option will be used.


* iconConfig

Used to customize the icons of the grids. There is a helper api function to
create an iconConfig, that can be usefull as it has predefined icon keys, ex. plugins.ngDataGrid.createIconConfig

* toolPanelConfig

Used to customize the tool panel of the grids. There is a helper api function to
create an toolPanelConfig, that can be usefull as it has predefined tool panel option keys, ex. plugins.ngDataGrid.createToolPanelConfig

* gridOptions

Used to customize any options that ag-Grid exposes. Check here for available options: https://www.ag-grid.com/javascript-grid-properties/

* localeText

Used for internationalisation. Check here for available options: https://www.ag-grid.com/javascript-grid-internationalisation/

* columnOptions

Used to customize the properties of the columns. Check here for available options: https://www.ag-grid.com/javascript-grid-column-properties/

# Feature Requests & Bugs

Found a bug or would like to see a new feature implemented? Raise an issue in the Issue Tracker

# Contributing

Eager to fix a bug or introduce a new feature? Clone the repository and issue a pull request

# License

Servoy NG Grid Services is licensed under the MIT license. You can freely use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies for the content of this repository.
