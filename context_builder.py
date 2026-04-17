class FlowBuilder:
  
  def __init__(self , cleaner , extractor , flow_builder):
    self.cleaner = cleaner
    self.extractor = extractor
    self.flow_builder = flow_builder
    
    
  def build(self , transcript , events):
    cleaned_transcript = self.cleaner.clean(transcript)
    
    extracted_events = self.extractor.extract(events)
    
    flow = self.flow_builder.build(extracted_events)
    
    context = {
      "transcript" : cleaned_transcript,
      "flow" : flow
    }
    
    return context