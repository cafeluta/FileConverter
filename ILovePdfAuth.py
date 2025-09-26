import requests
import json
from secretKeys import SECRET_KEY, PUBLIC_KEY

class ILovePDFAuth:
    def __init__(self):
        self.base_url = "https://api.ilovepdf.com/v1"
        self.public_key = PUBLIC_KEY
        self.secret_key = SECRET_KEY
        self.signed_token = None

    def authenticate(self):
        # Authentification url for signed token
        auth_url = f"{self.base_url}/auth"

        # Public Key is needed for the signed token
        payload = {
            'public_key': self.public_key
        }

        try:
            print(f"🔑 Authenticating with public_key: {self.public_key[:10]}...")

            # data = payload -> sending the public key inside the body
            response = requests.post(auth_url, data=payload)

            # INFO LOG 
            print(f"Authentication Status Code: {response.status_code}")
            print(f"Auth Response: {response.text}")

            if response.status_code == 200:
                # extracting the signed token from the response
                auth_data = response.json()  # creating a new dict
                self.signed_token = auth_data.get('token')  # getting the signed token

                # checking if the signed token exists
                if self.signed_token:
                    print(f"✅Authentication Successfull")
                    print(f"Signed Token:{self.signed_token[:20]} ...")

                    return True
                else:
                    print("❌ No token received in response")
                    return False

            else:
                print(f"❌ Authentication failed: {response.text}")
                return False
                

        except Exception as e:
            print(f"Authentication Error: {str(e)}")
            return False
        
    def start_task(self, task_type="compress"):
        # check for the signed token
        if not self.signed_token:
            print(f"❌Authentication needed first")
            return None

        start_url = f"{self.base_url}/start/{task_type}/eu"

        # request headers
        headers = {
            'Authorization': f"Bearer {self.signed_token}",
            'Content-Type': 'application/json'
        }

        try:
            print(f"🚀Starting task: {task_type}")
            response = requests.get(start_url, headers=headers)

            print(f"Start Task Status Code: {response.status_code}")
            print(f"Start Task Response: {response.text}")
            
            if response.status_code == 200:
                task_data = response.json()
                print("✅ Task started successfully!")
                return task_data
            else:
                print(f"❌ Failed to start task: {response.text}")
                return None
                
        except Exception as e:
            print(f"❌ Start task error: {str(e)}")
            return None
    
    def test_multiple_tasks(self):
        
        task_types = [
            "compress",
            "pdfjpg", 
            "officepdf",
            "merge",
            "split",
            "watermark"
        ]
        
        print("\n" + "="*50)
        print("Testing different task types:")
        print("-" * 30)
        
        successful_tasks = []
        
        for task_type in task_types:
            print(f"\n📋 Testing: {task_type}")
            result = self.start_task(task_type)
            
            if result:
                successful_tasks.append(task_type)
        
        print(f"\n📊 Summary: {len(successful_tasks)}/{len(task_types)} tasks work")
        if successful_tasks:
            print(f"✅ Working tasks: {', '.join(successful_tasks)}")

def test_authentication():
    print("=== iLovePDF API Authentication Test ===")
    print(f"Using PUBLIC_KEY: {PUBLIC_KEY[:15]}...")
    print(f"SECRET_KEY length: {len(SECRET_KEY)}")
    
    # Create the authentication instance
    api = ILovePDFAuth()
    
    if api.authenticate():
        
        # Basic task test
        print("\n" + "="*50)
        print("Testing basic task:")
        api.start_task("compress")
        
        # Multiple task test
        api.test_multiple_tasks()
    
    else:
        print("\n💡 Debugging suggestions:")
        print("1. Verify PUBLIC_KEY is exactly as shown in iLovePDF dashboard")
        print("2. Make sure your account has API access enabled") 
        print("3. Check if you're using the correct API endpoint region")
        print("4. Try regenerating your API keys")

if __name__ == "__main__":
    test_authentication()