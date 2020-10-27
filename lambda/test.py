

from decimal import Decimal 

a= {u'Count': 1, u'Items': [{u'Age': Decimal('10'), u'Name': u'John'}]}

print type(str(a['Items'][-1]['Age'])) 

