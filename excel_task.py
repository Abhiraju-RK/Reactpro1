from openpyxl import Workbook

wb=Workbook()
sheets=wb.active
sheets.title="Demo Sheet"

sheets["A1"]="Name"
sheets["B1"]='Age'

sheets.append(["Abhi",23])
sheets.append(["Arun",24])

wb.save("Demo.xlsx")
print("Demo excel file created")