from shutil import register_archive_format


def ux_agent(context , llm):
  
  prompt = f"""
  
  You are a UX researcher
  
  Analyze:
  {context}
  
  Identify usability issues and confusion points.
  """
  
  return llm(prompt)

