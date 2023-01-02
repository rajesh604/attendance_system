# Import openpyxl
import openpyxl

# Create a new workbook
workbook = openpyxl.Workbook()

# Get the active sheet
sheet = workbook.active

# Write data to cells
sheet['A1'] = 'hello'
sheet['B1'] = 'world'

# Save the workbook
workbook.save('example.xlsx')
