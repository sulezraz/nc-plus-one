You can run **`terraform destroy` locally or through another GitHub Actions workflow**. The key requirement is access to the **same Terraform state used during deployment**. [Terraform documentation](https://developer.hashicorp.com/terraform/cli/run)

**From your computer**, if your configuration uses the same shared backend, such as S3:

```bash
cd terraform
terraform init
terraform plan -destroy  # Preview what will be deleted
terraform destroy       # Review the plan and type yes to confirm
```

Use the same AWS account, Region, Terraform workspace and required input variables as the deployment.

**Through GitHub Actions**, create a separate, manually triggered destroy workflow that:

1. Checks out your Terraform configuration.
2. Sets up Terraform and AWS credentials.
3. Runs `terraform init` against the same backend.
4. Plans and applies the destruction.

A `workflow_dispatch` trigger lets you start it using **Actions → select workflow → Run workflow**. [GitHub documentation](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow)

**Check where your state is stored first.** If it existed only on the temporary GitHub-hosted runner and wasn’t saved, a new run won’t automatically know which resources were created. You would need to recover the state or import those resources before using Terraform to destroy them.