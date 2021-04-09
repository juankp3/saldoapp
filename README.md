# Saldo App


### Ingresar a la base de datos de odoo

> Ingrea al conenedor de la base de datos
```
docker exec -it [contenedor] bash
docker exec -it odoodocker_odoo10_1 bash
```

> Ejecuta un comando propio de odoo

Crea una estructura de carpetas del modulo **saldoapp**
```
docker exec -it [contenedor] /usr/bin/odoo scaffold [odoo_module] /mnt/extra-addons
docker exec -it odoodocker_odoo10_1 /usr/bin/odoo scaffold saldoapp /mnt/extra-addons
```
```
├── README.md
├── __init__.py
├── __manifest__.py
├── controllers
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── controllers.py
│   └── controllers.pyc
├── demo
│   └── demo.xml
├── models
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── models.py
│   └── models.pyc
├── security
│   └── ir.model.access.csv
└── views
    ├── templates.xml
    └── views.xml
```


> Ingrea al a la base de datos de postgres
```sql
su - postgres
psql -U odoo -d odoo
select name,email,create_date from res_partner;
```


> Reiniciar contenedor
```
docker restart odoodocker_odoo10_1
```

> Lista todas las vistas
```sql
select name,type,model from ir_ui_view;
```

> Registra permiso de forma manual para visualizar el menu de Saldo App
```
Groups / Administration / Settings
```

> Actualiza el modulo sin necesidad de hacerlo por la web
```
docker exec -it [contenedor] /usr/bin/odoo -d [database] -u [odoo_module]
docker exec -it odoodocker_odoo10_1 /usr/bin/odoo -d odoo -u saldoapp
```

docker exec -it  odoodocker_db_1 /usr/bin/odoo shell -d odoo -u saldoapp --http-port 8776 --longpolling-port 8763
docker exec -it  odoodocker_odoo10_1 /usr/bin/odoo shell -d odoo -u saldoapp --http-port 8776 --longpolling-port 8763


docker exec -it odoodocker_odoo10_1 /usr/bin/odoo shell -d odoo -u saldoapp --longpolling-port 8763

> Login de Odoo
```
Usuario: admin
Contraseña: admin
```