from record import Record

class FeatureExtractor:
  def add_record(self, record):
    """Adds a record to the feature extractor"""
    pass

  def flush(self):
    """Indicates that there are no more records to receive.

    All pending output should be computed and sent.
    """
    pass
