PACKAGE_DIR=package

package-aws:
	@echo "Packaging for AWS..."
	@rm -rf $(PACKAGE_DIR)
	@mkdir -p $(PACKAGE_DIR)
	@cp main.py common/*.py aws/aws_impl.py $(PACKAGE_DIR)
	@cp aws/requirements_aws.txt $(PACKAGE_DIR)/requirements.txt
	@cd $(PACKAGE_DIR) && zip -r ../deployment_aws.zip .
	@echo "AWS package created: deployment_aws.zip"

package-azure:
	@echo "Packaging for Azure..."
	@rm -rf $(PACKAGE_DIR)
	@mkdir -p $(PACKAGE_DIR)
	@cp main.py common/*.py azure/azure_impl.py $(PACKAGE_DIR)
	@cp azure/requirements_azure.txt $(PACKAGE_DIR)/requirements.txt
	@cd $(PACKAGE_DIR) && zip -r ../deployment_azure.zip .
	@echo "Azure package created: deployment_azure.zip"