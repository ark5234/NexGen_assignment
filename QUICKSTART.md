# Quick Start Commands for NexGen Logistics

## CORRECT Commands to Run the Application

### Step 1: Navigate to the project directory
```powershell
cd c:\Users\Vikra\OneDrive\Desktop\ofi\nexgen_logistics
```

### Step 2: Activate the virtual environment
```powershell
.\.venv\Scripts\Activate.ps1
```
You should see `(.venv)` appear before your prompt.

### Step 3: Run Streamlit
```powershell
streamlit run app.py
```

## All-in-One Command
```powershell
cd c:\Users\Vikra\OneDrive\Desktop\ofi\nexgen_logistics ; .\.venv\Scripts\Activate.ps1 ; streamlit run app.py
```

## Alternative (Without Activation)
```powershell
cd c:\Users\Vikra\OneDrive\Desktop\ofi\nexgen_logistics ; .\.venv\Scripts\streamlit.exe run app.py
```

## What Was Wrong Before?

**WRONG**: You were activating venv from `ofi/` folder
```powershell
# This activated the WRONG venv (if it exists in parent folder)
C:\Users\Vikra\OneDrive\Desktop\ofi\.venv\Scripts\Activate.ps1
```

**CORRECT**: Activate venv from `nexgen_logistics/` folder
```powershell
# This activates the RIGHT venv (where streamlit is installed)
C:\Users\Vikra\OneDrive\Desktop\ofi\nexgen_logistics\.venv\Scripts\Activate.ps1
```

## Troubleshooting

### If you see "No module named streamlit"
Your venv is not activated correctly. Run:
```powershell
cd c:\Users\Vikra\OneDrive\Desktop\ofi\nexgen_logistics
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### If you see "Execution policy" error
Run PowerShell as Administrator and execute:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### To verify streamlit is installed
```powershell
cd c:\Users\Vikra\OneDrive\Desktop\ofi\nexgen_logistics
.\.venv\Scripts\python.exe -m pip list | Select-String streamlit
```

## Expected Output
```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://10.71.86.181:8501
```

The app will automatically open in your default browser at http://localhost:8501
