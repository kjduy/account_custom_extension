# account_custom_extension

## Módulo Personalizado de Odoo

### Descripción General
Este es un ejemplo de un módulo personalizado de Odoo diseñado para extender o mejorar la funcionalidad de la contabilidad del sistema ERP Odoo 18.

### Características
- Traducción al idioma español.
- Creación de campos computados, almacenados y relacionales heredando del modelo `account.move`.
- Archivo de seguridad para asegurar que solo los usuarios que pertenecen al grupo `group_account_manager` puedan acceder.
- Modificación de la vista heredada `view_move_form` para agregar nuevos campos.
- Modificación de los filtros en la vista `view_account_invoice_filter` para agregar nuevos filtros.
- Creación de un menú en Clientes y Proveedores para mostrar los nuevos campos en una lista.
- Creación de un reporte.

### Instalación
1. Copiar el módulo en el directorio de addons de Odoo.
2. Reiniciar el servidor de Odoo.
3. Actualizar la lista de módulos desde el menú de Apps de Odoo.
4. Activar el módulo.

### Dependencias
Este módulo depende de:
- `account`

### Compatibilidad
- Versión de Odoo: 18

### Autor
- **Kevin Duy**
