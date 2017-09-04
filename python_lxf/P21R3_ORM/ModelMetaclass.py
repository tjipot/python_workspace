# @Nov 12, 2016, HYE
# Get mapping info of concrete sub-class such as 'User', via metaclass such as ModelMetaclass, because Model is only a base class;
# Any class(e.g. class User) inherited from class Model will automatically get mapping relationship via ModelMetaclass, and stores the relationship into its class attributes such as __table__, __mappings__, etc.;
class ModelMetaclass(type):
	def __new__(cls, name, bases, attrs):
		# Exclude class Model itself;
		if name == 'Model':
			return type.__new__(cls, name, bases, attrs)
		# Get name of table;
		tableName = attrs.get('__table__', None) or name
		logging.info('Model Found: %s (table: %s)' %(name, tableName))
		# Get all fields and primary keys;
		mappings = dict()
		fields = []
		primaryKey = None
		for k, v in attrs.items():
			if isinstance(v, Field):
				logging.info('Mapping Found: %s ==> %s' %(k, v))
				mappings[k] = v
				if v.primary_key:
					# Find primary key;
					if primaryKey:
						raise RuntimeError('Duplicate primary key for fields: %s' %k)
						primaryKey = k
				else:
					fields.append(k)
		if not primaryKey:
			raise RuntimeError('Primary key not found.')
		for k in mappings.keys():
			attrs.pop(k)
		escaped_fields = list(map(lambda f: '`%s`' %f, fields))
		# Save mapping relations between attributes and columns;
		attrs['__mappings__'] = mappings
		attrs['__table__'] = tableName
		attrs['__primary_key__'] = primaryKey
		attrs['__fields__'] = fields
		# Generate default MySQL query expression of SELECT, INSERT, UPDATE, DELETE;
		attrs['__select__'] = 'select `%s` , %s from `%s`' %(primaryKey, ', '.join(escaped_fields), tableName)
		attrs['__insert__'] = 'insert into `%s` (%s, `%s`) values (%s)' %(tableName, ', '.join(escaped_fields), primaryKey, create_args_string(len(escaped_fields) + 1))
		attrs['__update__'] = 'update `%s` set %s where `%s`=?' %(tableName, ', '.join(map(lambda f: '`%s`=?' %(mappings.get(f).name or f), fields)), primaryKey)
		attrs['__delete__'] = 'delete from `%s` where `%s`=?' %(tableName, primaryKey)
		return type.__new__(cls, name, bases, attrs)


