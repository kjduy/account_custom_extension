# account_custom_extension

# Custom Odoo Module

## Overview
This is an example of a custom Odoo module designed to extend or enhance the account functionality of the Odoo 18 ERP system.

## Features
- Translation into Spanish language
- Creation of computed, stored, and relational fields inheriting from the `account.move` model.
- Security file to ensure that only users belonging to the `group_account_manager` group can access.
- Modification of the inherited `view_move_form` to add new fields.
- Modification of the `view_account_invoice_filter` filters to add new filters.
- Creation of a menu in Customers and Vendors to display the new fields in a list.
- Report creation.

## Installation
1. Copy the module to your Odoo addons directory.
2. Restart the Odoo server.
3. Update Module List from the Odoo Apps menu.
4. Activate the module.

## Dependencies
This module depends on:
- `account`

## Compatibility
- Odoo Version: 18

## Author
- **Kevin Duy**
