from ._anvil_designer import ProjectsTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Projects(ProjectsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # self.ProjectListContainer = RepeatingPanel()
    # Any code you write here will run before the form opens.

    print("projects", app_tables.projects.search())

    self.ProjectListContainer.items = app_tables.projects.search()

  
  def home_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("Home")

  def projects_link_click(self, **event_args):
    open_form('Projects')