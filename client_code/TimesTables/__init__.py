from ._anvil_designer import TimesTablesTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..TimesTableRow import TimesTableRow

class TimesTables(TimesTablesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # # Any code you write here will run before the form opens.
      
  def number_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    for i in range(13):
        self.add_component(TimesTableRow(item={'base': i+1, 'number': self.get_number()}))
    self.refresh_data_bindings()

  def get_number(self):
    try:
      return self.number.text
    except:
      return False