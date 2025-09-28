# FileConverter - Word to PDF Converter

A simple Python program that converts Word files (.docx, .doc) to PDF format using the iLovePDF API.

## 📋 Requirements

### Python Dependencies
Install the required packages:
```bash
pip install requests
```

Or use the `requirements.txt` file
```bash
pip install -r requirements.txt
```

### iLovePDF API
You need a free iLovePDF account to obtain API keys.

## 🔑 Getting API Keys from iLovePDF

### Step 1: Create Account
1. Go to [iLovePDF Developer Portal](https://developer.ilovepdf.com/)
2. Click **"Sign Up"** and create a free account
3. Verify your email if required

### Step 2: Create API Project
1. After logging in, go to **Dashboard**
2. Click **"Create new project"** or **"New Project"**
3. Fill in the project details:
   - **Project Name**: FileConverter (or any name you prefer)
   - **Description**: Word to PDF Converter
4. Click **"Create"**

### Step 3: Get API Keys
1. In the dashboard, select your created project
2. You will see two important keys:
   - **Public Key** - a long key starting with alphanumeric characters
   - **Secret Key** - a secret key for signing requests

3. **Copy both keys exactly** - these are required for authentication

### Step 4: Configure Keys in Project
1. In the project directory, create a file named `secretKeys.py`
2. Add your keys in the following format:

```python
# secretKeys.py
PUBLIC_KEY = "your_public_key_here"
SECRET_KEY = "your_secret_key_here"
```

**Important**: 
- Replace `your_public_key_here` and `your_secret_key_here` with your actual keys
- Keep the quotes around the keys
- Never share these keys publicly or commit them to version control

## 🚀 How to Run

### Step 1: Setup
1. Clone or download this repository
2. Install dependencies: `pip install requests`
3. Create `secretKeys.py` with your API keys (see above)

### Step 2: Run the Program
```bash
python fileConvertor.py
```

### Step 3: Convert Files
1. The program will prompt you to select a Word file (.doc or .docx)
2. Choose your file from the file dialog
3. The converted PDF will be saved in the same directory
4. Check the console for conversion status and any error messages

## 📁 Project Structure
```
FileConverter/
├── fileConvertor.py      # Main program file
├── secretKeys.py         # Your API keys (create this file)
├── README.md            # This file
└── requirements.txt     # Dependencies (optional)
```

## ⚠️ Important Notes

- **Free Tier Limits**: iLovePDF free accounts have monthly processing limits
- **File Size**: Check iLovePDF documentation for maximum file size limits
- **Security**: Never commit your `secretKeys.py` file to public repositories
- **Internet Connection**: Active internet connection required for API calls

## 🐛 Troubleshooting

### Common Issues:

**401 Unauthorized Error**:
- Check that your PUBLIC_KEY and SECRET_KEY are correct
- Verify your iLovePDF account is active
- Ensure keys are copied exactly from the dashboard

**400 Bad Request**:
- File format might not be supported
- File might be corrupted
- Check file size limits

**Connection Errors**:
- Check your internet connection
- Verify iLovePDF API is accessible from your location
