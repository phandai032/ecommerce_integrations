from typing import Dict, List, NewType

from frappe.model.document import Document

DraERPWarehouse = NewType("DraERPWarehouse", str)
IntegrationWarehouse = NewType("IntegrationWarehouse", str)


class SettingController(Document):
	def is_enabled(self) -> bool:
		"""Check if integration is enabled or not."""
		raise NotImplementedError()

	def get_draerp_warehouses(self) -> List[DraERPWarehouse]:
		raise NotImplementedError()

	def get_draerp_to_integration_wh_mapping(self) -> Dict[DraERPWarehouse, IntegrationWarehouse]:
		raise NotImplementedError()

	def get_integration_to_draerp_wh_mapping(self) -> Dict[IntegrationWarehouse, DraERPWarehouse]:
		raise NotImplementedError()
