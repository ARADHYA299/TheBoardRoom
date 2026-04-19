from pydantic import BaseModel
from typing import Dict


class AnalyzeResponse(BaseModel):
  agents : Dict[str, str]
  summary : str
  
  
  