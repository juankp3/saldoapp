.DEFAULT_GOAL := help

## Target Commons ##

clear: ## Borra archivos generados
	rm controllers/__init__.pyc controllers/controllers.pyc models/__init__.pyc models/models.pyc

restar: ## Actualiza el modulo saldoapp
	docker exec -it odoodocker_odoo10_1 /usr/bin/odoo -d odoo -u saldoapp





## Target Help ##

help:
	@printf "\033[31m%-16s %-59s %s\033[0m\n" "Target" "Help" "Usage"; \
	printf "\033[31m%-16s %-59s %s\033[0m\n" "------" "----" "-----"; \
	grep -hE '^\S+:.*## .*$$' $(MAKEFILE_LIST) | sed -e 's/:.*##\s*/:/' | sort | awk 'BEGIN {FS = ":"}; {printf "\033[32m%-16s\033[0m %-58s \033[34m%s\033[0m\n", $$1, $$2, $$3}'
