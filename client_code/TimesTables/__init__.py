from ._anvil_designer import TimesTablesTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..TimesTableRow import TimesTableRow
from ..NavBar import NavBar

class TimesTables(TimesTablesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.item['number'] = 0
    self.number.text = self.item['number']
    self.nav_bar_container.add_component(NavBar(item={"active": "Projects"}))
    self.times_table_rows = []
    
    for i in range(13):
      row = TimesTableRow(item={'base': i+1, 'number': self.number.text})
      self.times_table_rows.append(row)
      self.add_component(row)
      
  def number_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    self.refresh_data_bindings()
    for row in self.times_table_rows:
      row.item['number'] = self.number.text
      row.refresh_data_bindings()