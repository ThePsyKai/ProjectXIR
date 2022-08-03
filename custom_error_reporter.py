

def XIR_ERROR_REPORT(Engine:str, Report:str, Solution:str):
	print(("="*15)+Engine+" Error Report"+("="*15))
	print(Report)
	print("Documented Solution:\n\t"+Solution)
	print(("="*15)+("="*(len(str(Engine))+len(" Error Report")))+("="*15))
