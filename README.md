# embrava_blynclight

This is a very simple project to control the light on an Embrava Blynclight Standard BLYNCUSB40-241 on Windows.

# Initial Setup
```powershell
# Install uvNotes: uv/python
# https://docs.astral.sh/uv/guides/install-python/#getting-started

# This must be run as administrator
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine

# Install uv
winget install --id=astral-sh.uv  -e

# Instal python with uv
uv python install

# Setup a virtual env
cd .\Documents\code\some_project
uv venv
.venv\Scripts\activate
```
