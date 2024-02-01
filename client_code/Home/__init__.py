from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def home_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Home')

  def projects_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('TimesTables')

  def times_tables_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('TimesTables')
