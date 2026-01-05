# python_study
python study code

## Read Excel example

A small example is provided at `python_study/read_excel_example.py` which reads the first sheet
of a `.xlsx` file and prints the first rows.

Run the example (replace the path with your file):

```powershell
python python_study/read_excel_example.py C:\path\to\your_file.xlsx
```

Notes:
- Use raw strings for Windows paths or `pathlib.Path` to avoid backslash escaping issues.
- Ensure the Excel file is closed in Excel to avoid file-locking errors.
# python_study
python study code
