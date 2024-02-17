from ._anvil_designer import TimesTableRow2Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class TimesTableRow2(TimesTableRow2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.value.text = self.item['number']
    # Any code you write here will run before the form opens.
