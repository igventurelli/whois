import sys
from whois import whois
from prettytable import PrettyTable

d = whois(sys.argv[1])

table = PrettyTable(['Domain', 'Owner', 'Owner Document', 'Expires', 'Status'])
table.add_row([d.domain, d.registrant_name, d.registrant_id, d.expiration_date, d.status])

print(table)