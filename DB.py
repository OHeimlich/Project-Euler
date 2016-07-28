from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, select

engine = create_engine('mysql://root:@10.13.32.60/cvg_val_db')
metadata = MetaData()
users = Table('Tests', metadata,
Column('id', Integer, primary_key=True),
Column('name', String),
Column('status', String))

metadata.create_all(engine)
conn = engine.connect()

ins = users.insert()
conn.execute(ins,name='xi_add', status='Pass')
conn.execute(ins,name='xi_LUT', status='Failed')

s = select([users])
result = conn.execute(s)
for row in result:
    print "row: "+ row.__str__()
