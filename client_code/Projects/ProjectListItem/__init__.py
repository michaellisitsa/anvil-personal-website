from ._anvil_designer import ProjectListItemTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ProjectListItem(ProjectListItemTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    print(self.item)
    # Any code you write here will run before the form opens.
    self.header.text = self.item['header']
    self.short_description.text = self.item['description']
    self.hero_image.source = self.item['hero_image']
