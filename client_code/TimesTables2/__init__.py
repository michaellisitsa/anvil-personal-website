from ._anvil_designer import TimesTables2Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..TimesTableRow import TimesTableRow
from ..NavBar import NavBar

class TimesTables2(TimesTables2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # self.number.text = self.item['number']
    self.nav_bar_container.add_component(NavBar(item={"active": "Projects"}))
    times_table_rows = []
    self.item['number'] = 0
    for i in range(13):
      print("number", self.item['number'])
      row = {'base': i+1, 'number': self.item['number']}
      times_table_rows.append(row)
    print(self.repeating_panels.items)
    self.repeating_panels.items = times_table_rows
  
  def number_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    # self.item['number']  = self.number.text
    print("new number", self.item['number'])
    self.refresh_data_bindings()
    for panel in self.repeating_panels:
      panel.refresh_data_bindings()
