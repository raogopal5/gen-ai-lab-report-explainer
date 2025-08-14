from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import LabReportInput, LabReportOutput
from chains import get_explainer_chain

import traceback
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI(title="Lab Report Explainer with Local Ollama LLM")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow frontend access
    allow_methods=["*"],
    allow_headers=["*"],
)

import traceback
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.middleware("http")
async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        tb = traceback.format_exc()
        print(f"Exception caught: {e}")
        print(tb)
        return JSONResponse(content={"detail": str(e)}, status_code=500)


chain = get_explainer_chain()

@app.post("/explain_lab_report", response_model=LabReportOutput)
async def explain_lab_report(data: LabReportInput):
    explanation = chain.run(report_text=data.report_text)
    return LabReportOutput(explanation=explanation)
