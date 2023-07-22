from table import Table
from table.columns import Column

class UserConnectedTable(Table):
    user_name=Column(field='user_name')
    user_terminal=Column(field='user_terminal')
    user_ip=Column(field='user_ip')