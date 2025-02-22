PACKAGE_DIR=package

package-aws:
	@echo "Packaging for AWS..."
	@rm -rf $(PACKAGE_DIR)
	@mkdir -p $(PACKAGE_DIR)
	@cp main.py $(PACKAGE_DIR)
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
	@cp main.py $(PACKAGE_DIR)
	@mkdir -p $(PACKAGE_DIR)/common_layer
	@cp common_layer/*.py $(PACKAGE_DIR)/common_layer
	@mkdir -p $(PACKAGE_DIR)/azure_layer
	@cp azure_layer/azure_impl.py $(PACKAGE_DIR)/azure_layer
	@cp azure_layer/requirements_azure.txt $(PACKAGE_DIR)/requirements.txt
	@cd $(PACKAGE_DIR) && zip -r ../deployment_azure.zip .
	@echo "Azure package created: deployment_azure.zip"