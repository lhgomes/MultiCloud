PACKAGE_DIR=package
FUNCTION_DIR=MyFunction

package-aws:
	@echo "Packaging for AWS..."
	@rm -rf $(PACKAGE_DIR)
	@mkdir -p $(PACKAGE_DIR)
	@cp main.py $(PACKAGE_DIR)
	@cp business_logic.py $(PACKAGE_DIR)
	@mkdir -p $(PACKAGE_DIR)/common_layer
	@cp common_layer/*.py $(PACKAGE_DIR)/common_layer
	@mkdir -p $(PACKAGE_DIR)/aws_layer
	@cp aws_layer/aws_impl.py $(PACKAGE_DIR)/aws_layer/aws_impl.py
	@cp aws_layer/requirements_aws.txt $(PACKAGE_DIR)/requirements.txt
	@cd $(PACKAGE_DIR) && zip -r ../deployment_aws.zip .
	@echo "AWS package created: deployment_aws.zip"

package-azure:
	@echo "Packaging for Azure..."
	@rm -rf $(PACKAGE_DIR)
	@mkdir -p $(PACKAGE_DIR)
	@cp azure_config/host.json $(PACKAGE_DIR)
	@cp azure_layer/requirements_azure.txt $(PACKAGE_DIR)/requirements.txt

	@mkdir -p $(PACKAGE_DIR)/$(FUNCTION_DIR)
	@cp main.py $(PACKAGE_DIR)/$(FUNCTION_DIR)
	@cp business_logic.py $(PACKAGE_DIR)/$(FUNCTION_DIR)
	@cp common_layer/*.py $(PACKAGE_DIR)/$(FUNCTION_DIR)
	@cp azure_layer/azure_impl.py $(PACKAGE_DIR)/$(FUNCTION_DIR)
	@cp azure_config/__init__.py $(PACKAGE_DIR)/$(FUNCTION_DIR)
	@cp azure_config/function.json $(PACKAGE_DIR)/$(FUNCTION_DIR)

	@cd $(PACKAGE_DIR) && zip -r ../deployment_azure.zip .
	@echo "Azure package created: deployment_azure.zip"