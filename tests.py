
from django.test import TestCase

from .models import Invoice

class TestInvoice(TestCase):
	        	
		self.total = 0
		items = self.invoiceitem_set.all()
                item.cost = 12
                item.qty = 2
                self.assertIs(self.total.total_items(), 24)
		

