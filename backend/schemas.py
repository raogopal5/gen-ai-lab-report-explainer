from pydantic import BaseModel

class LabReportInput(BaseModel):
    report_text: str

class LabReportOutput(BaseModel):
    explanation: str
