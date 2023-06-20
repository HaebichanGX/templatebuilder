# Initialization
# <snippet name="initial import">
import great_expectations as gx
context = gx.get_context()
# </snippet>


# Datasources
# <snippet name="add_pandas_filesystem">
datasource = context.sources.add_pandas_filesystem(name = 'pandas datasource', base_directory = '/path/to/your/files/')
# </snippet>

# <snippet name="add_sql">
datasource = context.sources.add_sql(name = 'sql datasource', connection_string = 'your_connection_string')
# </snippet>

# Assets
# <snippet name="add_csv_asset">
asset = datasource.add_csv_asset(name = 'csv asset', batching_regex = "your_data.csv")
# </snippet>

# <snippet name="add_query_asset">
asset = datasource.add_query_asset(name = 'sql asset', query = "your query")
# </snippet>


# <snippet name="add_table_asset">
asset = datasource.add_table_asset(name = 'table asset', table_name = "your table")
# </snippet>


# Splitters
# <snippet name="add_splitter_column_value">
asset.add_splitter_column_value(column_name = "your_column")
# </snippet>

# Batch Request
# <snippet name="build_batch_request">
batch_request = asset.build_batch_request()
# </snippet>

# <snippet name="add_expectation_suite">
expectation_suite = context.add_expectation_suite(expectation_suite_name = "my expectation suite")
# </snippet>

# <snippet name="validator">
validator = context.get_validator(expectation_suite=expectation_suite, batch_request=batch_request)
# </snippet>













