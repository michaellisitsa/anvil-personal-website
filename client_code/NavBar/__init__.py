from ._anvil_designer import NavBarTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class NavBar(NavBarTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  def home_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Home')

  def projects_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Projects')

  def times_table_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('TimesTables2')