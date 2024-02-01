from ._anvil_designer import ProjectsTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..NavBar import NavBar

class Projects(ProjectsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # self.ProjectListContainer = RepeatingPanel()
    # Any code you write here will run before the form opens.
    self.nav_bar_container.add_component(NavBar(item={"active": "Projects"}))
    self.ProjectListContainer.items = app_tables.projects.search()