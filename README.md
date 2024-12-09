# Installation:

1. To run app in local machine you should first install Install Tesseract-OCR:
Download the Tesseract OCR executable for Windows from Tesseract GitHub releases.
During installation, note the path where Tesseract is installed (e.g., C:\Program Files\Tesseract-OCR).

2. Configure Tesseract in Python:
Make sure to set the TESSDATA_PREFIX environment variable or provide the Tesseract installation path in your code.

## Install Poppler on Windows
1. Download Poppler for Windows:

Visit Poppler for Windows and download the latest release.
Download the binary (e.g., poppler-<version>-x86_64.zip).

2. Extract the Files:

Extract the downloaded ZIP file to a folder (e.g., C:\poppler).

3. Add Poppler to the System PATH:

Press Win + R, type sysdm.cpl, and press Enter to open the System Properties window.
Go to the Advanced tab and click Environment Variables.
Under System Variables, find the Path variable and click Edit.
Add the bin folder path of Poppler (e.g., C:\poppler\bin) to the list.
Click OK to close all windows.

4. Verify Installation:

Open a new Command Prompt window and type

```where pdfinfo```

You should see the path to the pdfinfo executable (e.g., C:\poppler\bin\pdfinfo.exe).

