import requests
params = {
    "grant_type": "password",
    "client_id": "3MVG9pRzvMkjMb6m2HF7FzKiLxEwPWDotqKwdtGm_IT.T2lFg9cvZYU9qXnfbrPx3OBfiWYJGCVnSGSUJbDcS", # Consumer Key
    "client_secret": "AC691E8B9E4C250CCF259789DE15EE7DC55C5020BA2423A73957B3E0CE55174C", # Consumer Secret
    "username": "puranjay@gmail.com", # The email you use to login
    "password": "QtdsC8D6FKMqPZ7h5fLJpBW8vTOibC9hQflIeDI" # Concat your password and your security token
}
r = requests.post("https://login.salesforce.com/services/oauth2/token", params=params)
# if you connect to a Sandbox, use test.salesforce.com instead
access_token = r.json().get("access_token")
instance_url = r.json().get("instance_url")
print("Access Token:", access_token)
print("Instance URL", instance_url)