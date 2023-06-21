# Initialization
# <snippet name="initial import">
# Initialize GX and data context
import great_expectations as gx
context = gx.get_context()
# </snippet>


# Datasources
# <snippet name="add_pandas">
# Instantiate your datasource
datasource = context.sources.add_pandas(name = 'pandas datasource')
# </snippet>

# <snippet name="add_pandas_filesystem">
# Instantiate your datasource
datasource = context.sources.add_pandas_filesystem(name = 'pandas filesystem datasource', base_directory = '/path/to/your/files/')
# </snippet>

# <snippet name="add_sql">
# Instantiate your datasource
datasource = context.sources.add_sql(name = 'sql datasource', connection_string = 'your_connection_string')
# </snippet>

# Assets
# <snippet name="add_csv_asset">
# Instantiate your asset
asset = datasource.add_csv_asset(name = 'csv asset', batching_regex = "your_data.csv")
# </snippet>

# <snippet name="add_dataframe_asset">
# Instantiate your asset
import pandas as pd
your_df = pd.read_csv("/path/to/your/df.csv")

asset = datasource.add_dataframe_asset(name = 'dataframe asset', dataframe = your_df)
# </snippet>

# <snippet name="add_query_asset">
# Instantiate your asset
asset = datasource.add_query_asset(name = 'sql asset', query = "your query")
# </snippet>

# <snippet name="add_table_asset">
# Instantiate your asset
asset = datasource.add_table_asset(name = 'table asset', table_name = "sql_table_name")
# </snippet>


# Splitters
# <snippet name="add_splitter_column_value">
# Instantiate your splitters
asset.add_splitter_column_value(column_name = "your_column")
# </snippet>

# Batch Request
# <snippet name="build_batch_request">
# Instantiate your batch request
batch_request = asset.build_batch_request()
# </snippet>

# <snippet name="add_expectation_suite">
# Add your expectation suite
expectation_suite = context.add_expectation_suite(expectation_suite_name = "my expectation suite")
# </snippet>

# <snippet name="validator">
# Create your validator
validator = context.get_validator(expectation_suite=expectation_suite, batch_request=batch_request)
# </snippet>

# <snippet name="expectations">
# Run your expectations here
validator.expect_your_expectations()
# </snippet>

# <snippet name="save_expectation_suite">
# Save your expectation suite
validator.save_expectation_suite(discard_failed_expectations=False)
# </snippet>

# <snippet name="checkpoint">
# Call and run your checkpoint
checkpoint = gx.checkpoint.SimpleCheckpoint(name = 'checkpoint', data_context = context, validator = validator)
checkpoint_result = checkpoint.run()

result = checkpoint_result.list_validation_result_identifiers()[0]
# </snippet>


# <snippet name="datadocs">
# Build and open data docs
context.build_data_docs(result)
context.open_data_docs(result)
# </snippet>

