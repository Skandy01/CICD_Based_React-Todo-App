import os

def check_azure_env():
  print("--Automation Task--")

  client_id = os.getenv('AZURE_CLIENT_ID')
  tenant_id = os.getenv('AZURE_TENANT_ID')

  if client_id and tenant_id:
    print(f"Success: Azure credentials found for Tenant: {tenant_id}")
  else:
    print("Warning: Azure credentials not found")

  print("Python execution finished successfully!")

if __name__ == "__main__":
  check_azure_env()
